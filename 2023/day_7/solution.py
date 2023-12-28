from pathlib import Path
from collections import defaultdict
RANK_MAP ={
    'A':'M',
    'K':'L',
    'Q':'K',
    'T':'J',
    '9':'I',
    '8':'H',
    '7':'G',
    '6':'F',
    '5':'E',
    '4':'D',
    '3':'C',
    '2':'B',
    'J':'A'
}
def rank_hand(hand):
    hand_dict = defaultdict(int)
    secondary = ''.join(RANK_MAP[x] for x in hand)
    wilds = 0
    for card in hand:
        if card == 'J':
            wilds += 1
            continue
        hand_dict[card] += 1
    if hand_dict:
        biggest_card = max(hand_dict, key=hand_dict.get)
        hand_dict[biggest_card] += wilds
    match len(hand_dict):
        case 5: return hand,'A'+ secondary,hand_dict
        case 4: return hand,'B'+ secondary,hand_dict
        case 3: 
            if 2 in hand_dict.values(): return hand,'C'+ secondary,hand_dict
            return hand,'D'+ secondary,hand_dict
        case 2:
            if 2 in hand_dict.values(): return hand,'E'+ secondary,hand_dict
            return hand,'F'+ secondary,hand_dict
        case 1: return hand, 'G' + secondary,hand_dict
        case 0: return hand, 'G' + secondary,hand_dict

def part1(source):
    with open(Path(r'C:\Users\cermit\source\repos\aoc\2023\day_7'+f'\\{source}'),'r') as input_data:
        tot=0
        ranked_hands = []
        for line in input_data:
            hand, points = line.replace('\n','').split(' ')
            ranked_hands.append((*rank_hand(hand),points))
        for i, hand in enumerate(sorted(ranked_hands, key=lambda e:e[1])):
            tot += (i+1)*int(hand[-1])
            print(f'{i+1} {hand}')
        print(tot)

if __name__ == '__main__':
    part1("input")