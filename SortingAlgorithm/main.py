# -*- coding: utf-8 -*-
__author__ = 'HoPun'


from SortingAlgorithm import sorttesthelper

items = []
# generate random numbers and put in items
testhelper = sorttesthelper.SortTestHelper()

# items = testhelper.generateRandomArray(20,2,999)

print ("-"*10 + "original numbers" + "-"*10 )
items = testhelper.generateNearlyOrderedArray(50,5)
print(items)
testhelper.testSort("Selection Sort",items)
testhelper.testSort("Insertion Sort",items)
testhelper.testSort("Bubble Sort",items)
testhelper.testSort("Shell Sort",items)
testhelper.testSort("Merge Sort",items)
testhelper.testSort("Quick Sort",items)
testhelper.testSort("Quick Sort 3 Way",items)
testhelper.testSort("Heap Sort",items)
testhelper.testSort("Merge Sort Bottom Up",items)