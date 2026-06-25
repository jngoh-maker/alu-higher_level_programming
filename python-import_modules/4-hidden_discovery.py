#!/usr/bin/python3

if __name__ == "__main__":
    hidden_4 = __import__('hidden_4')

    names = dir(hidden_4)

    for name in sorted(names):
        if name[:2] != "__":
            print(name)
