#   Directed graph
#   >> A Directed graph is a graph whose edges are have only one direction.
#   >> Undirected graphs have directions associated with them.

#       >> Using Adjacency Matrix to store relationships <<
#       >> Only use Adjacency Matrix for dense graphs / small dataset <<


class DirectedGraph:
    def __init__(self, vMap, vCount: int):
        self.vCount = vCount
        self.vMap = vMap  # using a vertex map / dict / object with state names
        # Creating a 2D Array / Matrix (Not a prefered way)
        self.adjacencyMatrix = [[False] * vCount for _ in range(vCount)]

    # We connect only v (vertex 1) to w (vertex 2) cuz its a 1 way connection.
    def add(self, v, w):
        self.adjacencyMatrix[v][w] = True
        return

    def remove(self, v, w):
        self.adjacencyMatrix[v][w] = False
        return

    def print(self):
        for i in range(len(self.adjacencyMatrix)):
            print(f"{self.vMap[i]} -> ", end=" ")
            for j in range(len(self.adjacencyMatrix)):
                if self.adjacencyMatrix[i][j] == True:
                    print(self.vMap[j], end=" ")

            # New Line for better formatting
            print()


# Task
# Create a Weighted Directed Graph
