from pathlib import Path



    # | is a vertical pipe connecting north and south.
    # - is a horizontal pipe connecting east and west.
    # L is a 90-degree bend connecting north and east.
    # J is a 90-degree bend connecting north and west.
    # 7 is a 90-degree bend connecting south and west.
    # F is a 90-degree bend connecting south and east.
    # . is ground; there is no pipe in this tile.
    # S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

NORTH = (-1,0)
SOUTH = (1,0)
EAST = (0,1)
WEST = (0,-1)

def add_vector(*vectors: tuple) -> tuple:
    return (sum(vector[0] for vector in vectors),
              sum(vector[1] for vector in vectors))

def map_char(chr: str) -> list:
    match chr:
        case '-':
            return [EAST,WEST]
        case '|':
            return [NORTH,SOUTH]
        case 'L':
            return [NORTH,EAST]
        case 'J':
            return [WEST,NORTH]
        case '7':
            return [WEST,SOUTH]
        case 'F':
            return [SOUTH,EAST]
        case '.':
            return None
        case 'S':
            return 'start'

def part1(source):
    with open(Path(r'C:\Users\cermit\source\repos\aoc\2023\day_10'+f'\\{source}'),'r') as input_data:
        parsed_map=[]
        for y, line in enumerate(input_data.readlines()):
            parsed_map.append([])
            for x, chr in enumerate(line.strip('\n')):
                parsed_map[y].append(map_char(chr))
                if parsed_map[y][x] == 'start':
                    start_pos = (y,x)
        
        for path in [NORTH, SOUTH, EAST, WEST]:
            last_pos = start_pos
            cur_pos = add_vector(last_pos, path)
            print(f"{cur_pos},{start_pos}")
            try:
                i=1
                while cur_pos!=start_pos:
                    nextors = [add_vector(cur_pos, vector) for vector in parsed_map[cur_pos[0]][cur_pos[1]]]
                    cur_pos = next(nextor for nextor in nextors if nextor != last_pos)
                    print(f"{cur_pos},{last_pos}, {nextors}, {bool(nextors[0]==last_pos)}")
                    # print(f"{cur_pos},{start_pos}")
                    last_pos=cur_pos
                    i+=1
            except Exception as e:
                print(e)
                continue
            return i

if __name__ == '__main__':
    print(part1('test'))
