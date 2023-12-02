
with open(r'aoc\2023\day_2\input','r') as input_data:
    data_struct = {}
    for line in input_data:
        key = int(line.split(' ')[1][:-1])
        dice = {'red':0,'green':0,'blue':0}
        for pull in line[:-1].split(':')[1].split(';'):
            for die in pull.split(','):
                dice[die.split(' ')[2]] = max([dice[die.split(' ')[2]],int(die[1:].split(' ')[0])])
        data_struct[key] = dice
    sum1 = sum([
        k for k, v in data_struct.items() if v['blue'] < 15 and v['green'] < 14 and v['red'] < 13
    ])
    sum2 = sum([
         v['blue'] * v['green'] * v['red'] 
         for k, v in data_struct.items()
    ])

print(sum1)
print(sum2)
