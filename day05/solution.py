def read_input(filename):
    with open(filename) as f:
        contents = f.read()
        chunks = contents.split('\n\n')
    return chunks

def read_map(s: str):
    header, *numbers = s.split('\n')
    parsed = [[int(number) for number in line.split(' ')] for line in numbers if line]
    return {header.split(' ')[0]: parsed}

def solve1(filename):
    seeds, *maps = read_input(filename)
    seeds = [int(seed) for seed in seeds.split(' ')[1:]]
    maps = {k: v for m in maps for k, v in read_map(m).items()}
    locations = []
    for seed in seeds:
        soil = find_target(seed, maps['seed-to-soil'])
        fertilizer = find_target(soil, maps['soil-to-fertilizer'])
        water = find_target(fertilizer, maps['fertilizer-to-water'])
        light = find_target(water, maps['water-to-light'])
        temperature = find_target(light, maps['light-to-temperature'])
        humidity = find_target(temperature, maps['temperature-to-humidity'])
        location = find_target(humidity, maps['humidity-to-location'])
        locations.append(location)
    return min(locations)

def read_seed_ranges(seeds: str):
    seed_ranges = [int(seed) for seed in seeds.split(' ')[1:]]
    seeds = set()
    ranges = []
    for start, range_length in zip(seed_ranges[0::2], seed_ranges[1::2]):
        ranges.append((start, start + range_length))
    ranges = sorted(ranges)
    ranges_without_overlaps = [ranges[0]]
    for start, end in ranges:
        previous_end = ranges_without_overlaps[-1][1]
        if start < previous_end:
            if end <= previous_end:
                continue
            else:
                start = previous_end + 1
        ranges_without_overlaps.append((start,end))
    return ranges_without_overlaps

# just bruteforcing
def solve2(filename):
    seeds, *maps = read_input(filename)
    seed_ranges = read_seed_ranges(seeds)
    maps = {k: v for m in maps for k, v in read_map(m).items()}
    smallest = None

    def find_target(x, map_key):
        for destination, source, range_length in maps[map_key]:
            if x >= source and x < source + range_length:
                return destination + x - source
        return x

    for start, end in seed_ranges:
        for seed in range(start, end):
            soil = find_target(seed, 'seed-to-soil')
            fertilizer = find_target(soil, 'soil-to-fertilizer')
            water = find_target(fertilizer, 'fertilizer-to-water')
            light = find_target(water, 'water-to-light')
            temperature = find_target(light, 'light-to-temperature')
            humidity = find_target(temperature, 'temperature-to-humidity')
            location = find_target(humidity, 'humidity-to-location')

            if smallest and location < smallest:
                smallest = location
            elif not smallest:
                smallest = location

    return smallest
