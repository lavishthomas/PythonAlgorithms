'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
input_n_m_k = input()
n, m, k = input_n_m_k.split(" ")

m=int(m)

graph = {}

for edge in range(0, m):
     edge = input()
     nodeA,nodeB = edge.split(" ")
     print(nodeA, " : ",nodeB)
     
     if nodeA in graph:
          graph[nodeA].append(nodeB)
     else:
          graph[nodeA] = [nodeB]

     if nodeB in graph:
          graph[nodeB].append(nodeA)
     else:
          graph[nodeB] = [nodeA]     
     

print (graph)
print(n, " " , m , " ", k , " " )