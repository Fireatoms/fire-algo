# 插入排序
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        value = arr[i]
        # 像这样需要在循环外部用到循环的索引的，不要使用range
        # for j in range(i-1, -1, -1):
        #     if arr[j] > value:
        #         # 已排序区间内数据大于要插入数据时要进行数据搬移
        #         arr[j+1] = arr[j]
        #     else:
        #         break
        j = i - 1
        while j >= 0:
            if arr[j] > value:
                arr[j+1] = arr[j]
                j -= 1
            else:
                break
            # j -= 1

        # 好好感受下这个插入，每次写都觉得很巧妙。
        arr[j+1] = value


if __name__ == "__main__":
    arr = [5, 4, 2, 3, 1]
    insertion_sort(arr)
    print(arr)
