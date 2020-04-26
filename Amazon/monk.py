import own_graph 

number_of_testcases = int(input())
#print(number_of_testcases)
for testcase in range(0,number_of_testcases):
    #print ("testcase", testcase)
    new_graph = own_graph.Graph()    
    n_m = input()
    n, m = n_m.split(" ")
    m = int(m)
    n = int(n)
    print("m ", m , " n ", n)
    for edges in range(0, m): 
        edge = input()
        vertix_a, vertix_b = edge.split(" ")
        new_graph.add_vertix(vertix_a)
        new_graph.add_vertix(vertix_b)
        new_graph.add_edge(vertix_a, vertix_b)

    new_graph.printGraph()
    path = new_graph.bfs('1',n)
    print(len(path))    
    print(path)