from cycledetection import ACyclicGraph, Node, Edge


class TopologicalSort(ACyclicGraph):
    """
    Since in a directed acyclic graph, unrelated vertices may 
    be present, thus there are serveral topological sortings of G.
    """

    def _sort(self, src, parent, order):
        for child in self.EdgesOf(src):
            if child not in parent:
                parent[child] = src
                order = self._sort(child, parent, order)
                order.append(child)
        return order

    def sort(self):
        parent = dict()
        order = []
        for node in self.nodes:
            if node not in parent:
                parent[node] = None
                order = self._sort(node, parent, order)
                order.append(node)
        return order[::-1]


def test():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))

    graph = TopologicalSort()

    for node in nodes:
        graph.addNode(node)

    graph.addEdge(Edge(nodes[5], nodes[2]))
    graph.addEdge(Edge(nodes[5], nodes[0]))
    graph.addEdge(Edge(nodes[4], nodes[0]))
    graph.addEdge(Edge(nodes[4], nodes[1]))
    graph.addEdge(Edge(nodes[2], nodes[3]))
    graph.addEdge(Edge(nodes[3], nodes[1]))

    print("Graph:\n{}".format(graph))

    if graph.iscyclic():
        print("Graph is cyclic, cannot perform toplogical sort.")
        return
    print("Graph is acyclic.")

    sorted_order = graph.sort()
    print("Topologically sorted graph....")
    print("-->".join([str(node) for node in sorted_order]))


if __name__ == "__main__":
    test()
