# -*- coding: utf-8 -*-
__author__ = 'HoPun'

class MergeSort(object):

    def merge(self, left, right):
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    def sort(self, lists):
        # 递归使用归并排序,对arr[l...r]的范围进行排序
        if len(lists) <= 1:
            return lists
        mid = round(len(lists) / 2)
        left = self.sort(lists[:mid])
        right = self.sort(lists[mid:])
        return self.merge(left, right)

