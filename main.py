import random
import timeit


def makeit(arr, lower, upper):
    for i in range(lower,upper):
        arr.append(i)
    random.shuffle(arr)

stuffy=[]
makeit(stuffy,1,1001)
print(stuffy)
#stuff=[1,5,8,9,3,2]

def SelctionSort(arr):
    for i in range(len(arr)):
        small=i #find the smallest number in the array, going up from 0
        for j in range(i+1, len(arr)):
            if arr[small]>arr[j]:
                small=j #if the position of the smallest number has a number larger than something else, it isn't the smallest
                #this keeps looping until it has the smallest number left
        arr[i], arr[small]= arr[small], arr[i] #this swaps it
    print(arr)

def InsertionSort(arr):
    for i in range(1, len(arr)):
        small=i
        number=arr[small]
        while arr[small-1] > number and small>0:
            arr[small]#swap here
            number=number-1
    print(arr)

def BubbleSort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
    print(arr)


# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

SelctionSort(stuffy)
InsertionSort(stuffy)
BubbleSort(stuffy)
mergeSort(stuffy)
print(stuffy)