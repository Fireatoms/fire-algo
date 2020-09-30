from collections import deque


def d_to_binary_int(num):
    """
    decimal int to binary
    """
    ans = deque()
    while num:
        ans.appendleft(num % 2)
        num //= 2

    return list(ans)


def d_to_binary_fraction(num, limit):
    ans = []
    count = 0
    while num and count < limit:
        num *= 2
        ans.append(int(num))
        num -= int(num)
        count += 1

    return ans


def d_to_binary(num):
    int_ans = d_to_binary_int(int(num))
    fra_ans = d_to_binary_fraction(num - int(num), 10)
    return ''.join(map(str,int_ans)) + '.' + ''.join(map(str, fra_ans))


if __name__ == "__main__":
    print(d_to_binary(127.125))