from collections import OrderedDict

from graphs import DirectedGraph, Edge, Node


class GraphSearch(DirectedGraph):
    def bfs(self, src, dest):
        level = {src: None}
        parent = {src: None}
        counter = 1

        queue = [src]
        while queue:
            node = queue.pop(0)
            for child in self.EdgesOf(node):
                if child not in level:
                    parent[child] = node
                    level[child] = counter
                    if child == dest:
                        break
                    queue.append(child)
            counter += 1

        return parent, level

    def bfsShortest(self, src, dest):
        path = []
        parent, level = self.bfs(src=src, dest=dest)

        dest_level = level[dest]
        while dest_level > 0:
            path.append(str(dest))
            dest = parent[dest]
            dest_level -= 1

        return path[::-1]

    def printpath(self, path):
        return "->".join([str(n) for n in path])

    def dfs(self, src, dest, path, shortest):
        path[src] = None
        if src == dest:
            return path
        for child in self.EdgesOf(src):
            if child not in path:
                if shortest == None or len(path) < len(shortest):
                    new_path = self.dfs(child, dest, path.copy(), shortest)
                    if new_path != None:
                        shortest = new_path
        return shortest

    def dfsShortest(self, src, dest):
        return self.dfs(src, dest, OrderedDict(), None)


def build_and_test():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))  # Create 6 nodes
    g = GraphSearch()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0], nodes[1]))
    g.addEdge(Edge(nodes[1], nodes[2]))
    g.addEdge(Edge(nodes[2], nodes[3]))
    g.addEdge(Edge(nodes[2], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[5]))
    g.addEdge(Edge(nodes[0], nodes[2]))
    g.addEdge(Edge(nodes[1], nodes[0]))
    g.addEdge(Edge(nodes[3], nodes[1]))
    g.addEdge(Edge(nodes[4], nodes[0]))

    # Print Directed Graph
    print("Graph:\n{}".format(g))

    # Shortest path using BFS.
    bfspath = g.bfsShortest(nodes[0], nodes[5])
    print("BFS Shortest path: {}".format(g.printpath(path=bfspath)))
    print("BFS Shortest path test passed:", bfspath == ["0", "2", "3", "5"])

    # Shortest path using DFS.
    dfspath = g.dfsShortest(nodes[0], nodes[5])
    print("DFS Shortest path: {}".format(g.printpath(path=dfspath)))
    print(
        "DFS Shortest path test passed:",
        [str(n) for n in dfspath] == ["0", "2", "3", "5"],
    )


if __name__ == "__main__":
    build_and_test()
