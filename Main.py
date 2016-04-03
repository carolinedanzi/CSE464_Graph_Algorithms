import sys
import re
from Graph import Graph

class Main:

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
        return 'not implemented yet'

    if __name__ == "__main__":
        graphFileName = input("Enter in the name of the graph file: ")
        userGraph = parseGraphFromFile(graphFileName)
        print(str(userGraph))
        
        choice = input("Please enter a menu option:\n0) Exit\n1) Is there a path from A to B?\n2) What is the shortest path from A to B?\n3) Find the minimum spanning tree\n")
        while(choice != '0'):
            if choice == '1':
                start = input("Enter a starting node: ")
                destination = input("Enter a destination node: ")
                print(DFS(userGraph, int(start), int(destination)))
            elif choice == '2':
                start = input("Enter a starting node: ")
                target = input("Enter a destination node: ")
                print(dijkstra(userGraph), int(start), int(target))
            elif choice == '3':
                print(prims(userGraph))
            else:
                print("Sorry, that was not an option")
            choice = input("Please enter a menu option:\n0) Exit\n1) Is there a path from A to B?\n2) What is the shortest path from A to B?\n3) Find the minimum spanning tree\n")
        
