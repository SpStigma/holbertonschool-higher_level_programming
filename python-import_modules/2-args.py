#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    arguments = len(argv)

    if arguments == 1:
        print("0 arguments.")
    elif arguments == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(arguments - 1))

    for i in range(1, arguments):
        print("{}: {}".format(i, argv[i]))
