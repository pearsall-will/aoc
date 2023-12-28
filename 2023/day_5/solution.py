from pathlib import Path
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor, as_completed


def get_value(lookup, ranges):
    for range in ranges:
        range_diff = lookup-range[1]
        if range_diff>=0 and range_diff <=range[2]:
            return range[0]+range_diff
    return lookup

def walk_garden_map(lookup, garden_map, seed_map, entry):
    try:
        target = garden_map[entry]['maps_to']
        seed_map[target] = get_value(lookup, garden_map[entry]['ranges'])
        walk_garden_map(seed_map[target], garden_map, seed_map, garden_map[entry]["maps_to"],)
        return seed_map
    except KeyError:
        return seed_map


def build_maps(source, seeds_are_ranges=False):
    with open(Path(r'C:\Users\cermit\source\repos\aoc\2023\day_5'+f'\\{source}'),'r') as input_data:
        raw_seeds = [int(x) for x in input_data.readline()[7:-1].split(' ')]
        if seeds_are_ranges:
            seeds = [list(a) for a in zip(raw_seeds[::2], raw_seeds[1::2])]
        else:
            seeds = raw_seeds
        map_name = ''
        garden_maps = {}
        for line in input_data.readlines():
            line = line.replace('\n', '')
            if not line:
                map_name =''
                continue
            if map_name:
                garden_maps[map_name]["ranges"].append([int(x) for x in line.split(' ')])
                continue
            map_name = line.split(' ')[0].split('-')[0]
            garden_maps[map_name]= {"maps_to": line.split(' ')[0].split('-')[-1],
                                    "ranges":[]}
    for garden_map in garden_maps:
        try:
            garden_maps[garden_maps[garden_map]["maps_to"]]["maps_from"] = garden_map
        except:
            pass

    return seeds, garden_maps


def part1(source):
    seeds, garden_maps = build_maps(source)
    seed_report = {}
    for seed in seeds:
        seed_report={}
        seed_report[seed] = walk_garden_map(seed,garden_maps,seed_report,'seed')
    print(min([
        x['location'] for x in seed_report.values()
    ]))


def get_value(lookup, ranges):
    for range in ranges:
        range_diff = lookup-range[1]
        if range_diff>=0 and range_diff < range[2]:
            return range[0]+range_diff
    return lookup

def walk_garden_map(lookup, garden_map, seed_map, entry):
    try:
        target = garden_map[entry]['maps_to']
        seed_map[target] = get_value(lookup, garden_map[entry]['ranges'])
        walk_garden_map(seed_map[target], garden_map, seed_map, garden_map[entry]["maps_to"],)
        return seed_map
    except KeyError:
        return seed_map

def check_range(lookup_range: list, mapping_ranges: list) -> list:
    check_vals = []
    return_vals = []
    for vals in mapping_ranges:
        check_vals.append(vals[1])
        check_vals.append(vals[1]+vals[2])
    endval = lookup_range[1]+lookup_range[0]
    check_vals.append(endval)
    check_vals.sort()
    while True:
        x1 = lookup_range[0]
        y1 = min(next(x for x in check_vals if x>x1),endval)
        return_vals.append([x1,y1])
        if y1==endval:
            break
        lookup_range[0] = next(x for x in check_vals if x>y1-1)
        lookup_range[1] = lookup_range[0]-x1
    # print(str(return_vals)+'\n')
    return [[get_value(s, mapping_ranges), r-s] for s, r in return_vals]

def walk_range(raw_range: list, garden_map: dict, entry: str) -> int:
    if entry == 'location':
        return raw_range[0]
    target = garden_map[entry]['maps_to']
    return min(walk_range(x, garden_map, target) for x in check_range(raw_range,garden_map[entry]["ranges"])) 

def part2(source):
    seedranges, report = build_maps(source, True)
    futures = []
    return min(walk_range(seed, report, 'seed') for seed in seedranges)


if __name__=='__main__':
    print(part2('input'))
