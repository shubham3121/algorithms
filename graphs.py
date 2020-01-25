class Node:
    """
    Node representation in a graph. 
    Node is also refered to as vertices.
    """

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)



class Edge:
    """
    Edge representation in the graph.
    """

    def __init__(self, src, dest):
        self._src = src
        self._dest = dest

    @property
    def sourceNode(self):
        return self._src

    @property
    def destNode(self):
        return self._dest

    def __str__(self):
        return u"{} -> {}".format(self._src, self._dest)


class DirectedGraph:
    """
    Directed Graph, assumes source node always points to destination node.
    """

    def __init__(self):
        self.nodes = set([])
        # Adjacency list, to keep track of a node and its corresponding edges
        self.edges = {}

    def addNode(self, node):
        """
        Adds a node/ vertex in the graph.
        """
        if node in self.nodes:
            raise ValueError("Duplicate entry")
        self.nodes.add(node)
        self.edges[node] = []

    def addEdge(self, edge):
        """
        Adds an edge between two nodes/vertex.
        """
        src = edge.sourceNode
        dest = edge.destNode
        if src not in self.nodes:
            raise ValueError("Node not in graph {}".format(src))
        if dest not in self.nodes:
            raise ValueError("Node not in graph {}".format(dest))
        self.edges[src].append(dest)

    def __str__(self):
        output = ""
        for node in self.nodes:
            for edge in self.EdgesOf(node):
                output += "{} -> {} \n".format(node, edge)
        return output[:-1]

    def hasNode(self, node):
        return node in self.nodes

    def EdgesOf(self, node):
        return self.edges[node]


class Graph(DirectedGraph):
    """
    Undirected graph
    """

    def addEdge(self, edge):
        super().addEdge(edge=edge)
        src = edge.sourceNode
        dest = edge.destNode
        revEdge = Edge(src=dest, dest=src)
        super().addEdge(edge=revEdge)


def test():
    vertices = []
    for i in range(0, 3):
        vertex = Node(i)
        vertices.append(vertex)
    edges = [Edge(vertices[0], vertices[1]), Edge(vertices[0], vertices[2])]

    digraph = DirectedGraph()
    for vertex in vertices:
        digraph.addNode(vertex)
    for edge in edges:
        digraph.addEdge(edge)
    print("Directed Graph:\n",digraph, sep='')

    undirectgraph = Graph()
    for vertex in vertices:
        undirectgraph.addNode(vertex)
    for edge in edges:
        undirectgraph.addEdge(edge)
    print("Undirected Graph:\n",undirectgraph, sep='')


if __name__ == "__main__":
    test()
