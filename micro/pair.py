
def findPairs(l,target):
    hash = set()
    for ele in l:
        if target < ele:
            continue
        else:
            compliment = target - ele
            if compliment in hash:
                print(ele, compliment)
                return
            else:
                hash.add(ele)
        print(hash)        
    print("No valid")
    return 
    

l = [4, 5, 6, 7, 8, 9, 2, 3]
target = 5
findPairs(l, target)

l = [2,2]
target = 4
findPairs(l, target)

l = [2]
target = 4
findPairs(l, target)

l = [12,2,3,4,5,6,0,22,4,5]
target = 4
findPairs(l, target)