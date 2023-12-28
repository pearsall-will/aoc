from pathlib import Path
from math import sqrt, floor

def part1(source, ):
    with open(Path(r'C:\Users\cermit\source\repos\aoc\2023\day_6'+f'\\{source}'),'r') as input_data:

        times = [int(x) for x in input_data.readline()[:-1].split(' ') if x.isnumeric()]
        distances = [int(x) for x in input_data.readline()[:-1].split(' ') if x.isnumeric()]
        possible = [
            len([x for x in range(1,distance+1) if (time-x)*x>distance ])
            for time, distance in zip(times,distances)
            ]
        ret=1
        for x in possible:
            ret=x*ret
        return ret

def part2(source, ):
    with open(Path(r'C:\Users\cermit\source\repos\aoc\2023\day_6'+f'\\{source}'),'r') as input_data:

        time = int(''.join([x for x in input_data.readline()[:-1].split(' ') if x.isnumeric()]))
        distance = int(''.join([x for x in input_data.readline()[:-1].split(' ') if x.isnumeric()]))
        for i,x in enumerate(range(round(time/2), time+1)):
            if (time-x)*x < distance:
                if(time % 2 ==0):
                    return(i*2+1)
                else:
                    return((i*2))
        else:
            return time
    

# print(part1('input'))

print(part2('test'))