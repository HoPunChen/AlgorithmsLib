# -*- coding: utf-8 -*-
__author__ = 'HoPun'
from SortingAlgorithm import insertionsort
from random import randint

class QuickSort(object):
    def sort(self, lists, left, right):
        # 快速排序
        if left >= right:
            return lists
        # if right - left <= 16:
        #     return insertionsort.InsertionSort.sort(lists)
        rand = randint(left, right)  # 优化，随机取标定点，以解决近乎有序的列表
        lists[left], lists[rand] = lists[rand], lists[left]
        key = lists[left]
        low = left
        high = right
        while left < right:
            while left < right and lists[right] >= key:
                right -= 1
            lists[left] = lists[right]
            while left < right and lists[left] <= key:
                left += 1
            lists[right] = lists[left]
        lists[right] = key
        self.sort(lists, low, left - 1)
        self.sort(lists, left + 1, high)
        return lists
