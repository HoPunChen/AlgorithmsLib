# -*- coding: utf-8 -*-
__author__ = 'HoPun'
import math

class ShellSort:
    def sort(arr):
        length = len(arr)
        group = int(length / 2)
        while group > 0:
            for i in range(group,length):
                while i >= group and arr[i-group] > arr[i]:
                    arr[i - group],arr[i] = arr[i], arr[i-group]
                    i -= group
            # print(arr)

            group = int(group/2)
        return arr


# if __name__ == '__main__':
#     # List = [3, 4, 1, 2, 5, 8, 0]
#     # List = [0, 8, 5, 2, 1, 4, 3]
#     List = [49, 38, 65, 97, 76, 13, 27, 49, 55, 4]
#     ShellSort.sort(List)
#     print(List)

