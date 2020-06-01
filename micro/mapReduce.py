def multiply(x):
    return x * x

def add(x):
    return x + x

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))
print(squared)

items = [1, 2, 3, 4, 5]
filtered = list(filter(lambda x: x > 2, items))
print(filtered)
from functools import reduce
product = reduce((lambda x, y: x * y), items)
print(product)

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]

