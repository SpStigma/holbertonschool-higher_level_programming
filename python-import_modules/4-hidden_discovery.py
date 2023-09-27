#!usr/bin/python3

import hidden_4

if __name__ == "__main__":
    hidden_module = [attr for attr in dir(hidden_4) if not attr.startswitch('__')]
    print(hidden_module)
    