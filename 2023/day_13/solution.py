from pathlib import Path

def list_compare(list1, list2, part2=False):
    if part2:
        smudge=False
    else:
        smudge=True
    for x in range(len(list1)):
        if list1[x] == list2[x]:
            continue
        if list1[x] != list2[x]:
            if smudge or len([c for i,c in enumerate(list1[x]) if c!=list2[x][i]]) > 1:
                return False
            smudge = True
    return smudge

def index_of_split(grid, vert=100, part2=False):
    for adj in range(len(grid)):
        if adj == 0:
            continue
        window = min(len(grid)-adj,adj)
        if list_compare(grid[adj-window:adj], grid[adj:adj+window][::-1],part2=part2):
            return vert*adj
    return index_of_split(rotated(grid), 1, part2)

def rotated(grid):
    return list(zip(*grid[::-1]))

def gridify(block):
    return [list(x) for x in block if x]

def part1(source,part2=False):
    with open(Path(r'C:\Users\cermit\source\repos\aoc\2023\day_13'+f'\\{source}'),'r') as input_data:
        return sum(index_of_split(gridify(block.split('\n')), part2=part2) for block in input_data.read().split('\n\n'))

if __name__ == '__main__':
    # print(part1('input'))
    print(part1('input',True))
