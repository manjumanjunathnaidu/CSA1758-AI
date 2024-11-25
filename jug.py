from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    """
    Solve the Water Jug problem using BFS.
    Args:
        jug1_capacity (int): Capacity of the first jug.
        jug2_capacity (int): Capacity of the second jug.
        target (int): Target amount of water.
    Returns:
        list: A list of steps to achieve the target, or an empty list if not possible.
    """
 
    visited = set()

    queue = deque([(0, 0)]) 
    parent = {}  
    while queue:
        current = queue.popleft()
        if current[0] == target or current[1] == target:
            path = []
            while current:
                path.append(current)
                current = parent.get(current)
            return path[::-1]
        if current in visited:
            continue
        visited.add(current)
        jug1, jug2 = current
        next_states = [
            (jug1_capacity, jug2),  
            (jug1, jug2_capacity),  
            (0, jug2),              
            (jug1, 0),              
            (max(jug1 - (jug2_capacity - jug2), 0),  
             min(jug2 + jug1, jug2_capacity)),
            (min(jug1 + jug2, jug1_capacity), 
             max(jug2 - (jug1_capacity - jug1), 0)),
        ]
        for state in next_states:
            if state not in visited:
                queue.append(state)
                parent[state] = current

    return []  

if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target = 2

    solution = water_jug_bfs(jug1_capacity, jug2_capacity, target)

    if solution:
        print("Steps to solve the Water Jug Problem:")
        for step in solution:
            print(step)
    else:
        print("No solution exists!")
