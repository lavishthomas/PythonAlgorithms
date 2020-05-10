def quickSort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    mid = len(arr) // 2
    print(arr)
    print(arr[mid])
    pivot = arr[mid]
    
    left_arr = []
    right_arr = []

    for ele in arr:
        if ele < pivot:
            left_arr.append(ele)
        elif ele > pivot:
            right_arr.append(ele)    

    sorted_array = quickSort(left_arr)
    sorted_array.append(pivot)        
    sorted_array.extend(quickSort(right_arr))

    return sorted_array

l = [15, 12, 51, 52, 13, 14, 17, 97 , 60, 70, 80, 100]
#l = [ 3,2,1]
#print(len(l))
#print(l)
s = quickSort(l)

#print(len(s))
print (s)

