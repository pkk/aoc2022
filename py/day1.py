import functools
import numpy


def read_input(file_name):
    res = []
    acc = 0
    with open(file_name) as f:
        res = []
        for line in f:
            if line == "\n":
                res.append(acc)
                acc = 0
            else:
                acc += int(line)
        res.append(acc)
    return res


def day1():
    arr = read_input("day1.txt")
    day1_1 = functools.reduce(lambda a, b: a if a > b else b, arr)
    print(day1_1)
    print(numpy.sort(arr))
    day1_2 = functools.reduce(lambda a, b: a + b, numpy.sort(arr)[-3:])
    print(day1_2)


if __name__ == "__main__":
    day1()
