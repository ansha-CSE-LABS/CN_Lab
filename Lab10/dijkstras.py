class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def print_solution(self, dist): 
        print("Vertex \tDistance from Source")
        for node in range(self.V): 
            print(node, "\t", dist[node])
  

    def min_distance(self, dist, sptSet): 
        min = 9999
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
    
    def add_edge(self, src, dest, weight):
        self.graph[src][dest] = self.graph[dest][src] = weight

    def dijkstra(self, src): 
  
        dist = [9999] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
            u = self.min_distance(dist, sptSet) 
            sptSet[u] = True
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v] 
  
        self.print_solution(dist)
g = Graph(int(input("Enter number of nodes in the topology: ")))
e = int(input("Enter number of edges: "))

for i in range(e):
    src, dest, cost = [int(_) for _ in input("Enter [SRC] [DEST] [WEIGHT]: ").split(' ')]
    g.add_edge(src, dest, cost)

src = int(input("Enter [SRC] to find costs: "))
g.dijkstra(src)

# Enter number of nodes in the topology: 5
# Enter number of edges: 6
# Enter [SRC] [DEST] [WEIGHT]: 0 1 2
# Enter [SRC] [DEST] [WEIGHT]: 0 2 1
# Enter [SRC] [DEST] [WEIGHT]: 0 3 4
# Enter [SRC] [DEST] [WEIGHT]: 1 4 3
# Enter [SRC] [DEST] [WEIGHT]: 2 4 1
# Enter [SRC] [DEST] [WEIGHT]: 3 4 8
# Enter [SRC] to find costs: 0

# Vertex 	Distance from Source
# 0 	 0
# 1 	 2
# 2 	 1
# 3 	 4
# 4 	 2
