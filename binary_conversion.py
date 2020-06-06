# 1. 十进制整数转换二进制，正负均支持
# 2. 十进制小数转换二进制，正负均支持


def decimal_integer_to_binary(num):
    symbol = ''
    binary_list = []
    if num < 0:
        symbol = '-'
        num = -num

    while num > 0:
        binary_list.append(num % 2)
        num //= 2

    binary_list.reverse()
    binary_str = ''.join(map(str, binary_list))
    print(symbol + binary_str)


def decimals_to_binary(num, max_deep):
    symbol = ''
    binary_list = []
    if num < 0:
        symbol = '-'
        num = -num

    while max_deep > 0:
        # 比如max_deep为2，代表只需要计算到小数点后两位
        num *= 2
        if num == 1:
            binary_list.append(1)
            break
        elif num > 1:
            binary_list.append(1)
            num -= 1
        else:
            binary_list.append(0)
        max_deep -= 1

    binary_str = ''.join(map(str, binary_list))
    print(symbol + '.' + binary_str)


if __name__ == "__main__":
    decimal_integer_to_binary(-4)
    decimals_to_binary(0.875, 7)