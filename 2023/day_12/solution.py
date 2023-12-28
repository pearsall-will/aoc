from pathlib import Path
from functools import cache

@cache
def check_data(data, pmap):
    dmap = tuple([x for x in data.split('.') if x])
    # No mapping conditions left. Check for # or rows. 0 means impossible state. 1 otherwise.
    if len(pmap) == 0:
        if '#' in data: return 0
        return 1
    
    # If no more variance validate pmap vs len of each map in dmap, which should be all #
    if '?' not in data: return int(tuple([len(x) for x in dmap])==pmap)
    
    # If no more variance in last block. Check lengths, if not matched then block is invalid, else return check of data subset.
    if '?' not in dmap[-1]:
        if pmap[-1] == len(dmap[-1]): 
            return check_data('.'.join(dmap[:-1]), pmap[:-1])
        return 0
    # Same as above but first block. Order here is largely arbitrary tbh.
    if '?' not in dmap[0]: 
        if pmap[0] == len(dmap[0]): 
            return check_data('.'.join(dmap[1:]), pmap[1:])
        return 0
    # Return a new check replaceing the possible characters as no exit condition was reached.
    return check_data(data.replace('?','.',1), pmap) + check_data(data.replace('?','#',1),pmap)



def part1(source):
    with open(Path(r'C:\Users\cermit\source\repos\aoc\2023\day_12'+f'\\{source}'),'r') as input_data:
        g = 0
        for line in input_data.readlines():
            data, data_map = line.strip().split(' ')
            data = '?'.join([data]*5)
            pmap = [int(i) for i in data_map.split(',')] * 5
            g+=check_data(data, tuple(pmap))
            print(g)
        return g

if __name__ == '__main__':
    print(part1('input'))



