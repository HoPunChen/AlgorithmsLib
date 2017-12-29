# -*- coding: utf-8 -*-
__author__ = 'HoPun'

class SelectionSort:
    def __init__(self):
        pass

    def sort(arr):
        length = len(arr)
        for i in range(0,length):
            # 寻找[i, length)区间里的最小值的索引
            minIndex = i
            for j in range(i+1,length):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
            print("Round ", i+1, ": ", arr)
        return arr


arr = [6,3,1,2,4,8]
arr2 = ["a","f","s","q","b","z","w"]
print("Selected Sort: ")
print(SelectionSort.sort(arr2))
arr.sort()
print(arr)
arr2.sort()
print(arr2)