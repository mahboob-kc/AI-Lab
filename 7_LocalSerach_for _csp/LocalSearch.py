#local search for csp


import random

def get_neighbors(state, graph):
    """Generate neighboring states by changing the color of one node."""
    neighbors = []
    for node in graph.keys():
        for color in colors:
            if state[node] != color:
                neighbor = state.copy()
                neighbor[node] = color
                neighbors.append(neighbor)
    return neighbors

def count_conflicts(state, graph):
    """Count the number of conflicting edges in the current state."""
    conflicts = 0
    for node in graph:
        for neighbor in graph[node]:
            if state[node] == state[neighbor]:
                conflicts += 1
    return conflicts

def hill_climbing(graph, colors):
    # Random initial state
    current_state = {node: random.choice(colors) for node in graph}
    
    print("Initial state:")
    print(current_state)
    
    current_conflicts = count_conflicts(current_state, graph)
    print(f"Initial conflicts: {current_conflicts}\n")
    
    while True:
        neighbors = get_neighbors(current_state, graph)
        neighbor_conflicts = [(neighbor, count_conflicts(neighbor, graph)) for neighbor in neighbors]
        
        # Choose the neighbor with the fewest conflicts
        best_neighbor, best_conflicts = min(neighbor_conflicts, key=lambda x: x[1])
        
        # If the best neighbor has fewer conflicts, move to it
        if best_conflicts < current_conflicts:
            current_state = best_neighbor
            current_conflicts = best_conflicts
            print(f"Current state: {current_state}")
            print(f"Conflicts: {current_conflicts}\n")
        else:
            # If no better neighbor is found, stop
            break

    return current_state, current_conflicts

# Input the graph
n = int(input("Enter number of nodes: "))
graph = {}
for i in range(n):
    node = input(f"Enter name of node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (comma-separated): ").split(',')
    graph[node] = neighbors

# Input the available colors
colors = input("Enter available colors (comma-separated): ").split(',')

# Run hill climbing
final_state, final_conflicts = hill_climbing(graph, colors)

print("Final state:")
print(final_state)
print(f"Final conflicts: {final_conflicts}")
