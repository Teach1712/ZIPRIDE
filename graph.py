# =========================================================
# graph.py (clean version with requested changes)
# =========================================================

INF = 999999

class Edge:
    def __init__(self, dest, weight):
        self.dest = dest
        self.weight = weight

class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)

class Graph:
    def __init__(self):
        self.vertices = []

    def add_location(self, name):
        if self.find_vertex(name) is None:
            self.vertices.append(Vertex(name))

    def find_vertex(self, name):
        for v in self.vertices:
            if v.name == name:
                return v
        return None

    def add_road(self, src, dest, weight):
        if weight < 0:
            print("Negative weight rejected")
            return
        self.add_location(src)
        self.add_location(dest)
        src_vertex = self.find_vertex(src)
        dest_vertex = self.find_vertex(dest)
        src_vertex.add_edge(Edge(dest, weight))
        dest_vertex.add_edge(Edge(src, weight))

    def print_graph(self):
        print("\n===== MODULE 1: GRAPH ROUTE PLANNING =====")
        print("\nAdjacency List:\n")
        for v in self.vertices:
            print(v.name + ":")
            for e in v.edges:
                print(" ->", e.dest, "(" + str(e.weight) + ")")

    def bfs(self, start):
        print("\nBFS Traversal (with levels):")
        visited = {v.name: False for v in self.vertices}
        queue = [(start, 0)]
        visited[start] = True
        current_level = 0
        level_nodes = []
        while queue:
            node, level = queue.pop(0)
            if level != current_level:
                print(f"Level {current_level}: {' '.join(level_nodes)}")
                level_nodes = []
                current_level = level
            level_nodes.append(node)
            vertex = self.find_vertex(node)
            for e in vertex.edges:
                if not visited[e.dest]:
                    visited[e.dest] = True
                    queue.append((e.dest, level + 1))
        print(f"Level {current_level}: {' '.join(level_nodes)}")

    def dfs_cycle(self, start):
        print("\nDFS Cycle Detection:")
        visited = {v.name: False for v in self.vertices}
        stack = []
        parent = {}

        def dfs(node):
            visited[node] = True
            stack.append(node)
            vertex = self.find_vertex(node)
            for e in vertex.edges:
                if not visited[e.dest]:
                    parent[e.dest] = node
                    if dfs(e.dest):
                        return True
                elif parent.get(node) != e.dest and e.dest in stack:
                    print("Cycle found:", " -> ".join(stack + [e.dest]))
                    return True
            stack.pop()
            return False

        if not dfs(start):
            print("No cycle detected.")

    def dijkstra(self, start, end):
        distances = {v.name: INF for v in self.vertices}
        previous = {v.name: None for v in self.vertices}
        distances[start] = 0
        unvisited = [v.name for v in self.vertices]

        while unvisited:
            # Pick node with smallest distance
            current = min(unvisited, key=lambda n: distances[n])
            unvisited.remove(current)

            vertex = self.find_vertex(current)
            for e in vertex.edges:
                new_dist = distances[current] + e.weight
                if new_dist < distances[e.dest]:
                    distances[e.dest] = new_dist
                    previous[e.dest] = current

        # Build path
        path = []
        node = end
        while node:
            path.insert(0, node)
            node = previous[node]

        print("\nDijkstra Shortest Path:")
        print("Source:", start)
        print("Destination:", end)
        print("Shortest time:", distances[end], "minutes")
        print("Path:", " -> ".join(path))
        return distances[end]
