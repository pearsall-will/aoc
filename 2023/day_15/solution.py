from pathlib import Path
from collections import OrderedDict
import re


def get_data(source):
    with open(Path(r'C:\Users\cermit\source\repos\aoc\2023\day_15'+f'\\{source}'),'r',encoding='ascii') as input_data:
        return [x for x in input_data.read().strip('\n').split(',')]

def hash(str, currentvalue=0):
    for i,c in enumerate(str):
        return hash(str[i+1:],((currentvalue+ord(c))*17)%256)
    return currentvalue

def part1(source):
    return(sum([hash(x) for x in get_data(source)]))

def part2(source):
    HASHMAP = {x:OrderedDict() for x in range(256)}
    for lens in get_data(source):
        label = re.split('[-|=]',lens)
        lenshash=hash(label[0])
        try:
            HASHMAP[lenshash][label[0]] = int(label[1])
        except:
            try:
                del HASHMAP[lenshash][label[0]]
            except:
                pass
    s = 0
    for h, dic in HASHMAP.items():
        for n,x in enumerate(dic.values()):
            s+=(n+1) * (h+1) * (x)
    return s
if __name__ == '__main__':
    print(part2('input'))
