
//Implemenation in Prims Algorithm
from queue import PriorityQueue
class Graph:

    def __init__(self, vertices):
        self.V = vertices   # Total number of vertices in the graph
        self.graph = []     # Array of edges

    # Add edges
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    # Print the solution
    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def prims(self, src):
    # Create an array to store the minimum distance from the source vertex
        dist = [float("Inf")] * self.V
        # Mark the source vertex
        dist[src] = 0
        # Create a set to store the vertices included in the MST
        included = set()
        # Create a priority queue to store the edges
        pq = PriorityQueue()
        # Add the edges of the source vertex to the queue
        for neighbor, weight in self.graph[src]:
            pq.put((weight, src, neighbor))
        # Repeat the process until all vertices are included in the MST
        while len(included) != self.V:
            # Get the edge with the smallest weight
            weight, s, d = pq.get()
            # If the destination vertex of the edge is already in the MST, skip it
            if d in included:
                continue
            # Add the destination vertex to the MST
            included.add(d)
            # Update the minimum distance of the destination vertex
            dist[d] = weight
            # Add the edges of the destination vertex to the queue
            for neighbor, weight in self.graph[d]:
                if neighbor not in included:
                    pq.put((weight, d, neighbor))
    # Print the solution
            self.print_solution(dist)



g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 3)
g.add_edge(2, 1, 6)
g.add_edge(3, 2, 2)

g.prims(0)
