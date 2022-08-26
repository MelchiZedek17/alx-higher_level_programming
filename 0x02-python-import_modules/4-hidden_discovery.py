#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    package = dir(hidden_4)
    names = []
    for item in package:
        if item.startswith("__") is False:
            names.append(item)
    names = sorted(names)
    for name in names:
        print(name)
