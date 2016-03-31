
class Edge:
    def __init__(self, n1, n2, cost):
        self.node1 = n1
        self.node2 = n2
        self.cost = cost    

class Graph:

    """
    Notes:
    have a dictionary of the nodes and their indices
    dictionary of vertex: edge list
    research Python3 efficiency dictionary vs. list
    """
    def __init__(self):
        E = []
        V = []

    def addEdge(self, n1, n2, cost):
        edge = Edge(n1, n2, cost)

    def addNode(self, node):

    def getNeighbors(self, node):

    
