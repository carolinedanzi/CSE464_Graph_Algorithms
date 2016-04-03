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

        print(str(graph))
        return graph

"""
if __name__ == "__main__":
    # Get file name from command line and send it to parseFile
    # The argv[0] is always the name of the program file
    # argv[1] will have the name of the file containing the graph
    graphFile = sys.argv[1]
    userGraph = parseGraphFromFile(graphFile)
    print(str(userGraph))
"""
