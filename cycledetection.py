from graph_search import DirectedGraph, Edge, Node


class ACyclicGraph(DirectedGraph):
    def _iscyclic(self, src, parent, stack):
        stack.add(src)
        for child in self.EdgesOf(src):
            if child in stack:
                return True
            if child not in parent:
                parent[child] = src
                if self._iscyclic(child, parent, stack):
                    return True
        stack.remove(src)
        return False

    def iscyclic(self):
        parent = dict()
        stack = set()
        for node in self.nodes:
            if node not in parent:
                parent[node] = None
                if self._iscyclic(node, parent, stack):
                    return True
        return False


def test():
    nodes = []
    for name in range(4):
        nodes.append(Node(str(name)))  # Create 4 nodes

    graph = ACyclicGraph()

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

    graph = ACyclicGraph()

    for node in nodes:
        graph.addNode(node)

    graph.addEdge(Edge(nodes[0], nodes[1]))
    graph.addEdge(Edge(nodes[1], nodes[3]))
    graph.addEdge(Edge(nodes[1], nodes[2]))
    graph.addEdge(Edge(nodes[3], nodes[2]))

    print("Graph:\n{}".format(graph))
    status = graph.iscyclic()
    print("Is graph cyclic: {}".format(status))


    graph = ACyclicGraph()

    for node in nodes[:-1]:
        graph.addNode(node)

    graph.addEdge(Edge(nodes[0], nodes[1]))
    graph.addEdge(Edge(nodes[1], nodes[2]))
    graph.addEdge(Edge(nodes[2], nodes[0]))

    print("Graph:\n{}".format(graph))
    status = graph.iscyclic()
    print("Is graph cyclic: {}".format(status))


if __name__ == "__main__":
    test()
