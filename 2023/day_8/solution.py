from math import lcm
from pathlib import Path
from itertools import cycle

def mstrip(string: str, chars: str) -> str:
    for char in chars:
        string = string.replace(char,'')
    return string

def part1(source):
    with open(Path(r'C:\Users\cermit\source\repos\aoc\2023\day_8'+f'\\{source}'),'r') as input_data:
        lr = input_data.readline().strip('\n')
        print(lr)
        nodes = {}
        start_nodes = []
        for line in input_data.read().split('\n'):
            if line =='':
                continue
            tag, lrvals = mstrip(line,' ()').split('=')
            if tag[-1] == 'A':
                start_nodes.append(tag)
            lrsplit = lrvals.split(',')
            nodes[tag] = {
                "L": lrsplit[0],
                "R": lrsplit[1]
            }
        steps = 0
        orbit_maps = {}
        for start_node in start_nodes:                
            next_node = start_node
            orbit_maps[next_node] = {"start": 0}
            for x,i in enumerate(cycle(lr)):
                steps += 1
                next_node = nodes[next_node][i]
                if next_node[-1] == "Z":
                    if orbit_maps[start_node]["start"] > 0:
                        orbit_maps[start_node]["length"] = 1+x-orbit_maps[start_node]["start"]
                        break
                    orbit_maps[start_node]["start"] = x+1
        base_iter = max(orbit_maps.values(), key=lambda e: e["length"])
        i = sum(base_iter.values())
        print(orbit_maps)
        n=1
        return lcm(
            *[x for x,y in [x.values() for x in orbit_maps.values()]]
        )

if __name__ == '__main__':
    print(part1('input'))