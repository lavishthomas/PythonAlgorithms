'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

graphes = []
number_of_testcases = int(input())
print(number_of_testcases)
for testcase in range(0, number_of_testcases):
    print("testcase", testcase)
    graphes.append({})
    n_m = input()
    n, m = n_m.split(" ")
    m = int(m)
    for edges in range(0, m):
        edge = input()
        vertix_a, vertix_b = edge.split(" ")
        if vertix_a in graphes[testcase]:
            graphes[testcase][vertix_a].append(vertix_b)
        else:
            graphes[testcase][vertix_a] = [vertix_b]

print(graphes)


