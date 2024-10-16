import numpy as np

def bubble(arr):
    while True:
        switch = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                switch += 1
        if switch == 0:
            return arr

def selection(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

def merge(arr):
    if(len(arr) == 2):
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    elif(len(arr) == 1):
        return arr
    else:
        mid = len(arr) // 2
        sub_arrays0 = merge(arr[:mid])
        sub_arrays1 = merge(arr[mid:])

        sorted = np.array([])
        min0 = min1 = 0
        while min0 <= len(sub_arrays0) - 1 and min1 <= len(sub_arrays1) - 1:
            if sub_arrays0[min0] < sub_arrays1[min1]:
                sorted = np.append(sorted, sub_arrays0[min0])
                min0 += 1
            else:
                sorted = np.append(sorted, sub_arrays1[min1])
                min1 += 1
        
        if min0 == len(sub_arrays0):
            sorted = np.append(sorted, sub_arrays1[(min1):])
        elif min1 == len(sub_arrays1):
            sorted = np.append(sorted, sub_arrays0[(min0):])
            
        return sorted

def quick(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)-1]
    
    i = 0
    j = len(arr)-2

    while i < j:
        if arr[i] > pivot:
            while arr[j] > pivot and j > i:
                j -= 1
            if arr[j] < pivot:
                arr[i] ,arr[j] = arr[j], arr[i]
        else:
            i += 1
    if arr[i] > pivot:
        arr[i], arr[len(arr)-1] = arr[len(arr)-1], arr[i]
    
    left = quick(arr[:i])
    right = quick(arr[i+1:])
    
    return np.concatenate((left, [arr[i]], right))

def heap():
    #TODO: implement heap sort and quick sort
    # 1 create a heap from array
    # 2 create a max heap and apply the changes in the heap to the array
    # 3 swap the first element with the last element and remove the last node in heap
    pass

arr = np.array([2,1,4,0,5,6,3])
sorted_arr = quick(arr)
print(sorted_arr)