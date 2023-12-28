from pathlib import Path
from math import sqrt


def build_grid(source, time):
    with open(Path(r'C:\Users\cermit\source\repos\aoc\2023\day_11'+f'\\{source}'),'r') as input_data:
        rows = []
        galaxies = []
        galaxy_cols = set()
        for i, line in enumerate(input_data.readlines()):
            glenth = len(line)
            line = line.strip('\n')
            if '#' in line:
                galaxy_cols.update([n for n, x in enumerate(line) if x=='#'])
                galaxies.extend([(i,x) for x,c in enumerate(line) if c=='#'])
            else:
                rows.append(i)
    cols = [col for col in range(glenth) if col not in galaxy_cols]
    gsum = 0
    for i, g in enumerate(galaxies[:-1]):
        for g2 in galaxies[i:]:
            if g2==g:
                continue
            v = len([x for x in cols 
                     if (x>g[1] and x <g2[1])
                     or (x<g[1] and x >g2[1])])*(time)
            h = (len([x for x in rows
                     if (x>g[0] and x<g2[0])
                     or (x<g[0] and x>g2[0])])*(time))
            nsum = abs(g[0]-g2[0])+abs(g[1]-g2[1])
            gsum += nsum+v+h
    return gsum

if __name__ == '__main__':
    print(build_grid('input', 1000000-1))


