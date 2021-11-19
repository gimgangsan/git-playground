import datetime
import random
import copy

exampleList = [x for x in range(1000)]
random.shuffle(exampleList)
def swap(targetList, i, j):
    if i != j:
        firstNumToSwap = targetList[i]
        targetList[i] = targetList[j]
        targetList[j] = firstNumToSwap

def bubbleSort(list_to_sort):
    listLength = len(list_to_sort)
    for loop in range(listLength -1, 0, -1):
        for index in range(loop):
            if list_to_sort[index] > list_to_sort[index + 1]:
                swap(list_to_sort, index, index + 1)

def selectionSort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

#print(exampleList)
#selectionSort(exampleList)
#print(exampleList)

def insertionSort(arr):
    for end in range(1, len(arr)):
        i = end
        while i > 0 and arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1

def recordBubble(targetList):
    startTime = datetime.datetime.now()
    bubbleSort(copy.deepcopy(targetList))
    timeSpent = datetime.timedelta.total_seconds(datetime.datetime.now()
                                                 - startTime)
    return timeSpent

def recordSelection(targetList):
    startTime = datetime.datetime.now()
    selectionSort(copy.deepcopy(targetList))
    timeSpent = datetime.timedelta.total_seconds(datetime.datetime.now()
                                                 - startTime)
    return timeSpent

def recordInsertion(targetList):
    startTime = datetime.datetime.now()
    insertionSort(copy.deepcopy(targetList))
    timeSpent = datetime.timedelta.total_seconds(datetime.datetime.now()
                                                 - startTime)
    return timeSpent

print(recordSelection(exampleList))
print(recordInsertion(exampleList))

def algorithmTesting(loop):
    exampleList = [x for x in range(1000)]
    bubbleTimeSum = 0
    selectionTimeSum = 0
    insertionTimeSum = 0
    for x in range(loop):
        random.shuffle(exampleList)
        bubbleTimeSum += recordBubble(exampleList)
        selectionTimeSum += recordSelection(exampleList)
        insertionTimeSum += recordInsertion(exampleList)
    
    return [bubbleTimeSum / loop,
            selectionTimeSum / loop,
            insertionTimeSum / loop]

#print(algorithmTesting(50))
