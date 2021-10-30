class Node:
    def __init__(self, data, cost):
        self.path = []      # will store the path upto (but not including) the city
        self.data = data    # will store the city to visit
        self.cost = cost    # will store the cost to visit the city

    # to print the node
    def __str__(self):
        return f"{self.data, self.cost, self.path}"

    # comparator functions
    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        if other == None:
            return False
        return self.cost == other.cost and self.data == other.data and self.path == other.path