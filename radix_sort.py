# 基数排序
# 输入是字符串数组，简化起见，人为保证所有的字符串等长。并且位数越靠前权重越高
# 使用计数排序来完成每一位的排序


def counting_sort(arr, index):
    """计数排序这里做一个小小的变种：
    传入当前要比较的位的索引
    """
    # 单个位上的范围是[0-9]
    ln = len(arr)
    ar = 9
    ac = [0] * (ar+1)
    for v in arr:
        ac[int(v[index])] += 1

    # 计数求和
    for i in range(1, len(ac)):
        ac[i] = ac[i-1] + ac[i]

    tmp = [None] * ln
    for i in range(ln-1, -1, -1):
        val = int(arr[i][index])
        new_index = ac[val] - 1
        tmp[new_index] = arr[i]
        ac[val] -= 1

    for i in range(ln):
        arr[i] = tmp[i]


def radix_sort(arr):
    k = len(arr[0])
    for i in range(k-1, -1, -1):
        counting_sort(arr, i)


if __name__ == '__main__':
    arr = ['134', '345', '145']
    radix_sort(arr)
    print(arr)