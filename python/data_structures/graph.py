from collections import deque

class Vertex:
    """A vertex in a graph with a value associated with it.

    Attributes:
        value: The value or data associated with the vertex.
    """
    def __init__(self, value):
        self.value = value

class Edge:
    """An edge in a graph connecting two vertices with an optional weight.

    Attributes:
        vertex: The Vertex object that this edge points to.
        weight: An optional weight of the edge. Defaults to 0.
    """
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    """A graph, consisting of vertices (nodes) and edges between them.

    Attributes:
        _adjacency_list: A dictionary where keys are Vertex objects and values are lists of Edge objects,
                         representing the adjacency list of the graph.
    """
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """Adds a node with the given value to the graph.

        Parameters:
            value: The value associated with the node to be added.

        Returns:
            The newly created Vertex object.
        """
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start, end, weight=0):
        """Adds an edge between two nodes in the graph.

        Parameters:
            start: The starting Vertex object.
            end: The ending Vertex object.
            weight: Optional weight of the edge. Defaults to 0.

        Raises:
            KeyError: If either the start or end vertex does not exist in the graph.
        """
        if start not in self._adjacency_list or end not in self._adjacency_list:
            raise KeyError("One or more vertices not found in graph")
        self._adjacency_list[start].append(Edge(end, weight))

    def get_nodes(self):
        """Returns a list of all nodes in the graph.

        Returns:
            A list of Vertex objects.
        """
        return [vertex for vertex in self._adjacency_list]

    def get_neighbors(self, vertex):
        """Returns a list of edges connected to a given vertex.

        Parameters:
            vertex: The Vertex object whose neighbors are to be found.

        Returns:
            A list of Edge objects connected to the specified vertex.
        """
        return self._adjacency_list.get(vertex, [])

    def size(self):
        """Returns the number of nodes in the graph.

        Returns:
            An integer representing the number of nodes.
        """
        return len(self._adjacency_list)

    def breadth_first(self, start):
        """Performs a breadth-first search starting from a given node.

        Parameters:
            start: The starting Vertex object.

        Returns:
            A list of values representing the vertices visited in breadth-first order.
        """
        visited = []
        queue = deque([start])

        while queue:
            current = queue.popleft()
            if current not in visited:
                visited.append(current)
                neighbors = self.get_neighbors(current)
                for edge in neighbors:
                    if edge.vertex not in visited:
                        queue.append(edge.vertex)

        return [vertex.value for vertex in visited]

    def check_path_exists(self, start, end):
        """Checks if there is a path between two vertices in the graph.

        Parameters:
            start: The starting Vertex object.
            end: The ending Vertex object.

        Returns:
            True if a path exists, False otherwise.
        """
        visited = []
        queue = deque([start])

        while queue:
            current = queue.popleft()
            if current == end:
                return True
            if current not in visited:
                visited.append(current)
                neighbors = self.get_neighbors(current)
                for edge in neighbors:
                    if edge.vertex not in visited:
                        queue.append(edge.vertex)

        return False
