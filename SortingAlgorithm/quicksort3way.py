# -*- coding: utf-8 -*-
__author__ = 'HoPun'

from random import randint

class QuickSort3Way(object):
    def sort(self, lists, left, right):
        # 快速排序
        if left >= right:
            return lists
        if right - left <= 16:
            self.insertionSortForQS(lists, left, right)
        else:
            rand = randint(left, right)  # 优化，随机取标定点，以解决近乎有序的列表
            lists[left], lists[rand] = lists[rand], lists[left]
            key = lists[left]
            low = left
            high = right
            i = low+1
            while left < right:
                while left < right and lists[right] >key:
                    right -= 1
                lists[left] = lists[right]
                while left < right and lists[left] < key:
                    left += 1
                    i += 1
                while left < right and lists[left] == key:
                    i += 1
                lists[right] = lists[left]
            lists[right] = key
            self.sort(lists, low, left - 1)
            self.sort(lists, left + 1, high)
            return lists

    def insertionSortForQS(self, alist, first, last):
        # 专门为辅助快速排序设计的插入排序
        for i in range(first + 1, last + 1):
            currentvalue = alist[i]
            position = i
            while position > first and alist[position - 1] > currentvalue:
                alist[position] = alist[position - 1]
                position = position - 1
            alist[position] = currentvalue
        return alist