with open('day2.txt', 'r') as f:
    day2_input = f.read().split('\n')

WIN = 6
DRAW = 3
LOSS = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

input_map = {
    'A X': DRAW + ROCK,
    'A Y': WIN + PAPER,
    'A Z': LOSS + SCISSORS,
    'B X': LOSS + ROCK,
    'B Y': DRAW + PAPER,
    'B Z': WIN + SCISSORS,
    'C X': WIN + ROCK,
    'C Y': LOSS + PAPER,
    'C Z': DRAW + SCISSORS,
}

day2_1 = sum([input_map.get(turn, 0) for turn in day2_input])
print(day2_1)

input_map2 = {
    'A X': LOSS + SCISSORS,
    'A Y': DRAW + ROCK,
    'A Z': WIN + PAPER,
    'B X': LOSS + ROCK,
    'B Y': DRAW + PAPER,
    'B Z': WIN + SCISSORS,
    'C X': LOSS + PAPER,
    'C Y': DRAW + SCISSORS,
    'C Z': WIN + ROCK,
}

day2_2 = sum([input_map2.get(turn, 0) for turn in day2_input])
print(day2_2)