# -*- coding: utf-8 -*-
__author__ = 'HoPun'

from timeit import default_timer as timer
import copy

from SortingAlgorithm import selectionsort,sorttesthelper,insertionsort

print ("-"*10 + "sorting numbers" + "-"*10)
items = []
# generate random numbers and put in items
testhelper = sorttesthelper.SortTestHelper
ssort = selectionsort.SelectionSort
isort = insertionsort.InsertionSort

items = testhelper.generateRandomArray(20,2,999)
print ("original items: %r" % items)
copy_items = copy.deepcopy(items)
copy_items1 = copy.deepcopy(items)

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

# calculate execution time for our insertion sort method
start = timer()
sorted_items1 = isort.sort(copy_items1)
end = timer()
duration3 = end - start

assert sorted_items == copy_items
print ("sorted items: %r" % ssort.sort(items))
print ("Duration: our selection sort method - %fs, python builtin sort - %fs, python insertion sort - %fs" % (duration1, duration2, duration3))


