# nested list flat


def flat(l):
    for k in l:
        if not isinstance(k, (list, tuple)):
            yield k
        else:
            yield from flat(k)


def flat_no_generator(l):
    new_list = []
    flat_r(new_list, l)
    return new_list


def flat_r(new_list, l):
    # loop is the key point
    for k in l:
        if not isinstance(k, (list, tuple)):
            new_list.append(k)
        else:
            flat_r(new_list, k)


if __name__ == "__main__":
    nested_list = [[1, [22, 33, [44]]], [1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # print(list(flat(nested_list)))
    print(flat_no_generator(nested_list))