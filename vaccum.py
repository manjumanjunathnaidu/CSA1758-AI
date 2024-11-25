def vacuum_cleaner_problem(environment, initial_position):
    """
    Simulate the Vacuum Cleaner Problem.
    
    Args:
        environment (dict): A dictionary representing the rooms and their states ('clean' or 'dirty').
        initial_position (str): The initial position of the vacuum cleaner.

    Returns:
        list: A sequence of actions taken by the vacuum cleaner.
    """
    actions = []  # List to store actions taken by the vacuum cleaner
    position = initial_position  # Starting position of the vacuum cleaner

    while any(state == 'dirty' for state in environment.values()):
        # Check the current room's state
        if environment[position] == 'dirty':
            actions.append(f"Clean {position}")
            environment[position] = 'clean'
        else:
            actions.append(f"{position} is already clean")

        # Determine the next move
        room_names = list(environment.keys())
        current_index = room_names.index(position)

        if current_index < len(room_names) - 1:
            # Move right if not at the last room
            position = room_names[current_index + 1]
            actions.append(f"Move to {position}")
        elif current_index == len(room_names) - 1:
            # Go back to the first room if at the last room
            position = room_names[0]
            actions.append(f"Move to {position}")

    return actions

# Example environment
environment = {
    'Room A': 'dirty',
    'Room B': 'clean',
    'Room C': 'dirty'
}

# Starting position
initial_position = 'Room A'

# Run the vacuum cleaner simulation
actions_taken = vacuum_cleaner_problem(environment, initial_position)

# Output the results
print("Actions Taken:")
for action in actions_taken:
    print(action)

print("\nFinal Environment State:")
print(environment)
