def read_input(filename):
     with open(filename, 'r') as f:
         return [line for line in f.read().split('\n') if line]

def find_digits(s):
    return [int(c) for c in s if c.isnumeric()]

def solve1(filename):
     lines = read_input(filename)
     parsed = [find_digits(s) for s in lines]
     return sum([l[0] * 10 + l[-1] for l in parsed])

def replace_spelled_digits(s):
     mapping = {
         'one': 1,
         'two': 2,
         'three': 3,
         'four': 4,
         'five': 5,
         'six': 6,
         'seven': 7,
         'eight': 8,
         'nine': 9
     }
     
     first_idx = len(s)
     first = None
     for k, v in mapping.items():
         if k in s and (temp := s.index(k)) >= 0:
             if temp < first_idx:
                 first_idx = temp
                 first = k
     if first:
         first_subs = s.replace(first, str(mapping[first]))
     else:
         first_subs = s
     

     last_idx = 0
     last = None
     for k, v in mapping.items():
         if k in s and (temp := s.rindex(k)) >= 0:
             if temp > last_idx:
                 last_idx = temp
                 last = k
     if last:
         last_subs = s.replace(last, str(mapping[last]))
     else:
         last_subs = s
     return find_digits(first_subs)[0] * 10 + find_digits(last_subs)[-1]

def solve2(filename):
     lines = read_input(filename)
     parsed = [replace_spelled_digits(s) for s in lines]
     return sum(parsed)
