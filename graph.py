from collections import defaultdict
from node import Node

class Graph:
    def __init__(self):
        self.graph = defaultdict(lambda: defaultdict(lambda: None))
    
    def add_edge(self, u, v, w):
        self.graph[u][v] = Node(v, w)
        self.graph[v][u] = Node(u, w)

    def __str__(self):
        s = ""
        for i in self.graph.keys():
            s += str(i) + ": "
            for j in self.graph[i].keys():
                s += str(j) + " "
            s += "\n"
        return s

    def make_graph(self, path):
        with open(path) as f:
            for line in f:
                print(line.strip())
                u, v, w = line.strip().split(",")
                self.add_edge(u, v, float(w))