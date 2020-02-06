from graph_search import DirectedGraph, Edge, Node


class Cyclic(DirectedGraph):
    def _iscyclic(self, src, parent, stack):
        if src in stack:
            return True
        stack.add(src)
        for child in self.EdgesOf(src):
            if child not in parent:
                parent[child] = src
                status = self._iscyclic(child, parent, stack)
                if status:
                    return True
        return False

    def iscyclic(self):
        parent = dict()
        for node in self.nodes:
            stack = set()
            status = self._iscyclic(node, parent, stack)
            if status:
                return True
        return False


def test():
    nodes = []
    for name in range(4):
        nodes.append(Node(str(name)))  # Create 4 nodes

    graph = Cyclic()

    for node in nodes:
        graph.addNode(node)

    graph.addEdge(Edge(nodes[0], nodes[1]))
    graph.addEdge(Edge(nodes[0], nodes[2]))
    graph.addEdge(Edge(nodes[1], nodes[2]))
    graph.addEdge(Edge(nodes[2], nodes[0]))
    graph.addEdge(Edge(nodes[2], nodes[3]))
    graph.addEdge(Edge(nodes[3], nodes[3]))

    print("Graph:\n{}".format(graph))
    status = graph.iscyclic()
    print("Is graph cyclic: {}".format(status))

    graph = Cyclic()

    for node in nodes:
        graph.addNode(node)

    graph.addEdge(Edge(nodes[0], nodes[1]))
    graph.addEdge(Edge(nodes[1], nodes[3]))
    graph.addEdge(Edge(nodes[1], nodes[2]))
    graph.addEdge(Edge(nodes[3], nodes[2]))

    print("Graph:\n{}".format(graph))
    status = graph.iscyclic()
    print("Is graph cyclic: {}".format(status))


if __name__ == "__main__":
    test()
