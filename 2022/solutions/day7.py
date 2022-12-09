from aocd import lines
from itertools import chain


class Command:
    def __init__(self, command, param) -> None:
        self.command = command
        self.param = param
        self.results = []

    def append(self, result):
        first, second = result.split()
        if first == "dir":
            node_type, name = first, second
            self.results.append(Node(node_type, name, 0, []))
        else:
            size, name = first, second
            self.results.append(Node("file", name, size, []))

    def __repr__(self):
        return f"Command({self.command}, {self.param}, {self.results})"


class Node:
    def __init__(self, node_type, name, size, children):
        self.type = node_type
        self.name = name
        self.size = int(size)
        self.children = children
        self.parent = None

    @property
    def total_size(self):
        if self.size > 0:
            return self.size
        else:
            size = sum(child.total_size for child in self.children)
            self.size = size
            return size

    def __repr__(self):
        return f"Node({self.type}, {self.name}, {self.size}, {self.parent}, {self.children})"


def parse_commands(lines):
    commands = []
    command = None
    for line in lines:
        if line.startswith("$"):
            if command:
                commands.append(command)
            _, command_name, *params = line.split()
            param = params[0] if len(params) > 0 else None
            command = Command(command_name, param)
        else:
            command.append(line)
    commands.append(command)

    return commands


def construct_tree(commands):
    top_node = Node("dir", "root", 0, [])
    current_node = top_node
    for command in commands:
        if command.command == "cd":
            if command.param == "..":
                current_node = current_node.parent
            else:
                children_with_name = [
                    n for n in current_node.children if n.name == command.param
                ]
                if len(children_with_name) == 0:
                    new_node = Node("dir", command.param, 0, [])
                    current_node.children.append(new_node)
                    current_node = new_node
                else:
                    current_node = children_with_name[0]
        elif command.command == "ls":
            for result in command.results:
                result.parent = current_node
                current_node.children.append(result)
    return top_node


def traverse(node):
    res = []
    if node:
        res.append((node.type, node.name, node.total_size))
        res.extend(chain(*[traverse(child) for child in node.children]))
    return res


def print_tree(node, depth=0):
    if node:
        print("  " * depth + f"{node.type} {node.name} {node.size}")
        for child in node.children:
            print_tree(child, depth + 2)


def main():
    commands = parse_commands(lines)
    tree = construct_tree(commands)
    all_nodes = traverse(tree)
    total_size = tree.total_size
    max_size = 70000000
    needed_unused_space = 30000000
    desired_max_size = max_size - needed_unused_space
    print(
        "Part 1:",
        sum([node[2] for node in all_nodes if node[0] == "dir" and node[2] < 100000]),
    )
    print(
        "Part 2:",
        min(
            [
                node[2]
                for node in all_nodes
                if total_size - node[2] < desired_max_size and node[0] == "dir"
            ]
        ),
    )


if __name__ == "__main__":
    main()
