from pathlib import Path
from itertools import combinations
from math import ceil
from collections import deque

NORTH = (-1,0)
SOUTH = (1,0)
EAST = (0,1)
WEST = (0,-1)

CHECK_DIRS = {
    NORTH: EAST,
    EAST: SOUTH,
    SOUTH: WEST,
    WEST: NORTH
}

def sum_vec(*vectors: tuple) -> tuple:
    try:
        return (sum(vector[0] for vector in vectors),
                sum(vector[1] for vector in vectors)
        )
    except:
        return None

def diff_vec(vector1: tuple, vector2: tuple) -> tuple:
    return (vector1[0]-vector2[0],vector1[1]-vector2[1])

def map_char(char: str, position: tuple, start_position: list) -> tuple | str:
    match char:
        case '.': return 'NONE'
        case '-': return (EAST,WEST)
        case '|': return (NORTH,SOUTH)
        case 'L': return (NORTH,EAST)
        case 'J': return (NORTH,WEST)
        case 'F': return (SOUTH,EAST)
        case '7': return (WEST,SOUTH)
        case 'S':
            start_position[0], start_position[1] = position
            return 'Start'


def get_pos(grid: list, vector: tuple):
    return grid[vector[0]][vector[1]]


def build_grid(source):
    with open(Path(r'C:\Users\cermit\source\repos\aoc\2023\day_10'+f'\\{source}'),'r') as input_data:
        grid = []
        start_position = [0,0]
        for y,line in enumerate(input_data.readlines()):
            # state hack since lists are passed by reference by default.
            grid.append([map_char(char,(y,x),start_position) for x,char in enumerate(line.strip('\n'))])
        start_position = tuple(start_position)
        for y, line in enumerate(grid):
            for x, pos in enumerate(line):
                if not isinstance(pos,str):
                    grid[y][x]= {
                    sum_vec((y,x),l):sum_vec((y,x),r) for l,r in combinations(pos,2)
                    }
                    grid[y][x].update(
                        {
                            value:key for key,value in grid[y][x].items()
                        }
                    )
    return start_position,grid

def part1(source):
    start_position, grid = build_grid(source)
    for start in [NORTH,SOUTH,EAST,WEST]:
        i = 1
        current_position = start_position
        next_position = sum_vec(start_position, start)
        try:
            while next_position!=start_position:
                last_position = current_position
                current_position = next_position 
                next_position = get_pos(grid, current_position)[last_position]
                i +=1
        except:
            continue
        return ceil(i/2)
NORTH, EAST, SOUTH, WEST
def part2(source):
    start_pos, grid = build_grid(source)
    for start in [NORTH,SOUTH,EAST,WEST]:
        path = []
        current_position = start_pos
        path.append(current_position)
        next_position = sum_vec(start_pos, start)
        try:
            while next_position!=start_pos:
                last_position = current_position
                current_position = next_position
                path.append(current_position)
                next_position = get_pos(grid, current_position)[last_position]
        except:
            continue
        break
    first = None
    for y,line in enumerate(grid):
        for x in range(len(line)):
            if (y,x) not in path:
                grid[y][x] = None
            elif first is None:
                first = (y,x)
    contained = set()
    start_i = path.index(first)
    path = path[start_i:]+path[:start_i]
    path = path[::-1]
    for i, vector in enumerate(path):
        check_dir1 = CHECK_DIRS[diff_vec(vector, path[i-1])]
        try:
            check_dir2 = CHECK_DIRS[diff_vec(path[i+1],vector)]
        except:
            break
        for check_dir in (check_dir1,check_dir2):
            check_path = sum_vec(vector, check_dir)
            if check_path[0] < 0 or check_path[1] < 0:
                continue
            try:
                while get_pos(grid,check_path) == None:
                    if check_path[0]<0 or check_path[1]<0:
                        break
                    contained.add(check_path)
                    check_path = sum_vec(check_dir, check_path)
            except:
                continue
    return(len(contained))


if __name__ == '__main__':
    print(part2('input'))
