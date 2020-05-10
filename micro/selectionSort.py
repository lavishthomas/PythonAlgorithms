l = [5, 2, 101, 102, 98, 99, 100, 3, 4, 1, 97]
#l= [3,2,1,4,5]
len = len(l)

for i in range(0, len): 
    min_pos = i   
    for j in range(i, len): 
        if l[min_pos] > l[j]:
            min_pos = j

    print(min_pos, " : ", l[min_pos])    
    if min_pos != i:
        temp = l[i]
        l[i] = l[min_pos]
        l[min_pos] = temp
    print(l)

print(l)

