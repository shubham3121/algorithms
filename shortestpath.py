"""
Dijkstra's algorithm, with edges represented as adjancecy matrix.

"""


class Graph:
    def __init__(self, vertices):
        self.vertices = [vertex for vertex in range(vertices)]
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printgraph(self):
        for row in self.graph:
            for col in row:
                print(col, end="\t")
            print("")

    def shortestPath(self, src, dest):
        visited = set()
        parent = dict()
        distances = dict()

        for vertex in self.vertices:
            distances[vertex] = float("inf")

        distances[src] = 0
        parent[src] = None

        for u in self.vertices:
            u = self.findMinimum(distances, visited)
            if u not in visited:
                visited.add(u)
            for v in self.vertices:
                if v not in visited and self.graph[u][v]:
                    weight = self.graph[u][v]
                    parent, distances = self.relax(u, v, weight, distances, parent)
                    if v == dest:
                        break
        return parent, distances

    def findMinimum(self, distances, visited):
        min_val, min_key = None, None
        for key, val in distances.items():
            if key not in visited:
                if min_val and val < min_val:
                    min_key, min_val = key, val
                elif min_val is None:
                    min_key, min_val = key, val
        return min_key

    def relax(self, u, v, weight, distances, parent):
        if distances[v] > distances[u] + weight:
            distances[v] = distances[u] + weight
            parent[v] = u
        return parent, distances

    def printpath(self, parent, dest):
        if parent[dest] == None:
            print("Path:", dest, end=",")
            return
        self.printpath(parent, parent[dest])
        print(dest, end=",")


def test():
    g = Graph(9)
    g.graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0],
    ]
    g.printgraph()
    src, dest = (0, 8)
    print("\nsrc:{}, dest:{}".format(src, dest))
    parent, dist = g.shortestPath(src, dest)
    g.printpath(parent, dest)
    print("\nTotal distance covered:", dist[dest])

    src, dest = (3, 6)
    print("\nsrc:{}, dest:{}".format(src, dest))
    parent, dist = g.shortestPath(src, dest)
    g.printpath(parent, dest)
    print("\nTotal distance covered:", dist[dest])


if __name__ == "__main__":
    test()
