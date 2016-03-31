"""
Marian Willard and Caroline Danzi
CSE 464 Algorithms
Implements an Edge and a Graph Class
"""

"""
Edge
Edges contain 2 nodes (one on each end) and a cost
"""
class Edge:
    def __init__(self, n1, n2, cost):
        self.node1 = n1
        self.node2 = n2
        self.cost = cost

    # (node1, node2, cost: cost)
    def __str__(self):
        return "(" + str(self.node1) + ", " + str(self.node2) + ", cost: " + str(self.cost) + ")"

"""
Graphs have numbered nodes starting at zero.  When you add a
node, the number of nodes increases and a new list is provided
for its edges. The edge list E contains one list for every node
in the graph.  This list stores a collection of edges for this node.
"""
class Graph:

    # Graphs have a list of all Edges and a collection of nodes,
    # which since we are numbering from zero we just need to know
    # the number of nodes.
    def __init__(self):
        self.E = []
        self.numNodes = 0

    # Node: x has edges: (); ();"
    def __str__(self):
        string = ""
        for node in range(len(self.E)):
            string += "Node " + str(node) + " has edges: "
            lst = self.E[node]
            for edge in lst:
                string += str(edge) + "; "
            string += "\n"
        print(string)
        return string

    # Checks that the node numbers given are valid for this
    # graph, creates an Edge object, and appends it to the
    # edge lists for each node.
    def addEdge(self, n1, n2, cost):
        if(n1 < 0 or n1 > self.numNodes):
            print("First node not in G")
        elif(n2 < 0 or n2 > self.numNodes):
            print("Second node not in G")
        else:
            edge = Edge(n1, n2, cost)
            self.E[n1].append(edge)
            self.E[n2].append(edge)

    # Since we do not store a list of the vertices, simply
    # add one to the number of nodes and create an empty list
    # for its edges.
    def addNode(self):
        self.numNodes += 1
        self.E.append([])

    # Returns the list of edges for the specified node.
    def getNeighbors(self, node):
        return self.E[node]


    
