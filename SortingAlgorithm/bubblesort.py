# -*- coding: utf-8 -*-
__author__ = 'HoPun'

class BubbleSort():
    def sort(arr):
        length = len(arr)
        while length > 0:
            for i in range(length-1):
                if arr[i] > arr[i + 1]:
                    arr[i] = arr[i] + arr[i + 1]
                    arr[i + 1] = arr[i] - arr[i + 1]
                    arr[i] = arr[i] - arr[i + 1]
            length -= 1

        return arr


if __name__ == '__main__':
    bubbleList = [3, 4, 1, 2, 5, 8, 0]
    BubbleSort.sort(bubbleList)
    print(bubbleList)