import random
import math
import pprint
import matplotlib.pyplot as plt

# ----------------------------------
# 1. Generate random 2D points.
def generate_random_points(n, x_range=(0, 100), y_range=(0, 100)):
    points = []
    for _ in range(n):
        x = random.uniform(*x_range)
        y = random.uniform(*y_range)
        points.append((x, y))
    return points

# Compute Euclidean distance between two points.
def euclidean_distance(p, q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)

# ----------------------------------
# 2. Create a complete graph from the points.
# The graph is represented as a dictionary where each key is a node index,
# and its value is a dictionary mapping every other node's index to the Euclidean distance.
def create_complete_graph(points):
    graph = {}
    n = len(points)
    for i in range(n):
        graph[i] = {}
        for j in range(n):
            if i != j:
                graph[i][j] = euclidean_distance(points[i], points[j])
    return graph

# ----------------------------------
# 3. Nearest Neighbor TSP Algorithm (Greedy)
# This algorithm starts at a given start node and repeatedly visits the closest unvisited node.
def nearest_neighbor_tsp(graph, start):
    n = len(graph)
    unvisited = set(range(n))
    unvisited.remove(start)
    route = [start]
    current = start

    while unvisited:
        # Find the nearest neighbor from the current node.
        next_node = min(unvisited, key=lambda x: graph[current][x])
        route.append(next_node)
        unvisited.remove(next_node)
        current = next_node

    # Finally, return to the start to complete the cycle.
    route.append(start)
    return route

# Compute the total length of a given route based on the graph.
def calculate_route_length(route, graph):
    total = 0
    for i in range(len(route)-1):
        total += graph[route[i]][route[i+1]]
    return total

# ----------------------------------
# 4. (Optional) Plot the TSP route
def plot_tsp(points, route):
    plt.figure(figsize=(8, 6))
    
    # Plot the points.
    xs = [points[i][0] for i in range(len(points))]
    ys = [points[i][1] for i in range(len(points))]
    plt.scatter(xs, ys, c='blue')
    
    # Annotate points with their indices.
    
        
    
    # Plot the route.
    for i in range(len(route)-1):
        p1 = points[route[i]]
        p2 = points[route[i+1]]
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='green', linewidth=2)
    
    plt.title("TSP Route using Nearest Neighbor Heuristic")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

# ----------------------------------
# 5. Main function putting it all together.
def main():
    n_points = 1000
      # Adjust as needed.
    points = generate_random_points(n_points)
    
    # Create the complete graph.
    graph = create_complete_graph(points)
    
    # Print the graph dictionary to the console.
    
    # Choose a starting node (for simplicity, we choose node 0).
    start = 0
    tsp_route = nearest_neighbor_tsp(graph, start)
    total_length = calculate_route_length(tsp_route, graph)
    
    print("\nNearest Neighbor TSP Route (node indices):", tsp_route)
    print("Total distance of the route: {:.2f}".format(total_length))
    
    # Optionally, display the TSP route graphically.
    plot_tsp(points, tsp_route)

if __name__ == '__main__':
    main()
