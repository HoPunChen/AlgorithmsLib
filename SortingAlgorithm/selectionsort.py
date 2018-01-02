# -*- coding: utf-8 -*-
__author__ = 'HoPun'

class SelectionSort(object):
    def sort(arr):
        length = len(arr)
        for i in range(0,length):
            # 寻找[i, length)区间里的最小值的索引
            minIndex = i
            for j in range(i+1,length):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
            # print("Round ", i+1, ": ", arr)
        return arr
