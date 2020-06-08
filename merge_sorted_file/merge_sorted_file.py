#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 合并c个已排序的小文件到一个大文件
# 思想类似归并排序里的合并函数，但但文件数较多时，每次文件顶部数据比较得到最小值会比较耗时，如果是基于数组存储这c个元素，则时间复杂度是o(c)
# 这里引入了堆来处理c个文件里取出的c个字符串的大小关系。这样涉及两个操作：
# 1. 从小文件（c个数据中上一个最小的数据的来源文件）中取出新的元素插入小顶堆
# 2. 删除小顶堆堆顶，并将堆顶元素放入新的合并大文件中
# 包的引入问题要解决

import random
from merge_heap import MergeHeap


def generate_sorted_files():
    for i in range(100):
        log_file = "./" + str(random.randint(0, 9)) + ".log"
        with open(log_file, 'a') as f:
            f.write(str(i) + '\n')


def clear_sorted_file():
    for i in range(10):
        log_file = "./" + str(i) + ".log"
        with open(log_file, 'r+') as f:
            f.seek(0)
            f.truncate()


def value_convert(val, stream_num):
    """将val值转换成val-stream_num的格式"""
    return str(val) + '-' + str(stream_num)


def merge_files(destination):
    hp = MergeHeap(10)
    sorted_file_streams = []
    mf = open(destination, 'w+')
    for i in range(10):
        log_file = "./" + str(i) + ".log"
        f = open(log_file, 'r')
        sorted_file_streams.append(f)

    # 初始化用于获取最小值的堆
    for i, s in enumerate(sorted_file_streams):
        s_val = s.readline().strip()
        if s_val:
            h_val = value_convert(s_val, i)
            hp.insert(h_val)

    while not hp.is_empty():
        root_val, root_stream_num = hp.remove_root()
        # 将当前流中最小值写入目标合并文件
        mf.write(str(root_val) + '\n')
        next_val = sorted_file_streams[root_stream_num].readline().strip()
        if next_val:
            hp.insert(value_convert(next_val, root_stream_num))


if __name__ == "__main__":
    # generate_sorted_files()
    # clear_sorted_file()
    # mf = open('./merge_file.log', 'w+')
    # mf.write('9')
    merge_files('./merge_file.log')
    # with open('./5.log', 'r') as f:
    #     # 读取文件时，最后一行的换行符不被统计进去
    #     lines = f.readlines()
    #     print('length: ', len(lines))
    #     for i, v in enumerate(lines):
    #         print(i, v)