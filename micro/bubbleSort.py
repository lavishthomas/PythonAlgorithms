l = [15, 12, 51, 52, 60, 70, 80, 13, 14, 13, 97]
#l= [3,2,1,4,5]
len = len(l)

for i in range(0, len-1): 
    for j in range(i, len-1): 
        if l[i] > l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp 

print(l)

