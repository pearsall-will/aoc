from pathlib import Path
import re

def clean_line(line):
    return line.replace('one','1').replace('two','2').replace('three','3').replace('four','4').replace('five','5').replace('six','6').replace('seven','7').replace('eight','8').replace('nine','9').strip('\r\n')

def clean_line_back(line):
    return line.replace('eno','1').replace('owt','2').replace('eerht','3').replace('ruof','4').replace('evif','5').replace('xis','6').replace('neves','7').replace('thgie','8').replace('enin','9').strip('\r\n')

num_text_map = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
    '1':'1',
    '2':'2',
    "3":'3',
    '4':'4',
    '5':'5',
    '6':'6',
    '7':'7',
    '8':'8',
    '9':'9'
}

def getleft(line):
    return num_text_map[re.search(r'\d|one|two|three|four|five|six|seven|eight|nine',line).group(0)]


def getright(line):
    return num_text_map[re.search(r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin',line[::-1]).group(0)[::-1]]


with open(Path(r'aoc\2023\day_1\input'),'r') as input_data:
# #     # print(f'Part 1: {sum([int(re.search('\d',line).group(0) + re.search('\d',line[::-1]).group(0)) for line in input_data])}')
    print(f'Part 2: {sum([int(getleft(line) + getright(line)) for line in input_data])}')
#     for line in input_data:
#         print(f'{line.strip('\r\n')} |{clean_line(line)}|{re.search('\d',clean_line(line)).group(0) + re.search('\d',clean_line_back(line[::-1])).group(0)}')
