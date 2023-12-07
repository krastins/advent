from functools import reduce, cache
import operator

def calculate_distance(race_time, charge_time):
    distance = 0
    speed = 0
    for t in range(0, race_time):
        if charge_time > 0:
            speed += 1
            charge_time -= 1
        else:
            distance += speed
    return distance

def solve1(filename):
    def read_input(filename):
        with open(filename) as f:
            contents = f.read()
            times, distances = [[int(c) for c in line.split(':')[1].split(' ') if c] for line in contents.split('\n') if line]
        return list(zip(times, distances))

    races = read_input(filename)
    ways = []
    for time, record in races:
        ways.append(len([d for d in [calculate_distance(time, t) for t in range(0, time + 1)] if d > record]))
    return reduce(operator.mul, ways)

def solve2(filename):
    def read_input(filename):
        with open(filename) as f:
            contents = f.read()
            return [int(line.split(':')[1].replace(' ', '')) for line in contents.split('\n') if line]

    time, record = read_input(filename)
    a = -1
    b = time
    c = -record
    d = b**2-4*a*c
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
    x1 = abs(math.floor(x1))
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)
    x2 = abs(math.floor(x2))
    return (x2 - x1)
