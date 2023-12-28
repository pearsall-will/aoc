from pathlib import Path

# part 1
def part1(source):
    with open(Path(r'C:\Users\cermit\source\repos\aoc\2023\day_4'+f'\\{source}'),'r') as input_data:
        data_struct = {}
        total=0
        for line in input_data:
            key = int(line.split(' ')[-1][:-1])
            left, right = line.split(':')[1].split('|')
            winners = set([int(x) for x in left.split(' ') if x.isnumeric()])
            numbers = [int(x) for x in right.split() if x.isnumeric()]
            points = int(2 ** (len([x for x in numbers if x in winners])-1))
            data_struct[key]= {"winners":winners, "numbers": numbers, "points": points}
            total += points
        print(data_struct)
        print(total)



# part 2
def part2(source):
    with open(Path(r'C:\Users\cermit\source\repos\aoc\2023\day_4'+f'\\{source}'),'r') as input_data:
        cards = {}
        copied_cards = {}
        total=0
        for line in input_data:
            key = int(line.split(':')[0].split(' ')[-1])
            left, right = line.split(':')[1].split('|')
            winners = set([int(x) for x in left.split(' ') if x.isnumeric()])
            numbers = [int(x) for x in right.split() if x.isnumeric()]
            points = len([x for x in numbers if x in winners])
            cards[key]= {"winners":winners, "numbers": numbers}
            if key not in copied_cards:
                copied_cards[key] = 1
            else:
                copied_cards[key] += 1
            for i in range(1,points+1,1):
                try:
                    copied_cards[key+i] += copied_cards[key]
                except:
                    copied_cards[key+i] = copied_cards[key]
        print(copied_cards)
        print(sum(copied_cards.values()))
part2('input')
