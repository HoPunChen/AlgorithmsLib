# -*- coding: utf-8 -*-
__author__ = 'HoPun'
import random
from timeit import default_timer as timer
import copy
from SortingAlgorithm import selectionsort,insertionsort,bubblesort,shellsort,mergesort,quicksort

class SortTestHelper(object):
    # 生成有n个元素的随机数组, 每个元素的随机范围为[rangeL, rangeR]
    def generateRandomArray(self, length, rangeL, rangeR):
        random_list = []
        for i in range(length):
            random_list.append(random.randint(rangeL, rangeR))
        return random_list

    # 打印arr数组的所有内容
    def printArray(self, arr):
        for num in arr:
            print(num)

    def isSorted(self, arr):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True

    # 生成一个完全有序的数组
    def generateOrderedArray(self, length):
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
    def generateNearlyOrderedArray(self, length, swapTimes):
        ordered_list = []
        for i in range(length):
            ordered_list.append(i)

        for i in range(swapTimes):
            a = random.randint(0,length-1)
            b = random.randint(0,length-1)
            ordered_list[a],ordered_list[b] = ordered_list[b],ordered_list[a]

        return ordered_list

    def testSort(self, str, arr):
        if str == "Selection Sort":
            copy_items = copy.deepcopy(arr)
            print("-" * 10 + str + "-" * 10)
            ssort = selectionsort.SelectionSort
            start = timer()
            sorted_items = ssort.sort(copy_items)
            end = timer()
            duration = end - start
            print(sorted_items)
            if self.isSorted(sorted_items):
                print("python selection sort - %fs" % duration)

        if str == "Insertion Sort":
            copy_items = copy.deepcopy(arr)
            print( "-"*10 + str  + "-"*10 )
            isort = insertionsort.InsertionSort
            start = timer()
            sorted_items = isort.sort(copy_items)
            end = timer()
            duration = end - start
            print(sorted_items)
            if self.isSorted(sorted_items):
                print("python insertion sort - %fs" % duration)

        if str == "Bubble Sort":
            copy_items = copy.deepcopy(arr)
            print( "-"*10 + str  + "-"*10 )
            bsort = bubblesort.BubbleSort
            start = timer()
            sorted_items = bsort.sort(copy_items)
            end = timer()
            duration = end - start
            print(sorted_items)
            if self.isSorted(sorted_items):
                print("python bubble sort - %fs" % duration)

        if str == "Shell Sort":
            copy_items = copy.deepcopy(arr)
            print( "-"*10 + str  + "-"*10 )
            shsort = shellsort.ShellSort
            start = timer()
            sorted_items = shsort.sort(copy_items)
            end = timer()
            duration = end - start
            print(sorted_items)
            if self.isSorted(sorted_items):
                print("python shell sort - %fs" % duration)

        if str == "Merge Sort":
            copy_items = copy.deepcopy(arr)
            print("-" * 10 + str + "-" * 10)
            msort = mergesort.MergeSort()
            start = timer()
            sorted_items = msort.sort(copy_items)
            end = timer()
            duration = end - start
            print(sorted_items)
            if self.isSorted(sorted_items):
                print("python merge sort - %fs" % duration)

        if str == "Quick Sort":
            copy_items = copy.deepcopy(arr)
            print("-" * 10 + str + "-" * 10)
            qsort = quicksort.QuickSort()
            length = len(copy_items)
            start = timer()
            sorted_items = qsort.sort(copy_items, 0, length-1)
            end = timer()
            duration = end - start
            print(sorted_items)
            if self.isSorted(sorted_items):
                print("python quick sort - %fs" % duration)






