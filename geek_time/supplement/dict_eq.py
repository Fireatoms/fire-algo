# link: https://drmingdrmer.github.io/tech/algorithm/2019/01/09/dict-cmp.html


def dict_eq(a, b):
    # simply: only support dict
    for i in set(a) | set(b):
        if i not in a or i not in b:
            return False

        if not dict_eq(a[i], b[i]):
            return False

    return True


if __name__ == "__main__":
    a = {"a": {"b": {}}}
    b = {"a": {"b": {}}}
    print(dict_eq(a, b))