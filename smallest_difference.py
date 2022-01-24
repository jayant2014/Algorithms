# Smallest difference between two numbers from a pair of non-empty arrays

def smallest_difference(array1, array2):
    array1.sort()
    array2.sort()
    idx1 = 0
    idx2 = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []

    while idx1 < len(array1) and idx2 < len(array2):
        first = array1[idx1]
        second = array2[idx2]
        if first < second:
            current = second - first
            idx1 += 1
        elif first > second:
            current = first - second
            idx2 += 1
        else:
            return [first, second]

        if smallest > current:
            smallest = current
            difference_pair = [first, second]
	
    return difference_pair

array1 = [-1, 5, 7, 20, 29, 3]
array2 = [15, 67, 29, 17, 35, 12]

difference_pair = smallest_difference(array1, array2)
print(difference_pair) 

