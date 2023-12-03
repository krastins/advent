import re
import numpy as np
from scipy import ndimage

def read_input(filename):
    return np.genfromtxt(filename, dtype='|S1',  delimiter=1, comments=None)

def is_symbol(char):
    if isinstance(char, bytes):
        char = char.decode()
    return not bool(re.match(r"\d|\.", char))

def solve1(filename):
    a = read_input(filename)
    window = ndimage.generate_binary_structure(2, 2)
    symbol_mask = np.stack(np.vectorize(is_symbol)(a)).astype(int)
    symbol_lookaround_mask = ndimage.binary_dilation(symbol_mask, structure=window).astype(symbol_mask.dtype)
    number_mask = np.stack(np.vectorize(lambda s: s.decode().isnumeric())(a)).astype(int)

    number_labels = ndimage.label(number_mask)[0]
    found_labels = set(number_labels[(number_labels * symbol_lookaround_mask).astype(bool)])

    numbers = []
    for label in found_labels:
        mask = number_labels == label
        numbers.append(int(''.join(i.decode() for i in a[mask])))
    return sum(numbers)

def solve2(filename):
    a = read_input(filename)

    number_mask = np.stack(np.vectorize(lambda s: s.decode().isnumeric())(a)).astype(int)
    number_labels = ndimage.label(number_mask)[0]

    found_labels = []
    for x, y in zip(*np.where(a == b'*')):
        labels = set(number_labels[x-1:x+2,y-1:y+2].flatten())
        labels.remove(0)
        if len(labels) == 2:
            found_labels.append(labels)
    
    gear_ratios = []
    for (n1_label, n2_label) in found_labels:
        n1 = int(''.join(i.decode() for i in a[number_labels == n1_label]))
        n2 = int(''.join(i.decode() for i in a[number_labels == n2_label]))
        gear_ratio = n1 * n2
        res.append(gear_ratio)

    return sum(gear_ratios)
