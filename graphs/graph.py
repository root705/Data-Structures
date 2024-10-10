from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(set)  # Use a set to avoid duplicate edges

    def add_edge(self, u, v):
        """Add an edge from node u to node v."""
        self.graph[u].add(v)

    def generate_edges(self):
        """Generate all edges in the graph as a list of tuples."""
        return [(node, neighbor) for node in self.graph for neighbor in self.graph[node]]

    def display_edges(self):
        """Prints all the edges in the graph."""
        edges = self.generate_edges()
        for edge in edges:
            print(f"Edge: {edge[0]} -> {edge[1]}")

# Create a new graph instance
graph = Graph()

# Add edges to the graph
graph.add_edge('a', 'c')
graph.add_edge('b', 'c')
graph.add_edge('b', 'e')
graph.add_edge('c', 'd')
graph.add_edge('c', 'e')
graph.add_edge('c', 'a')
graph.add_edge('c', 'b')
graph.add_edge('e', 'b')
graph.add_edge('d', 'c')
graph.add_edge('e', 'c')

# Display the generated edges
graph.display_edges()
