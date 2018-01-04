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

    def isSorted(arr):
        for i in range(len(arr)):
            if arr[i] > arr[i+1]:
                return False
        return True

    # 生成一个完全有序的数组
    def generateOrderedArray(length):
        ordered_list = []
        for i in range(length):
            ordered_list.append(i)
        return ordered_list

    # 生成一个近乎有序的数组
    # 首先生成一个含有[0...n - 1]
    # 的完全有序数组, 之后随机交换swapTimes对数据
    # swapTimes定义了数组的无序程度:
    # swapTimes == 0
    # 时, 数组完全有序
    # swapTimes
    # 越大, 数组越趋向于无序
    def generateNearlyOrderedArray(length, swapTimes):
        ordered_list = []
        for i in range(length):
            ordered_list.append(i)

        for i in range(swapTimes):
            a = random.randint(0,length-1)
            b = random.randint(0,length-1)
            ordered_list[a],ordered_list[b] = ordered_list[b],ordered_list[a]

        return ordered_list





