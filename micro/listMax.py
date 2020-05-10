import time

tic = time.perf_counter()
l = [5, 2, 101, 102, 98, 99, 100, 3, 4, 1, 97]
print(l)
l.sort()
l.append(-1)

max_len = 0
cur_len = 0
for i in range(0, len(l) - 1):
    if (l[i] + 1) == l[i + 1]:
        cur_len += 1
    else:
        if max_len < cur_len:
            max_len = cur_len
            cur_len = 0

toc = time.perf_counter()
print(f"Downloaded the tutorial in {toc - tic} seconds")
print(l)
l.pop()
print(max_len + 1)
