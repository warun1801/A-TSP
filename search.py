from node import Node
from graph import Graph
from mst import prims_mst
import heapq
import copy


def check_all_nodes_visited(g ,node, goal):
    #total number of vertices
    n = len(g.graph.keys())
    # checking if path has all nodes and if start node is reachable  
    if len(node.path) == n-1 and g.graph[node.data][goal]!= None:
        return True
    return False 


def tsp(graph, start):
    # initialize the start node
    start_node = Node(start, 0)
    total_nodes_explored = 0
    # mst heuristic
    # start_node.path.append(start)
    h = prims_mst(graph, [], start)
    g = 0
    f = h + g

    # initialize the fringe list (priority queue)
    fringe = [(f, g, start_node)]
    
    while fringe:
        # pop the node with the lowest f-cost value
        f, g, node = heapq.heappop(fringe)
        total_nodes_explored += 1
        print("Pop = ",f, g, node)

        # set the explored list as already exposed path for the node
        explored = set(node.path)

        # check if all nodes are visited and you can return to the start node
        if check_all_nodes_visited(graph, node, start):
            total_cost = g + graph.graph[node.data][start].cost
            graph.graph[node.data][start].path = node.path.copy()
            # Adding the current node to the path of the node to start node
            graph.graph[node.data][start].path.append(node.data)
            # push the goal state node to the fringe
            heapq.heappush(fringe, (total_cost, 0, graph.graph[node.data][start]))

        #* Actual goal state check. Checks if path has all nodes plus start node 
        if len(node.path) == len(graph.graph.keys()):
            print("Total nodes explored = ",total_nodes_explored)
            pt = node.path.copy()
            pt.append(start)
            return pt, f
        
        # Since the path to all children is same (excluding themselves),
        # the heurisitic of the children is the same
        h = prims_mst(graph, node.path.copy() + [node.data], start)
        # if h the rest of the tree is disconnected, try other paths
        if h == float('inf'):
            continue

        # get the neighbors of the node
        for neighbor, neighbor_node in graph.graph[node.data].items():
            # making a deep copy of the node because python is crazy
            neighbor_node = copy.deepcopy(neighbor_node)
            if neighbor_node != None and neighbor not in explored:
                    # update neighbor node's path by adding the current node
                    neighbor_node.path = node.path.copy()
                    neighbor_node.path.append(node.data)

                    # calculate the new f value for the neighbor node
                    new_g = g + neighbor_node.cost      # cost upto the neighbor node (g(n))
                    new_h = h                           # mst heuristic (h(n))
                    new_f = new_h + new_g               # final f-cost
                    
                    # push the neighbor node to the fringe
                    heapq.heappush(fringe, (new_f, new_g, neighbor_node))
                    explored.add(neighbor_node.data)

    #! If no Hamiltonian cycle is found
    print(f"Total nodes explored = {total_nodes_explored}")
    return ("TSP tour not found!")

def main():
    graph = Graph()
    graph.make_graph("./fcgraph50.csv")
    print(tsp(graph, '1'))

if __name__ == '__main__':
    main() 
        
