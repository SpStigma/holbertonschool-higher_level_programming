#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    arguments = len(argv)
    sum = 0
    for i in range(1, arguments):
        sum += int(argv[i])
    print("{}".format(sum))
