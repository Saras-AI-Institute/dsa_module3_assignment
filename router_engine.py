class DeliveryNetworkGraph:
    def __init__(self):
        # Adjacency list representation: { node: { neighbor: weight } }
        self.graph = {}

    def add_hub(self, hub_id: str):
        if hub_id not in self.graph:
            self.graph[hub_id] = {}

    def add_road(self, u: str, v: str, weight: float):
        """Adds a bidirectional weighted edge between hub 'u' and hub 'v'."""
        self.add_hub(u)
        self.add_hub(v)
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def find_shortest_delivery_route(self, start_hub: str, end_hub: str) -> float:
        """
        TODO:
        Implement an optimal shortest-path algorithm (e.g., Dijkstra's algorithm) 
        to return the absolute minimum total weight/distance from start_hub to end_hub.
        
        Return float('inf') if no route path exists.
        """
        # YOUR CODE HERE
        pass
