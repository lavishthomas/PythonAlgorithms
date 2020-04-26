def some(x):
    return (lambda y: x+y)
each = some (3)
print (each(2))