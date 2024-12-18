from aocd import data
from util import delimit
import re

class Computer:
    def __init__(self, registers, program):
        self.program = program
        a, b, c = registers
        self.A, self.B, self.C = a[1], b[1], c[1]
        self.instruction = 0
        self.outputs = []
        self.operations = [self.adv, self.bxl, self.bst, self.jnz, self.bxc, self.out, self.bdv, self.cdv]

    def run(self):
        while self.instruction < len(self.program):
            opcode, operand = self.program[self.instruction:self.instruction+2]
            jump = self.operations[opcode](operand)
            self.instruction = jump if jump is not None else self.instruction + 2
        return ",".join([str(v) for v in self.outputs])

    def combo(self, code):
        if code <= 3:
            return code
        elif 4 <= code <= 6:
            return [self.A, self.B, self.C][code - 4]
        raise ValueError(f'Invalid combo operand: {code}')

    def adv(self, operand): self.A //= 2 ** self.combo(operand)
    def bxl(self, operand): self.B ^= operand
    def bst(self, operand): self.B = self.combo(operand) % 8
    def jnz(self, operand): return operand if self.A != 0 else None
    def bxc(self, _): self.B ^= self.C
    def out(self, operand): self.outputs.append(self.combo(operand) % 8)
    def bdv(self, operand): self.B = self.A // 2 ** self.combo(operand)
    def cdv(self, operand): self.C = self.A // 2 ** self.combo(operand)

def main():
    registers, program = parse()
    computer = Computer(registers, program)
    print("Part 1:", computer.run())

def parse():
    registers, program = delimit(data.splitlines())
    captures = [re.match(r'Register (.): (\d+)', register) for register in registers]
    registers = [(v.group(1), int(v.group(2))) for v in captures]
    program = [int(v) for v in re.findall(r'(\d+)', program[0])]
    return registers, program

if __name__ == '__main__':
    main()
