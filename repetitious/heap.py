#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 这个heap从0开始存储数据
# heap的容量为count，然后heap的索引范围为闭区间[0, count-1]
# heap中的索引i的结点的左子结点: 2*i+1, 右子结点：2*i+2, 父结点：(i-1)//2
# 堆排序的前置操作是堆化，堆化要从第一个非叶子结点开始堆化，第一个非叶子结点：count/2 - 1. 因为这个结点的左子结点为count-1, 是堆最后的一
# 索引，如果比这个结点索引大的结点的左右结点索引都会超出堆的索引范围限制
# 实际这里实现的是一个基于大顶堆的堆排序，大顶堆更适合做一个原地的排序操作


def heap_sort(arr):
    n = len(arr)
    build_heap(arr, n)
    # 实际的原地排序
    while n > 1:
        arr[0], arr[n-1] = arr[n-1], arr[0]
        n -= 1
        heapify(arr, 0, n)


def build_heap(arr, n):
    idx = n//2 - 1
    while idx >= 0:
        heapify(arr, idx, n)
        idx -= 1


def heapify(arr, idx, n):
    """从上往下进行堆化"""
    while True:
        # 实际的数据交换放到最后再去做
        max_pos = idx
        if 2*idx+1 < n and arr[2*idx+1] > arr[idx]:
            max_pos = 2*idx+1
        if 2*idx+2 < n and arr[2*idx+2] > arr[max_pos]:
            max_pos = 2*idx+2
        if max_pos == idx:
            # 此时两种可能：1. 叶子结点比本结点都小，无需交换 2. 本结点没有叶子结点
            break
        arr[idx], arr[max_pos] = arr[max_pos], arr[idx]
        # 这个赋值让循环继续下去
        idx = max_pos


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 3]
    heap_sort(arr)
    print(arr)
