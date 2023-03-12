#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    length -= 1

    if length == 0:
        print(f"{length} arguments.")
    elif length == 1:
        print(f"{length} argument:")
    elif length > 1:
        print(f"{length} arguments.")

    for i in range(1, length + 1):
        print("{}: {}".format(i, sys.argv[i]))
