from functools import cache, reduce
from operator import and_
from typing import List, Set

def read_input(filename) -> List[List[Set[str]]]:
    with open(filename) as f:
        contents = f.read()
        lines = contents.split('\n')
        return [
            [{n for n in c.split(' ') if n}
             for c in line.split(': ')[1].split(' | ')]
             for line in lines if line
        ]

def solve1(filename):
    cards = read_input(filename)
    return sum(pow(2, count - 1) for n in cards if (count := len(reduce(and_, n))))

def count_matching(n: List[Set[str]]):
    return len(reduce(and_, n))

def solve2(filename):
    cards = read_input(filename)

    @cache
    def play_round(position=0):
        res = 1
        if count := count_matching(cards[position]):
            for i in range(position + 1, position + count + 1):
                res += play_round(i)
        return res

    return sum(play_round(i) for i in range(0, len(cards)))
