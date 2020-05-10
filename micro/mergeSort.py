def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    # print(left_arr)
    # print(right_arr)

    left_arr = mergeSort(left_arr)
    right_arr = mergeSort(right_arr)

    sorted_array = []
    i = 0
    j = 0
    k = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            sorted_array.append(left_arr[i])
            i += 1
        else:
            sorted_array.append(right_arr[j])
            j += 1

    if i < len(left_arr):
        for k in range(i, len(left_arr)):
            sorted_array.append(left_arr[k])

    if j < len(right_arr):
        for k in range(j, len(right_arr)):
            sorted_array.append(right_arr[k])

    print(sorted_array)

    return sorted_array


l = [15, 12, 51, 52, 60, 70, 80, 13, 14, 17, 97]
print(len(l))
s = mergeSort(l)
print(len(s))