import numpy as np

arr = np.array([2,1,4,0,5,6,3])

def bubble(arr):
    while True:
        switch = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
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

def heap():
    #TODO: implement heap sort and quick sort
    pass
    

sorted_arr = merge(arr)
print(sorted_arr)