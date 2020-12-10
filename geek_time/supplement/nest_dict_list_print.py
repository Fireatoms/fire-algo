#!/usr/bin/env python


def print_nested_dict_list(l, layer=-1):
    if isinstance(l, list):
        print("[ ", end="")
        for i in l:
            print_nested_dict_list(i, layer+1)
            print(",", end="")
        print(" ]", end="")
    elif isinstance(l, dict):
        layer += 1
        print("{ ", end="")
        for k, v in l.items():
            print("{}: ".format(k), end="")
            print_nested_dict_list(v, layer)
        print(" }", end="")
    else:
        print("{}".format(l), end="")


if __name__ == "__main__":
    l = [
        1,
        {
            "fire": "man",
            "atom": "this"
        },
        [
            {"here": 1},
            {"there": 2}
        ]
    ]

    print_nested_dict_list(l)