
exampleList = [5,2,6,1,3,4]

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

def selectionSort(list_to_sort):
    listLength = len(list_to_sort)
    
    for i in range(listLength -1):
        smallestNum = list_to_sort[i]
        smallestNumIndex = i
        for j in range(i,listLength):
            if list_to_sort[j] < smallestNum:
                smallestNum = list_to_sort[j]
                smallestNumIndex = j
        swap(list_to_sort, i, smallestNumIndex)
        print(exampleList)

selectionSort(exampleList)
print(exampleList)
def insertionSort(list_to_sort):
    pass
