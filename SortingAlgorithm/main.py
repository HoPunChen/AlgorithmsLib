# -*- coding: utf-8 -*-
__author__ = 'HoPun'

import random
import string
from timeit import default_timer as timer
import copy

from SortingAlgorithm import selectionsort,sorttesthelper

print ("-"*10 + "sorting numbers" + "-"*10)
items = []
# generate random numbers and put in items
testhelper = sorttesthelper.SortTestHelper
ssort = selectionsort.SelectionSort
items = testhelper.generateRandomArray(10,2,999)
print ("original items: %r" % items)
copy_items = copy.deepcopy(items)

# calculate execution time for our selection sort method
start = timer()
sorted_items = ssort.sort(items)
end = timer()
duration1 = end - start

# calculate execution time for python built-in sort method
start = timer()
copy_items.sort()
end = timer()
duration2 = end - start

assert sorted_items == copy_items
print ("sorted items: %r" % ssort.sort(items))
print ("Duration: our selection sort method - %fs, python builtin sort - %fs" % (duration1, duration2))


