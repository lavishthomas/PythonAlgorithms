class Graph:
    def __init__(self, graph={}):
        self.graph = graph

    def add_vertix(self, new_vertice):
        self.graph[new_vertice] = []

    def add_edge(self, vertix_a, vertix_b):
        if vertix_a in self.graph and vertix_b in self.graph:
            self.graph[vertix_a].append(vertix_b)
            self.graph[vertix_b].append(vertix_a)
        else:
            raise Exception("vertix not available")

    def bfs(self, start_node, target_node):

        if start_node in self.graph or target_node in self.graph:
            self.graph[start_node]
        else:
            raise Exception("start node or end not present")

        from collections import deque
        traversal_graph = deque()
        visited_nodes = [start_node]
        new_path = [start_node]
        traversal_graph.appendleft(new_path)

        while(len(traversal_graph)):
            print(" before : ", traversal_graph)
            current_path = traversal_graph.pop()
            current_node = current_path[len(current_path)-1]
            print("current Node : " , current_node, current_path)

            if (current_node == target_node):                
                return current_path
            else:
                for node in self.graph[current_node]:
                    if node not in traversal_graph and node not in visited_nodes:
                        # current_path.append(node)
                        new_path = current_path.copy()
                        new_path.append(node)
                        print(" new path ", new_path)
                        traversal_graph.appendleft(new_path)
                        visited_nodes.append(node)
            print("after :" , traversal_graph)
            print("(-----------------------------)")

            return "path not found"
    
    def dfs(self, start_node, target_node):

        if start_node in self.graph or target_node in self.graph:
            self.graph[start_node]
        else:
            raise Exception("start node or end not present")

        from collections import deque
        traversal_graph = deque()
        visited_nodes = [start_node]
        new_path = [start_node]
        traversal_graph.append(new_path)

        while(len(traversal_graph)):
            print(" before : ", traversal_graph)
            current_path = traversal_graph.pop()
            current_node = current_path[len(current_path)-1]
            print("current Node : " , current_node, current_path)

            if (current_node == target_node):                
                return current_path
            else:
                for node in self.graph[current_node]:
                    if node not in traversal_graph and node not in visited_nodes:
                        # current_path.append(node)
                        new_path = current_path.copy()
                        new_path.append(node)
                        print(" new path ", new_path)
                        traversal_graph.append(new_path)
                        visited_nodes.append(node)
            print("after :" , traversal_graph)
            print("(-----------------------------)")    

    def printGraph(self):
        ###
        print(self.graph)


if __name__ == "__main__":
    new_graph = Graph()
    new_graph.add_vertix("a")
    new_graph.add_vertix("b")
    new_graph.add_vertix("c")
    new_graph.add_vertix("d")
    new_graph.add_vertix("e")
    new_graph.add_vertix("f")
    new_graph.add_vertix("g")

    new_graph.add_edge('a', 'b')
    new_graph.add_edge('a', 'c')

    new_graph.add_edge('b', 'd')
    new_graph.add_edge('b', 'e')

    new_graph.add_edge('c', 'd')
    new_graph.add_edge('c', 'f')

    new_graph.add_edge('d', 'e')
    new_graph.add_edge('e', 'f')
    new_graph.printGraph()

    result = new_graph.bfs('a', 'f')
    print(result)

    result = new_graph.dfs('a', 'f')
    print(result)
