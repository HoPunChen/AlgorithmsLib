# -*- coding: utf-8 -*-
__author__ = 'HoPun'

class InsertionSort(object):
    # def sort(arr):
    #     length = len(arr)
    #     for i in range(0,length):
    #         for j in range(i,0,-1):
    #             if arr[j] < arr[j-1]:
    #                 arr[j],arr[j-1] = arr[j-1],arr[j]
    #             else:
    #                 break
    #         print("Round ", i + 1, ": ", arr)

    def sort(arr):
        length = len(arr)
        for i in range(0,length):
            tmp = arr[i]
            for j in range(i,0,-1):
                if arr[j-1] > tmp:
                    arr[j] = arr[j-1]
                else:
                    arr[j] = tmp
                    break

            print("Round ", i + 1, ": ", arr)




arr = [2,6,8,5,1,2,3]
InsertionSort.sort(arr)

