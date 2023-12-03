from collections import defaultdict
from functools import reduce

def read_input(filename):
    with open(filename) as f:
        contents = f.read()
        lines = contents.split('\n')
        return [[{kv[1]: int(kv[0]) for pair in c.split(', ') if (kv := pair.split(' '))} for c in line.split(': ')[1].split('; ')] for line in lines if line]

def solve1(filename, red=12, green=13, blue=14):
    games = read_input(filename)

    res = []
    for game in games:
        maximums = defaultdict(int)
        for d in game:
            for k, v in d.items():
                maximums[k] = max(maximums[k], v)
        res.append(maximums)
    
    ids = []
    for i, maximums in enumerate(res):
        if maximums.get('red') <= red and maximums.get('green') <= green and maximums.get('blue') <= blue:
            ids.append(i + 1)
    return sum(ids)

def solve2(filename):
    games = read_input(filename)

    res = []
    for game in games:
        maximums = defaultdict(int)
        for d in game:
            for k, v in d.items():
                maximums[k] = max(maximums[k], v)
        res.append(maximums)
    
    return sum([reduce(lambda x, y: x*y, game.values()) for game in res])
