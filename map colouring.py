def is_safe(graph, color, node, color_assignment):
    for neighbor in graph[node]:
        if color_assignment[neighbor] == color:
            return False
    return True


def map_coloring(graph, num_colors, color_assignment, node):
    if node == len(graph): 
        return True
    
    for color in range(1, num_colors + 1):  
        if is_safe(graph, color, node, color_assignment):  
            color_assignment[node] = color  
            if map_coloring(graph, num_colors, color_assignment, node + 1):
                return True
            color_assignment[node] = 0 

    return False  


def main():
    num_regions = int(input("Enter the number of regions (nodes): "))
    
    graph = {i: [] for i in range(num_regions)}
    
    print("Enter adjacency list for the regions:")
    for i in range(num_regions):
        adjacents = input(f"Enter adjacent regions for region {i} : ").split(',')
        for adjacent in adjacents:
            if adjacent:
                graph[i].append(int(adjacent.strip()))

    num_colors = int(input("Enter the number of colors available: "))
    
    color_assignment = [0] * num_regions

    if map_coloring(graph, num_colors, color_assignment, 0):
        print("\nMap coloring solution:")
        for i in range(num_regions):
            print(f"Region {i} -> Color {color_assignment[i]}")
    else:
        print("\nNo solution found with the given number of colors.")

if __name__ == "__main__":
    main()
