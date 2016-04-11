import sys
import re
from Graph import Graph
from Graph import Edge

# parses a text file with one line of the format
# 4 $ 1,2,3 ; 2,1,5
# Where the first number before the $ is the number of
# nodes in the graph and the section after $ lists the edges
# in the form node1, node2, cost; for an edge from node1 to node2
# with a weight of cost.
# Builds the corresponding graph and returns it.
def parseGraphFromFile(fileName):
    file = open(fileName, 'r')
    line = file.readline()
    
    graph = Graph()
    # take out any extra whitespace, such as 1   $  2  , 3...
    line = re.sub("\s*", "", line)
    # partition returns a 3-tuple of the string before the
    # specified delimiter, the delimiter, and the string after
    # the delimiter
    parts = line.partition('$')
    # the first part contains the list of nodes
    # add each node to the graph
    numNodes = parts[0]
    for i in range(int(numNodes)):
        graph.addNode()

    # each edge has the form node1, node2, cost
    edgeList = parts[2].split(';')
    for edge in edgeList:
        n1, n2, cost = edge.split(',')
        n1 = int(n1)
        n2 = int(n2)
        cost = int(cost)
        graph.addEdge(n1, n2, cost)
        
    return graph

# Depth First Search
# Note: According to https://wiki.python.org/moin/TimeComplexity
# the time complexity of x in s is O(n), where n is the lenght of s
# and the time complexity of append is O(1)
def DFS(G, start, dest):
    # s is a stack
    workList = []
    visited = []
    workList.append(start)
    while (len(visited) != G.numNodes):
        n = workList.pop()
        visited.append(n)
        if(n == dest):
            return True
        else:
            # getNeighbors actually returns the list of edges
            # connected to node n
            edgeList = G.getNeighbors(n)
            for v in edgeList:
                if v.node2 not in visited:
                    workList.append(v.node2)
    return False

def prims(G):
    # The minimum spanning tree will be a list of Edge objects
    min_span_tree = []

    # If there are more than 0 nodes, will put node 0
    # in left and the rest of the nodes in right
    # O(n) time
    left, right = cut(G)

    # Loop: O(n * (n^2 * d)) = O(dn^3)
    while len(left) < G.numNodes:
        # Find the minimum edge that connects a node
        # from left to a node in right
        e = cheapest_connection(G, left, right)
        # Add the edge to the minimum spanning tree
        min_span_tree.append(e)
        # Add the node from right to left
        left.append(e.node2)
        # Remove the node from right
        right.remove(e.node2)
        
    return min_span_tree

# Returns 2 lists that represent a cut of the graph, where
# one list has a length of one and the other has the rest of
# the nodes. Runs in O(n) time where n is the number of nodes in G
def cut(G):
    left = []
    right = []
    # If we have at least one node in the graph,
    # make the cut
    if(G.numNodes > 0):
        # left gets the starting node (node 0)
        left.append(0)
        # Add the nodes 1...n to the right list
        for node in range(G.numNodes - 1):
            right.append(node + 1)
            
    return left, right

# If G is a weighted, connected graph and S1 and S2 represent a
# cut of G, then cheapest_connection(G, S1, S2) is the edge with
# the lowest cost that connects a node in S1 to a node in S2
# Runs in O(n^2 * d), where n is the number of nodes and d is
# the highest degree of any node in G
def cheapest_connection(G, S1, S2):
    minEdge = Edge(-1, -1, sys.maxsize)
    for node1 in S1:
        for node2 in S2:
            # Runs in O(d), where d is the highest degree of any node
            edge = G.getEdge(node1, node2) 
            if edge and edge.cost < minEdge.cost:
                minEdge = edge
    return minEdge


def shortestPath(G, start, target):
    R = dijkstra(G, start, target)
    D = R[1]
    P = R[0]
    s = []
    u = int(target)
    print("u = " + str(u))
    print(P)
    while P[u] != u and u != None:
        s.append(u)
        u = P[u]
    s.append(u)
    print("Shortest path from " + str(start) + " to " + str(target) + " is: \n")
    while len(s) != 0:
        print(str(s.pop()) + " ")
    print("Cost: " + str(D[target]))

# Dijkstra's Algorithm
def dijkstra(G, start, target):
    # V is list of visited nodes
    V = [start]
    # D is an array of the total costs of the paths
    D = [sys.maxsize] * G.numNodes
    # P is an array of the parents
    P = [None] * G.numNodes
    # set start node parent to start
    P[start] = start
    # set start node path cost to 0
    D[start] = 0
    while(len(V) != G.numNodes):
        temp = sys.maxsize
        n = Edge(0, 0, 0) # n will be the minimal edge
        for i in V: # for every visited node
            for c in G.getNeighbors(i):    # for every neighbor of i
                # find minimal edge from node in V to node not in V
                if not c.node2 in V:
                    if c:       # if c is a not null edge
                        if D[i] + c.cost < temp:    # is this new edge minimal
                            temp = D[i] + c.cost
                            n = c
        # n should be the minimum edge where D[n.node1] + n.cost is minimal
        # total cost of dest node = total cost of parent node +
        # cost(parent, dest)
        D[n.node2] = D[n.node1] + n.cost
        # add dest node to V
        V.append(n.node2)
        # update parent of dest node
        P[n.node2] = n.node1
        # if dest node is the target node
        # then return the list of parents and costs
        if(n.node2 == target):
            R = [P, D]
            return R
    # end while
    R = [P, D]
    return R

if __name__ == "__main__":
    graphFileName = input("Enter in the name of the graph file: ")
    userGraph = parseGraphFromFile(graphFileName)
    print(str(userGraph))
    
    choice = input("Please enter a menu option:\n0) Exit\n1) Is there a path from A to B?\n2) What is the shortest path from A to B?\n3) Find the minimum spanning tree\n")
    while(choice != '0'):
        if choice == '1':
            start = input("Enter a starting node: ")
            destination = input("Enter a destination node: ")
            answer = DFS(userGraph, int(start), int(destination))
            print("There is a path.") if answer is True else print("No path exists.")
        elif choice == '2':
            start = input("Enter a starting node: ")
            target = input("Enter a destination node: ")
            shortestPath(userGraph, int(start), int(target))
        elif choice == '3':
            mst = prims(userGraph)
            for edge in mst:
                print(edge)
        else:
            print("Sorry, that was not an option")
        choice = input("\nPlease enter a menu option:\n0) Exit\n1) Is there a path from A to B?\n2) What is the shortest path from A to B?\n3) Find the minimum spanning tree\n")
        
