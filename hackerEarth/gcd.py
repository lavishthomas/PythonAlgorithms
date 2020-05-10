'''
Given integer , you need to find four integers , such that they're all factors of  (), and . Your goal is to maximize .

Input format
First line contains an integer , represents the number of test cases.

Each of the next  lines contains an integer  (,  will not exceed 64 bit integer).

Output format
 lines, each line contains the answer () to correspond test case. If there is no way to find such four numbers, output .
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from itertools import combinations_with_replacement
from functools import reduce

def find_factors(num):
    factors = []
    for i in range (1, int(num/2) + 1 ):
        if(num%i == 0):
            factors.append(i)
    return factors        

testcases = input()
for i in range(0,int(testcases)):
    num = int(input())
    factors= find_factors(num)
    #print(factors)
    com = list(combinations_with_replacement(factors,4))
    #print(com)
    sumarray =[]
    for combination in com:
        if sum(combination) == num :       
            product = reduce((lambda x, y: x * y), combination)
            sumarray.append(product)
    if(len(sumarray) == 0 ):
        print ("-1")
    else:
        print (max(sumarray))

