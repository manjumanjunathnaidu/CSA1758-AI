import math

# Define a simple tree structure for testing
class GameNode:
    def __init__(self, value=None, children=None):
        self.value = value  # None for non-leaf nodes
        self.children = children if children else []
    
    def is_terminal(self):
        # A node is terminal if it has no children
        return not self.children
    
    def evaluate(self):
        # Return the value of the node if it's a leaf
        return self.value
    
    def get_children(self):
        # Return the children of the node
        return self.children

# Function to implement Alpha-Beta Pruning
def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate()

    if maximizing_player:
        max_eval = -math.inf
        for child in node.get_children():
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = math.inf
        for child in node.get_children():
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval

# Gather input values from the user for the leaf nodes
print("Please enter values for the leaf nodes in a binary tree of depth 3:")

leaf_values = []
for i in range(4):
    value = int(input(f"Enter value for leaf node {i+1}: "))
    leaf_values.append(GameNode(value))

# Gather input values from the user for the intermediate nodes
print("Please enter values for the intermediate nodes (left and right of the root):")
left_value = int(input("Enter value for the left intermediate node: "))
right_value = int(input("Enter value for the right intermediate node: "))

# Create the intermediate nodes
left_child = GameNode(left_value, children=[leaf_values[0], leaf_values[1]])
right_child = GameNode(right_value, children=[leaf_values[2], leaf_values[3]])

# Gather input value from the user for the root node
print("Please enter value for the root node:")
root_value = int(input("Enter value for the root node: "))

# Create the root node
root = GameNode(root_value, children=[left_child, right_child])

# Run Alpha-Beta Pruning
optimal_value = alpha_beta_pruning(root, depth=3, alpha=-math.inf, beta=math.inf, maximizing_player=True)
print("Optimal Value:", optimal_value)
