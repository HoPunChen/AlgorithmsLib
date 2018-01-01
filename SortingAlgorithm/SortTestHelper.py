# -*- coding: utf-8 -*-
__author__ = 'HoPun'
import random

class SortTestHelper:
    # 生成有n个元素的随机数组, 每个元素的随机范围为[rangeL, rangeR]
    def generateRandomArray(length,rangeL, rangeR):
        random_list = []
        for i in range(length):
            random_list.append(random.randint(rangeL, rangeR))
        return random_list

    # 打印arr数组的所有内容
    def printArray(arr):
        for num in arr:
            print(num)
