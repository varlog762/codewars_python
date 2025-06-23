from functools import reduce

def grow(arr):
  return reduce(lambda acc, value: acc * value, arr, 1)