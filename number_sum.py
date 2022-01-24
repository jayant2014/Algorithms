def three_number_sum(array, target):
    array.sort()
    triplets = []
    for i in range(len(array)-2):
        left = i+1
        right = len(array)-1
        while left < right:
            sum = array[i] + array[left] + array[right]
            if sum == target:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1
    return triplets

array = [3, 4, 2, 10, 0, -8, 9]
target = 5

triplets = three_number_sum(array, target)
print(triplets)
