import random

def makeit(arr, lower, upper, amount):
    arr.append(random.sample(range(lower, upper), amount))

stuffy=[]
makeit(stuffy,1,50,10)
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
    return arr

def InsertionSort(arr):
    for i in range(1, len(arr)):
        small=i
        number=arr[small]
        while arr[small-1] > number and small>0:
            arr[small]#swap here
            number=number-1
    return arr

def BubbleSort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]

sortedstuff=SelctionSort(stuffy)
#sortedstuff=InsertionSort(stuff)
sortedstuff=BubbleSort(stuffy)
print(sortedstuff)