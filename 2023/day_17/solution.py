from pathlib import Path
from itertools import product
from queue import PriorityQueue

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

    BASE_OPTIONS = {
        NORTH:[EAST,WEST],
        SOUTH:[EAST,WEST],
        EAST:[NORTH,SOUTH],
        WEST:[NORTH,SOUTH]
    }

    def __init__(self, source):
        self.grid = self.get_data(source)
        self.yrange = len(self.grid)-1
        self.xrange = len(self.grid[0])-1

    def get_data(self, source):
        with open(Path(r'C:\Users\cermit\source\repos\aoc\2023\day_17'+f'\\{source}'),'r',encoding='ascii') as input_data:
            return [list(map(int,x.strip())) for x in input_data.readlines()] 

    def get_options(self, pos: vector, dir: vector, count: int) -> vector:
        # returns a list of vectors
        base = [(pos+dr,dr,1) for dr in self.BASE_OPTIONS[dir]]
        if count<3:
            base.append((pos+dir,dir,count+1))
        return [bas for bas in base if bas[0][0] >=0
            and bas[0][1]>= 0 
            and bas[0][0]<=self.yrange
            and bas[0][1]<=self.xrange]

    def get(self, vector):
        if (vector[0] <0
            or vector[1]< 0 
            or vector[0]>self.yrange
            or vector[1]>self.xrange):
            return None
        return self.grid[vector[0]][vector[1]]

    def print(self):
        for line in self.grid:
            print(line)
        print()
 
    def path_find(self):
        frontier = PriorityQueue()
        lava = vector([0,0])
        mecha = vector([self.yrange, self.xrange])
        dads = {lava: None}
        costs = {lava:0}
        # Frontier object will be (priority, (vector,dir,count))
        frontier.put((0,lava,EAST,0))
        while not frontier.empty():
            front = frontier.get()
            # if front[1] == mecha:
            #     break
            for pfront in self.get_options(*front[1:]):
                p_cost = costs[front[1]] + self.get(pfront[0])
                if pfront[0] in costs and p_cost< costs[pfront[0]]:
                    continue
                costs[pfront[0]] = p_cost
                frontier.put((p_cost, *pfront))
                dads[pfront[0]]=front[1]
        # for pair in dads.items():
        #     print(pair)
        return costs[mecha]

def part1(source):
    g = grid(source)
    print([g.path_find()])

if __name__ == '__main__':
    part1('test')
