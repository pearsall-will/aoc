from pathlib import Path
from itertools import product
import re


class vector(tuple):
    def __add__(self, other):
        if not isinstance(other,vector):
            raise TypeError('Vector cannot be added to non Vector')
        return vector([self[i]+n for i,n in enumerate(other)])

NORTH = vector((-1,0))
SOUTH = vector((1,0))
EAST = vector((0,1))
WEST = vector((0,-1))

TRANSFORM = {
    NORTH:{'/':[EAST],'-':[EAST,WEST],'|':[NORTH],'.':[NORTH],'\\':[WEST]},
    SOUTH:{'/':[WEST],'-':[EAST,WEST],'|':[SOUTH],'.':[SOUTH],'\\':[EAST]},
    EAST:{'/':[NORTH],'-':[EAST],'|':[NORTH,SOUTH],'.':[EAST],'\\':[SOUTH]},
    WEST:{'/':[SOUTH],'-':[WEST],'|':[NORTH,SOUTH],'.':[WEST],'\\':[NORTH]}
}

class grid:

    def __init__(self, source):
        self.grid = self.get_data(source)
        self.yrange = len(self.grid)-1
        self.xrange = len(self.grid[0])-1
        self.pathed = set()
        self.walked = set()

    def get_data(self, source):
        with open(Path(r'C:\Users\cermit\source\repos\aoc\2023\day_16'+f'\\{source}'),'r',encoding='ascii') as input_data:
            return [list(x.strip()) for x in input_data.readlines()]

    def reset(self):
        self.pathed = set()
        self.walked = set()  

    def get(self, vector):
        if (vector[0] <0
            or vector[1]< 0 
            or vector[0]>self.yrange
            or vector[1]>self.xrange):
            return None
        return self.grid[vector[0]][vector[1]]


    def path_laser(self, position: vector, direction:vector) -> set:
        self.pathed.add(position)
        while True:
            if (position,direction) in self.walked:
                return
            self.walked.add((position,direction))
            position = position + direction
            nval = self.get(position)
            if not nval:
                return
            self.pathed.add(position)
            dirs = TRANSFORM[direction][nval]
            if len(dirs) != 1:
                break
            direction = dirs[0]
        [self.path_laser(position, dir) for dir in TRANSFORM[direction][nval]]

def part1(source):
    lens=[]
    g = grid(source)
    xrange,yrange = g.xrange,g.yrange
    iterstarts = [(vector([y,x]),dir) for y,x,dir in product(range(yrange+1),(0,xrange),[NORTH,SOUTH,EAST,WEST])]
    iterstarts.extend([(vector([y,x]),dir) for y,x,dir in product((0,yrange),range(xrange+1),[NORTH,SOUTH,EAST,WEST])])
    paths = []
    for start in iterstarts:
        g.path_laser(start[0],start[1])
        paths.append(len(g.pathed))
        g.reset()
    print(max(paths))

if __name__ == '__main__':
    part1('input')
