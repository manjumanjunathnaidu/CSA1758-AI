from itertools import permutations

def tsp_brute_force(graph, start):
    """
    Solve the Travelling Salesman Problem using brute force.
    Args:
        graph (dict): Adjacency matrix representation of the graph.
                      Example: {A: {B: 10, C: 15}, B: {A: 10, C: 35}, ...}.
        start (str): Starting city.
    Returns:
        tuple: (shortest_path, minimum_cost)
    """
    cities = list(graph.keys())
    cities.remove(start)
    min_cost = float('inf')
    best_path = []

    # Generate all permutations of cities to visit
    for perm in permutations(cities):
        # Add the starting city at the beginning and end of the path
        path = [start] + list(perm) + [start]
        # Calculate the cost of the current path
        cost = sum(graph[path[i]][path[i+1]] for i in range(len(path) - 1))

        # Update the minimum cost and best path
        if cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost


# Example usage
if __name__ == "__main__":
    # Define the graph as an adjacency matrix
    graph = {
        'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
    }

    start_city = 'A'
    path, cost = tsp_brute_force(graph, start_city)
    print("Shortest Path:", path)
    print("Minimum Cost:", cost)
