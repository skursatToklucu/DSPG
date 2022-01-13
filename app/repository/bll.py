import itertools
import json
from itertools import combinations


def n_length_combo(arr, n):
    return list(map(''.join, itertools.product(arr, repeat=n)))


tripletCombinations = n_length_combo('RLrl', 3)
tripletData = []


def create_all_triplets():
    item = {}
    x = 0
    for triplet in tripletCombinations:
        x = x + 1
        item = {'id': x, 'pattern': triplet}
        print(item)
    return json.dumps(tripletData.append(item))
