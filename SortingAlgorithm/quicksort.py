# -*- coding: utf-8 -*-
__author__ = 'HoPun'

class QuickSort(object):
    def sort(self, lists, left, right):
        # 快速排序
        if left >= right:
            return lists
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
