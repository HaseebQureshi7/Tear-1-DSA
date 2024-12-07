#   Directed graph
#   >> A Directed graph is a graph whose edges are have only one direction.
#   >> Undirected graphs have directions associated with them.

#       >> Using Adjacency List to store relationships <<
#       >> Use Adjacency List for large dataset <<

from collections import defaultdict


class DirectedGraphAL:
    def __init__(self, vMap, vCount: int):
        self.vCount = vCount
        self.vMap = vMap  # using a vertex map / dict / object with item names
        # Creating a Dictionary with Arrays (prefered way)
        self.adjacencyList = defaultdict(list)

    def add(self, v, w):
        self.adjacencyList[v].append(w)

    def remove(self, v, w):
        self.adjacencyList[v].remove(w)

    def print(self):
        al = self.adjacencyList

        for i in range(len(al)):
            print(f"{self.vMap[i]} -> ", end=" ")
            for j in range(len(al[i])):
                print(self.vMap[al[i][j]], end=" ")

            print()


# Task
# Create a Weighted Directed Graph
