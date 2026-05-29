# =========================================================
# graph.py (fixed)
# =========================================================

import numpy as np

INF = 999999
MAX_VERTICES = 20

class Edge:
    def __init__(self, dest, weight):
        self.dest = dest
        self.weight = weight

class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.edge_count = 0
    def add_edge(self, edge):
        self.edges.append(edge)
        self.edge_count += 1

class Graph:
    def __init__(self):
        self.vertices = []
        self.vertex_count = 0

    def add_location(self, name):
        if self.find_vertex(name) is None:
            self.vertices.append(Vertex(name))
            self.vertex_count += 1

    def find_vertex(self, name):
        for v in self.vertices:
            if v.name == name:
                return v
        return None

    def get_index(self, name):
        for i, v in enumerate(self.vertices):
            if v.name == name:
                return i
        return -1

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
        start_index = self.get_index(start)
        end_index = self.get_index(end)
        if start_index == -1 or end_index == -1:
            print("Invalid location")
            return INF
        distances = {v.name: INF for v in self.vertices}
        previous = {v.name: None for v in self.vertices}
        distances[start] = 0
        visited = set()
        while len(visited) < self.vertex_count:
            current = min((v for v in self.vertices if v.name not in visited),
                          key=lambda v: distances[v.name], default=None)
            if current is None or distances[current.name] == INF:
                break
            visited.add(current.name)
            for e in current.edges:
                new_dist = distances[current.name] + e.weight
                if new_dist < distances[e.dest]:
                    distances[e.dest] = new_dist
                    previous[e.dest] = current.name
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
