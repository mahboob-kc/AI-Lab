#Write  a program to implement state space search algorithm like BFS and DFS


from collections import deque

def bfs(start, graph):
    #Perform Breadth-First Search to explore the path from start.
    if start not in graph:
        return []
    
    visited = set()
    queue = deque([start])  # Queue holds nodes
    path = []  # List to store the order of nodes discovered
    
    while queue:
        node = queue.popleft()
        
        if node in visited:
            continue
        
        visited.add(node)
        path.append(node)
        
        # Explore neighbors of the current node
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)  # Add neighbor to the queue
    
    return path

def dfs(start, goal, graph, path=None):
    """Perform Depth-First Search to find a path from start to goal."""
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            new_path = dfs(node, goal, graph, path)
            if new_path:
                return new_path
    return None

def input_graph():
    #Function to input a directed graph from the user.
    graph = {}
    print("Enter the adjacency list for each node (type 'done' when finished):")
    
    while True:
        node = input("Enter node: ")
        if node.lower() == 'done':
            break
        neighbors = input(f"Enter neighbors of {node} (comma separated): ").split(',')
        graph[node] = [neighbor.strip() for neighbor in neighbors if neighbor.strip()]
    
    return graph

def main():
    graph = input_graph()
    
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    
    print(f"Graph: {graph}")
    
    dfs_path = dfs(start_node, goal_node, graph)
    bfs_path = bfs(start_node, graph)
    
    print(f"DFS path from {start_node} to {goal_node}: {dfs_path}")
    print(f"BFS exploration path from {start_node}: {bfs_path}")

if __name__ == "__main__":
    main()

