from queue import PriorityQueue

def a_star_search(graph, heuristics, start, goal):

    open_list = PriorityQueue()
    open_list.put((0, start))
    came_from = {} 
    g_cost = {start: 0}  

    while not open_list.empty():
        _, current = open_list.get()  

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_cost[goal]


        for neighbor, cost in graph[current]:
            tentative_g_cost = g_cost[current] + cost


            if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristics[neighbor]
                open_list.put((f_cost, neighbor))
                came_from[neighbor] = current


    return None, float('inf')


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2), ('E', 1)],
    'E': [('B', 5), ('D', 1), ('G', 2)],
    'F': [('C', 3), ('G', 1)],
    'G': [('E', 2), ('F', 1)]
}

heuristics = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 4,
    'E': 3,
    'F': 1,
    'G': 0  
}


start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

path, cost = a_star_search(graph, heuristics, start, goal)

if path:
    print("\nPath found:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("No path found from", start, "to", goal)
