#!/usr/bin/env python


class Solution:
    def pirnt_nest_struct(self, entity):
        if isinstance(entity, list):
            print("[", end="")
            for e in entity:
                self.pirnt_nest_struct(e)
                print(", ", end="")
            print("]", end="")
        elif isinstance(entity, dict):
            print("{", end="")
            for k, v in entity.items():
                print("{}: ".format(k), end="")
                self.pirnt_nest_struct(v)
                print(",", end="")
            print("}", end="")
        else:
            print(entity, end="")


if __name__ == "__main__":
    sl = Solution()
    nested_stuct = {
        "fire": "man",
        "yuan": [1, 2, 3],
        "dong": {
            "fang": [4, 5, 6]
        }
    }
    sl.pirnt_nest_struct(nested_stuct)