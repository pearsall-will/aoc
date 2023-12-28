from pathlib import Path
import itertools
import copy
from functools import cache

class vector(tuple):
    def __add__(self, other):
        if not isinstance(other,vector):
            raise TypeError('Vector cannot be added to non Vector')
        return vector([self[i]+n for i,n in enumerate(other)])

NORTH = vector((-1,0))
SOUTH = vector((1,0))
EAST = vector((0,1))
WEST = vector((0,-1))

class grid:

    def __init__(self, block):
        self.data = [list(x.strip()) for x in block if x]
        self.xrange = range(len(self.data[0]))
        self.yrange = range(len(self.data))

    def get(self, vector, force=False):
        if (vector[0] <0
            or vector[1]< 0 
            or vector[0]>self.yrange[-1]
            or vector[1]>self.xrange[-1]):
            return None
        return self.data[vector[0]][vector[1]]
    
    def set(self, vector, value):
        self.data[vector[0]][vector[1]] = value

    def cycle(self):
        for dir in [NORTH,WEST,SOUTH,EAST]:
            self.tilt(dir)
        return self.getstate()

    def tilt(self, direction):
        ydir = direction[0]*-1 if direction[0]*-1 else 1
        xdir = direction[1]*-1 if direction[1]*-1 else 1
        for vec in [vector((y,x))for y,x in itertools.product(self.yrange[::ydir], self.xrange[::xdir])]:
            if self.get(vec)!='O':
                continue
            while self.get(vec+direction)=='.':
                self.set(vec,self.get(vec+direction))
                vec = vec+direction
                self.set(vec,'O')

    def calc_sum(self):
        return sum(len(self.data)-y for y,x in itertools.product(self.yrange, self.xrange) if self.get((y,x))=='O')

    def getstate(self):
        return tuple(map(tuple, self.data))

    def print(self):
        for line in self.data:
            print(''.join(line))
        print()

def get_data(source):
    with open(Path(r'C:\Users\cermit\source\repos\aoc\2023\day_14'+f'\\{source}'),'r') as input_data:
        return grid(input_data.readlines())

def part1(source):
    data = get_data(source)
    data.tilt(NORTH)
    return data.calc_sum()

def check_lists(l1,l2):
    try:
        for i,x in enumerate(l1):
            if l2[i]!=x:
                return False
        return True
    except:
        return False

def part2(source):
    data = get_data(source)
    states = {data.getstate(): data.calc_sum()}
    statelist = [data.getstate()]
    while (state:=data.cycle()) not in states:
        statelist.append(state)
        states[state] = data.calc_sum()
    idx = statelist.index(state)
    statelist = statelist[idx:]
    calcstate = 1000000000 % len(statelist)
    print([states.values(),idx,calcstate],sep='\n')
    return states[statelist[calcstate-idx]]

if __name__ == '__main__':
    print(part2('input'))
