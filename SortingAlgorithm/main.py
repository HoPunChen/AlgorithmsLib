# -*- coding: utf-8 -*-
__author__ = 'HoPun'


from SortingAlgorithm import sorttesthelper

items = []
# generate random numbers and put in items
testhelper = sorttesthelper.SortTestHelper()

# items = testhelper.generateRandomArray(20,2,999)

print ("-"*10 + "original numbers" + "-"*10 )
items = testhelper.generateNearlyOrderedArray(100,10)
print(items)
testhelper.testSort("Selection Sort",items)
testhelper.testSort("Insertion Sort",items)
testhelper.testSort("Bubble Sort",items)
testhelper.testSort("Shell Sort",items)

