#   Undirected graph
#   >> An Undirected graph is a graph whose edges are bidirectional.
#   >> Undirected graphs have no directions associated with them.
#   >> Undirected graphs are not strongly connected.

#       >> Using Adjacency Matrix to store relationships <<
#       >> Only use Adjacency Matrix for dense graphs / small dataset <<


class UndirectedGraph:
    def __init__(self, vMap ,vCount:int):
        self.vCount = vCount
        self.vMap = vMap # using a vertex map / dict / object with state names
        # Creating a 2D Array / Matrix (Not a prefered way) 
        self.adjacencyMatrix = [[False] * self.vCount for _ in range(self.vCount)]

    # We connect both v (vertex 1) to w (vertex 2) and w to v. 
    def add(self, v, w):
        self.adjacencyMatrix[v][w] = True
        self.adjacencyMatrix[w][v] = True
        return

    def remove(self, v, w):
        self.adjacencyMatrix[v][w] = False
        self.adjacencyMatrix[w][v] = False
        return

    def print(self):
        for i in range(len(self.adjacencyMatrix)):
            print(f"{self.vMap[i]} -> ", end=" ")
            for j in range(len(self.adjacencyMatrix)):
                if (self.adjacencyMatrix[i][j] == True):
                    print(self.vMap[j], end= " ")
                
            # New Line for better formatting
            print()


# Task
# Create a Weighted Undirected Graph