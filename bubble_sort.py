def bubbleSort(arr):
    isSorted = False
    ctr = 0
    while not isSorted:
        isSorted = True
        for i in range(len(arr) - 1 - ctr):
            if arr[i] > arr[i + 1]:
                swap(i, i + 1, arr)
                isSorted = False
        ctr += 1
    return arr

def swap(i, j, arr):
    arr[i], arr[j], = arr[j], arr[i]

arr = [34,23,2,9,8,5]
print('Given array is : ')
print(arr)
sorted_arr = bubbleSort(arr)
print('Sorted array is : ')
print(sorted_arr)
