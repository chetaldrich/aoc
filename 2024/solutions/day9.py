from aocd import data
import numpy as np
from copy import deepcopy

def main():
    disk = parse()
    compacted = compact(deepcopy(disk))
    smart_compacted = smart_compact(disk)
    print("Part 1:", checksum(compacted))
    print("Part 2:", checksum(smart_compacted))

def checksum(disk):
    return sum(i * int(d) for i, d in enumerate(disk) if d != -1)

def smart_compact(disk):
    unique_ids = set(disk) - {-1}
    contiguous_blocks = contiguous_free(disk)
    start_indices = { id: count_and_start(disk, id) for id in unique_ids }
    for id, (start, count) in sorted(start_indices.items(), reverse=True, key=lambda x: x[0]):
        free_block_start = min([i for i, len_block in contiguous_blocks.items() if len_block >= count], default=float("inf"))
        if free_block_start <= start:
            for i in range(free_block_start, free_block_start+count):
                disk[i] = id
            for i in range(start, start+count):
                disk[i] = -1
            contiguous_blocks = contiguous_free(disk)
    return disk

def contiguous_free(disk):
    contiguous_free_blocks = {}
    count = 0
    for i, d in enumerate(disk):
        if d == -1:
            count += 1
        elif count > 0:
            contiguous_free_blocks[i-count] = count
            count = 0
    return contiguous_free_blocks

def count_and_start(disk, id):
    indices = np.argwhere(disk==id)
    return min(indices)[0], len(indices)

def compact(disk):
    last_index = len(disk)-1
    empties = np.argwhere(disk==-1)
    for i in empties:
        if last_index <= i:
            break
        disk[i] = disk[last_index]
        disk[last_index] = -1
        while disk[last_index] == -1:
            last_index -= 1
    return disk

def parse():
    block = []
    for i, c in enumerate(data):
        file_id = i // 2 if i % 2 == 0 else -1
        block.extend([file_id] * int(c))
    return np.array(block)

if __name__ == '__main__':
    main()
