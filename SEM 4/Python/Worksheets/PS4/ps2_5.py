# To normalize against the sum to ensure that the sum is always 1.0 (or as close to as possible).
def normalize(lst):
    return [float(i) / sum(lst) for i in lst]


if __name__ == '__main__':
    lst = [10, 20, 10]
    print(normalize(lst))
