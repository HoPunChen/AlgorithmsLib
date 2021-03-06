# -*- coding: utf-8 -*-
__author__ = 'HoPun'

class HeapSort():
    def adjust_heap(self, lists, i, size):
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        max = i
        if i < size / 2:
            if lchild < size and lists[lchild] > lists[max]:
                max = lchild
            if rchild < size and lists[rchild] > lists[max]:
                max = rchild
            if max != i:
                lists[max], lists[i] = lists[i], lists[max]
                self.adjust_heap(lists, max, size)

    def build_heap(self, lists, size):
        for i in range(0, round(size / 2))[::-1]:
            self.adjust_heap(lists, i, size)

    def sort(self, lists):
        size = len(lists)
        self.build_heap(lists, size)
        for i in range(0, size)[::-1]:
            lists[0], lists[i] = lists[i], lists[0]
            self.adjust_heap(lists, 0, i)
        return lists