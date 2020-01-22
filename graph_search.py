from graphs import DirectedGraph, Node, Edge


class BFS(DirectedGraph):
    def search(self, src):
        parent = {src: None}
        level = {src: 0}
        counter = 1

        queue = [src]

        while queue:
            neighbours = []
            node = queue.pop(0)
            for vertex in self.edges[node]:
                if vertex not in level:
                    level[vertex] = counter
                    parent[vertex] = node
                    neighbours.append(vertex)
            counter += 1
            queue = neighbours

        return parent, level


class DFS(DirectedGraph):
    def search(self, src):
        parent = {}
        for node in self.nodes:
            if node not in parent:
                parent[node] = None
                parent = self.dfs_visit(src=node, parent=parent)
        return parent


    def dfs_visit(self, src, parent):
        for node in self.edges[src]:
            if node not in parent:
                parent[node] = src
                self.dfs_visit(node, parent)
        return parent


def test():
    vertices = []
    for i in range(0, 4):
        vertex = Node(i)
        vertices.append(vertex)
    edges = [
        Edge(vertices[0], vertices[1]),
        Edge(vertices[0], vertices[2]),
        Edge(vertices[1], vertices[2]),
        Edge(vertices[2], vertices[0]),
        Edge(vertices[2], vertices[3]),
        Edge(vertices[3], vertices[3]),
    ]

    # Breadth first search
    BFSdigraph = BFS()
    for vertex in vertices:
        BFSdigraph.addNode(vertex)
    for edge in edges:
        BFSdigraph.addEdge(edge)
    print("Directed Graph:\n", BFSdigraph, sep="")

    src = list(BFSdigraph.nodes)[3]
    parent, _ = BFSdigraph.search(src)
    print("BFS Search:")
    for key in parent.keys():
        print(key)

    # Depth first search
    DFSdigraph = DFS()
    for vertex in vertices:
        DFSdigraph.addNode(vertex)
    for edge in edges:
        DFSdigraph.addEdge(edge)
    print("Directed Graph:\n", DFSdigraph, sep="")

    src = list(DFSdigraph.nodes)[3]
    parent = DFSdigraph.search(src)
    print("DFS Search:")
    for key in parent.keys():
        print(key)
