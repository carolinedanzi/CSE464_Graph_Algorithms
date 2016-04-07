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
def DFS(G, start, dest):
    s = []
    s.append(start) # stack
    while (len(s) != 0):
        n = s.pop()
        if(n == dest):
            return True
        else:
            N = G.getNeighbors(n)
            for v in N:
                s.append(v.node2)
    return False

 # Dijkstra's Algorithm
def dijkstras(G, start, target):
    V = G
    D[0:len(G)] = sys.maxint
    P[0:len(G)] = None
    D[0] = start
    return 'not done yet'

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

# Dijkstra's Algorithm
def dijkstra(G, start, target):
    V = list(range(G.numNodes))
    D = [sys.maxsize] * G.numNodes
    P = [None] * G.numNodes
    D[0] = start
    while(len(V) != 0):
        temp = sys.maxsize
        n = 0 # n is only the value of the node
        for i in V: # check this out, it's not right yet
            if int(D[i]) < int(temp):
                temp = D[i]
                n = i
        if(n == target):
            R = [P, D]
            return R
            # return P, D
        N = G.getNeighbors(n)
        for c in N:     # c is an edge node, thus c.node2 is the value of
                        # the destination of the edge
            if(D[n] + c.cost < D[c.node2]):
               D[c.node2] = D[n] + c.cost
               P[c.node2] = n
        V.remove(n)
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
            print(dijkstra(userGraph), int(start), int(target))
        elif choice == '3':
            mst = prims(userGraph)
            for edge in mst:
                print(edge)
        else:
            print("Sorry, that was not an option")
        choice = input("\nPlease enter a menu option:\n0) Exit\n1) Is there a path from A to B?\n2) What is the shortest path from A to B?\n3) Find the minimum spanning tree\n")
        
