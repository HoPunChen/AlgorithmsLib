# -*- coding: utf-8 -*-
__author__ = 'HoPun'

class MergeSortBU():
    def sort(alist):
        n = len(alist)
        size = 1
        while size < n:
            blist = alist[:]
            i = 0
            while i + size < n:
                if alist[i + size - 1] < alist[i + size]:  # 优化1。优化2方案放弃。
                    i = i + size + size
                    continue
                a, b, c = i, i + size, i
                while a < i + size and b < min(i + size + size, n):
                    if blist[a] <= blist[b]:
                        alist[c] = blist[a]
                        a += 1
                    else:
                        alist[c] = blist[b]
                        b += 1
                    c += 1
                while a < i + size:
                    alist[c] = blist[a]
                    a += 1
                    c += 1
                while b < min(i + size + size, n):
                    alist[c] = blist[b]
                    b += 1
                    c += 1
                i = i + size + size
            size = size + size
        return alist