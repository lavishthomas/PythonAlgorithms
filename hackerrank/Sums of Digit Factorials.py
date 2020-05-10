# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
from functools import lru_cache

digits = list(range(1,10))
factorials = list(map(lambda x:math.factorial(x),digits))

#@lru_cache(maxsize=1048)
def factorial_of_digits(n):
    #print(n)
    n = str(n)
    factorial_sum = 0 
    for i in range (0, len(n)):
        factorial_sum += factorials[int(n[i])-1]
    return factorial_sum
    
def sum_digits(n): 
    n = str(n)
    sum = 0 
    for i in range (0, len(n)):
        sum += int(n[i])
    return sum

def sof(n):
    return sum_digits(factorial_of_digits(n))

def gof(n):
    i = 1
    while(True):        
        g = sof(i)
        if (g == n ):
            #print(g, i)
            return i                    
        else:
            i = i +1

def sum_gof(n):
    sum = 0
    for i in range(1, n+1):
        #print(i)
        sum = sum + sum_digits(gof(i))
    return sum    

testcases = 1
#testcases = int(input())

for testcase in range(0,testcases):
    #line = input()
    line = "20 100000"
    n, m = line.split(" ")
    n = int(n)
    v = sum_gof (n)
    print(v)
