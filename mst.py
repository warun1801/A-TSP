import heapq
import random

def prims_mst(graph, path, start):
    pq = []
    total_cost = 0
    # ignore the nodes already in the path of the node
    visited = set(path)
    heapq.heappush(pq, (0, start))
    
    #? to bring start into the mst so that the path back to start node is accounterd for
    if start in visited:
        visited.remove(start)

    while pq:
        # pop the min cost to reach node from the heap
        cost, node = heapq.heappop(pq)
        if node not in visited:
            visited.add(node)
            total_cost += cost
            # no need for cost updation, just let the bad nodes remain in the heap and remove while popping
            # O(log(n^2)) == O(log(n))
            for neighbor, ne_node in graph.graph[node].items():
                if neighbor not in visited:
                    # push the neighbor and cost to reach it
                    heapq.heappush(pq, (ne_node.cost, neighbor))

    # check for if the augmented subgraph is connected or not
    for i in graph.graph.keys():
        if i not in visited:
            # if not connected return infinity to suggest no way to reach the destination
            return float('inf')
            
    return total_cost

    