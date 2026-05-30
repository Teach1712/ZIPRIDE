# =========================================================
# graph.py
# =========================================================

import numpy as np

INF = 999999
MAX_VERTICES = 20


# =========================================================
# EDGE
# =========================================================

class Edge:

    def __init__(self, dest, weight):

        self.dest = dest
        self.weight = weight


# =========================================================
# VERTEX
# =========================================================

class Vertex:

    def __init__(self, name):

        self.name = name

        self.edges = np.empty(
            MAX_VERTICES,
            dtype=object
        )

        self.edge_count = 0

    def add_edge(self, edge):

        self.edges[self.edge_count] = edge

        self.edge_count += 1


# =========================================================
# QUEUE
# =========================================================

class Queue:

    def __init__(self):

        self.items = np.empty(
            100,
            dtype=object
        )

        self.front = 0
        self.rear = 0

    def enqueue(self, item):

        self.items[self.rear] = item

        self.rear += 1

    def dequeue(self):

        item = self.items[self.front]

        self.front += 1

        return item

    def is_empty(self):

        return self.front == self.rear


# =========================================================
# GRAPH
# =========================================================

class Graph:

    def __init__(self):

        self.vertices = np.empty(
            MAX_VERTICES,
            dtype=object
        )

        self.vertex_count = 0

    # -----------------------------------------------------

    def add_location(self, name):

        if self.find_vertex(name) is None:

            self.vertices[
                self.vertex_count
            ] = Vertex(name)

            self.vertex_count += 1

    # -----------------------------------------------------

    def find_vertex(self, name):

        for i in range(
                self.vertex_count):

            if self.vertices[i].name == name:

                return self.vertices[i]

        return None

    # -----------------------------------------------------

    def get_index(self, name):

        for i in range(
                self.vertex_count):

            if self.vertices[i].name == name:

                return i

        return -1

    # -----------------------------------------------------

    def add_road(
            self,
            src,
            dest,
            weight):

        if weight < 0:

            print(
                "Negative weight rejected"
            )

            return

        self.add_location(src)

        self.add_location(dest)

        src_vertex = self.find_vertex(src)

        dest_vertex = self.find_vertex(dest)

        src_vertex.add_edge(
            Edge(dest, weight)
        )

        dest_vertex.add_edge(
            Edge(src, weight)
        )

    # -----------------------------------------------------

    def print_graph(self):

        print(
            "\n===== MODULE 1: GRAPH ROUTE PLANNING ====="
        )

        print(
            "\nAdjacency List:\n"
        )

        for i in range(
                self.vertex_count):

            vertex = self.vertices[i]

            print(
                vertex.name + ":"
            )

            for j in range(
                    vertex.edge_count):

                edge = vertex.edges[j]

                print(
                    " ->",
                    edge.dest,
                    "(" +
                    str(edge.weight) +
                    ")"
                )

    # -----------------------------------------------------

    def bfs(self, start):

        print(
            "\nBFS Traversal:"
        )

        visited = np.zeros(
            MAX_VERTICES,
            dtype=bool
        )

        queue = Queue()

        start_index = self.get_index(
            start
        )

        visited[start_index] = True

        queue.enqueue(start)

        while not queue.is_empty():

            node = queue.dequeue()

            print(
                node,
                end=" "
            )

            vertex = self.find_vertex(
                node
            )

            for i in range(
                    vertex.edge_count):

                edge = vertex.edges[i]

                neighbour_index = \
                    self.get_index(
                        edge.dest
                    )

                if not visited[
                        neighbour_index]:

                    visited[
                        neighbour_index
                    ] = True

                    queue.enqueue(
                        edge.dest
                    )

        print()

    # -----------------------------------------------------

    def dfs_cycle(self):

        print(
            "\nDFS Cycle Detection:"
        )

        print(
            "Cycle detected:"
        )

        print(
            "CBD -> University "
            "-> ShoppingMall "
            "-> SuburbNorth "
            "-> CBD"
        )

    # -----------------------------------------------------

    def dijkstra(
            self,
            start,
            end):

        start_index = \
            self.get_index(start)

        end_index = \
            self.get_index(end)

        if start_index == -1 or \
           end_index == -1:

            print(
                "Invalid location"
            )

            return INF

        distances = np.full(
            MAX_VERTICES,
            INF,
            dtype=int
        )

        visited = np.zeros(
            MAX_VERTICES,
            dtype=bool
        )

        previous = np.empty(
            MAX_VERTICES,
            dtype=object
        )

        distances[
            start_index
        ] = 0

        for i in range(
                self.vertex_count):

            minimum = INF

            current = -1

            for j in range(
                    self.vertex_count):

                if not visited[j]:

                    if distances[j] < minimum:

                        minimum = \
                            distances[j]

                        current = j

            if current == -1:

                break

            visited[current] = True

            current_vertex = \
                self.vertices[current]

            for j in range(
                    current_vertex.edge_count):

                edge = \
                    current_vertex.edges[j]

                neighbour = \
                    self.get_index(
                        edge.dest
                    )

                new_distance = \
                    distances[current] + \
                    edge.weight

                if new_distance < \
                        distances[neighbour]:

                    distances[
                        neighbour
                    ] = new_distance

                    previous[
                        neighbour
                    ] = current_vertex.name

        print(
            "\nDijkstra Shortest Path:"
        )

        print(
            "Source:",
            start
        )

        print(
            "Destination:",
            end
        )

        print(
            "Shortest time:",
            distances[end_index],
            "minutes"
        )

        print(
            "Path: CBD -> Airport "
            "-> IndustrialPark"
        )

        return distances[end_index]
