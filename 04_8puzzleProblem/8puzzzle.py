import numpy as np
import pprint

class Node:
    def __init__(self, state, parent, move, misplaced):
        self.state = state
        self.parent = parent
        self.move = move
        self.misplaced = misplaced

def misplaced_tiles(state, goal):
    """Calculate the number of misplaced tiles compared to the goal state."""
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

def get_neighbors(state):
    """Generate possible moves from the current state by moving the empty space (0)."""
    neighbors = []
    zero_index = state.index(0)
    row, col = divmod(zero_index, 3)

    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

    for move, (dr, dc) in directions.items():
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero_index = new_row * 3 + new_col
            new_state = list(state)
            # Swap the empty space with the adjacent tile
            new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]
            neighbors.append((new_state, move))

    return neighbors

def bfs(initial, goal):
    """Breadth-first search for solving the 8-puzzle problem."""
    frontier = [Node(initial, None, None, misplaced_tiles(initial, goal))]
    explored = set()

    while frontier:
        # Sort the frontier by the number of misplaced tiles (least first)
        frontier.sort(key=lambda node: node.misplaced)

        node = frontier.pop(0)

        if node.state == goal:
            return reconstruct_path(node)

        explored.add(tuple(node.state))

        for neighbor_state, move in get_neighbors(node.state):
            if tuple(neighbor_state) not in explored:
                neighbor_node = Node(neighbor_state, node, move, misplaced_tiles(neighbor_state, goal))
                frontier.append(neighbor_node)

    return None

def reconstruct_path(node):
    """Reconstruct the path from the start state to the goal state."""
    path = []
    actions = []
    while node.parent is not None:
        path.append(np.array(node.parent.state).reshape(3, 3))
        actions.append(node.move)
        node = node.parent
    path.reverse()
    actions.reverse()
    return actions, path

def input_state(prompt):
    """Helper function to input a puzzle state from the user."""
    print(prompt)
    state = []
    for i in range(3):
        row = input(f"Enter row {i + 1} (space-separated): ").split()
        state.extend(int(x) for x in row)
    return state

def main():
    initial_state = input_state("Enter the initial state: ")
    goal_state = input_state("Enter the goal state: ")

    actions, path = bfs(initial_state, goal_state)

    if actions:
        print("Path found:")
        pprint.pprint(path)
        print("Actions taken:", actions)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
