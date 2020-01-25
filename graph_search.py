from collections import OrderedDict

from graphs import DirectedGraph, Edge, Node


class GraphSearch(DirectedGraph):
    def bfs(self, src, dest):
        path = OrderedDict()
        path[src] = None
        queue = [src]

        while queue:
            node = queue.pop(0)
            for edge in self.EdgesOf(node):
                if edge not in path:
                    path[edge] = node
                    if edge == dest:
                        return path
                    queue.append(edge)
        return path

    def bfsShortest(self, src, dest):
        path = OrderedDict()
        path[src] = None
        queue = [src]
        shortest = None

        while queue:
            node = queue.pop(0)
            for edge in self.EdgesOf(node):
                if edge not in path:
                    path[edge] = node
                    if edge == dest:
                        shortest = path
                    queue.append(edge)
        return shortest

    def printpath(self, path, verbose=1):
        if path is None:
            print("No path found")

        if verbose > 1:
            for dest, src in path.items():
                print("{} -> {}".format(src, dest))
        else:
            for node in path.keys():
                print("{}->".format(node), end="", sep="")

    def dfs_visit(self, src, parent):
        for node in self.EdgesOf(src):
            if node not in parent:
                parent[node] = src
                parent = self.dfs_visit(node, parent)
        return parent

    def dfs_search(self, src):
        parent = {}
        for node in self.nodes:
            if node not in parent:
                parent[node] = None
                self.dfs_visit(src=node, parent=parent)
        return parent


def build_graph():
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
    digraph = GraphSearch()
    for vertex in vertices:
        digraph.addNode(vertex)
    for edge in edges:
        digraph.addEdge(edge)

    return digraph


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

    digraph = GraphSearch()
    for vertex in vertices:
        digraph.addNode(vertex)
    for edge in edges:
        digraph.addEdge(edge)
    print("Directed Graph:\n", digraph, sep="")

    src = list(digraph.nodes)[3]
    parent, _ = digraph.bfs_search(src)
    print("BFS Search:")
    for key in parent.keys():
        print(key)

    parent = digraph.dfs_search(src)
    print("DFS Search:")
    for key in parent.keys():
        print("{key}: {parent}".format(key=key, parent=parent[key]))
