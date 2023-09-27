#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    hidden_module = dir(hidden_4)
    for module in hidden_module:
        if not module.startswith('__'):
            print("{}".format(module))
