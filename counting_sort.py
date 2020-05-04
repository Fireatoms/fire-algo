# 计数排序


def counting_sort(arr):
    am = max(arr)
    ln = len(arr)
    # 要写你才会发现这里要申请的是max+1大小的数组，因为我们需要的是索引区间为0-max，自然容量是max+1
    # 初始化
    ac = [0] * (am+1)
    for v in arr:
        ac[v] += 1
    # 求聚合值
    for i in range(1, len(ac)):
        ac[i] = ac[i] + ac[i-1]

    # 故意不使用python的reverse函数，用索引倒序遍历通用性更好
    tmp = [0] * ln
    for i in range(ln-1, -1, -1):
        index = ac[arr[i]] - 1
        tmp[index] = arr[i]
        ac[arr[i]] -= 1

    for i in range(ln):
        arr[i] = tmp[i]


if __name__ == '__main__':
    arr = [1, 2, 3, 2, 4, 5, 5, 5, 6]
    counting_sort(arr)
    print(arr)