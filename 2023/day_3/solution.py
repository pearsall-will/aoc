from pathlib import Path
DIGITS = ('1','2','3','4','5','6','7','8','9','0')
NON_SYMBOLS = ('1','2','3','4','5','6','7','8','9','0','.')
GEAR_SYMBOL = '*'

# part 1
def part1(source, line_length: int):
    with open(Path(r'C:\Users\cermit\source\repos\aoc\2023\day_3'+f'\\{source}'),'r') as input_data:
        parts = []
        current_number = ''
        current_digit_range = set()
        text_data = input_data.read().replace('\n','.')

        for i, x in enumerate(text_data):
            if x in DIGITS:
                current_number += x
                for n in [-1,0,1]:
                    if i+n > -1 and i+n <len(text_data): current_digit_range.add(i+n)
                    if i-line_length+n>-1: current_digit_range.add(i-line_length+n)
                    if i+line_length+n<len(text_data): current_digit_range.add(i+line_length+n)
            elif current_number:
                for i in current_digit_range:
                    if (text_data[i] not in NON_SYMBOLS):
                        parts.append(int(current_number))
                        break
                current_number = ''
                current_digit_range = set()
    print(sum(parts))

# part 2
def part2(source: str, line_length: int):
    with open(Path(r'C:\Users\cermit\source\repos\aoc\2023\day_3'+f'\\{source}'),'r') as input_data:
        gears = {}
        current_number = ''
        current_digit_range = set()
        text_data = input_data.read().replace('\n','.')

        for i, x in enumerate(text_data):
            if x in DIGITS:
                current_number += x
                for n in [-1,0,1]:
                    if i+n > -1 and i+n <len(text_data): current_digit_range.add(i+n)
                    if i-line_length-1+n>-1: current_digit_range.add(i-line_length+n)
                    if i+line_length+1+n<len(text_data): current_digit_range.add(i+line_length+n)
            elif current_number:
                intnum = int(current_number)
                for i in current_digit_range:
                    if text_data[i] == GEAR_SYMBOL:
                        try:
                            gears[i].append(intnum)
                        except:
                            gears[i]=[intnum]
                        break
                current_number = ''
                current_digit_range = set()
    print(sum([gear[0]*gear[1] for gear in gears.values() if len(gear)==2]))


part2('input', 141)