import time

tic = time.perf_counter()
l = [5, 2, 101, 102, 98, 99, 100, 3, 4, 1, 97]


l.append(-1)
len = len(l)
max_len = 0
cur_len = 0
for i in range(0, len):
    min_pos = i
    for j in range(i, len-1):
        if l[min_pos] > l[j]:
            min_pos = j
    # print(min_pos, " : ", l[min_pos])
    if min_pos != i:
        temp = l[i]
        l[i] = l[min_pos]
        l[min_pos] = temp
    # print(l)
    if (l[i] - 1) == l[i - 1]:
        cur_len += 1
    else:
        if max_len < cur_len:
            max_len = cur_len
            cur_len = 0
toc = time.perf_counter()
print(f"Downloaded the tutorial in {toc - tic} seconds")
#l.pop()
print(max_len + 1)
print(l)