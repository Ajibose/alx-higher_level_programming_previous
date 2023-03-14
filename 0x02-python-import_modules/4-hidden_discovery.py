#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lists = dir(hidden_4)
    for item in lists:
        if item.startswith('_'):
            continue
        print({:s}.format(item))
