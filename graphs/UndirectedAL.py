#   Undirected graph
#   >> An Undirected graph is a graph whose edges are bidirectional.
#   >> Undirected graphs have no directions associated with them.
#   >> Undirected graphs are not strongly connected.

#       >> Using Adjacency List to store relationships <<
#       >> Use Adjacency List for large dataset <<

from collections import defaultdict


class UndirectedGraphAL:
    def __init__(self, vMap, vCount: int):
        self.vCount = vCount
        self.vMap = vMap  # using a vertex map / dict / object with item names
        # Creating a Dictionary with Arrays (prefered way)
        self.adjacencyList = defaultdict(list)

    def add(self, v, w):
        self.adjacencyList[v].append(w)
        self.adjacencyList[w].append(v)

    def remove(self, v, w):
        self.adjacencyList[v].remove(w)
        self.adjacencyList[w].remove(v)

    def print(self):
        al = self.adjacencyList

        for i in range(len(al)):
            print(f"{self.vMap[i]} -> ", end=" ")
            for j in range(len(al[i])):
                print(self.vMap[al[i][j]], end=" ")

            print()


# Task
# Create a Weighted Undirected AL Graph
