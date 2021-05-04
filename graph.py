import random

class Vertex(object):
    def __init__(self, value):
        self.value = value  # value is the word
        self.adjacent = {}  # nodes that have an edge from this vertex
        self.neighbors = []
        self.neighbors_weights = []

    def add_edge_to(self, vertex, weight=0):
        # add edge to vertex with weight
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_adjacent_nodes(self):
        pass

    # initializes probability map
    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]



class Graph(object):
    def __init__(self):
        self.vertices = {}  # maps string to Vertex

    def get_vertex_values(self):
        # return all possible words
        return set(self.vertices.keys())

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()
