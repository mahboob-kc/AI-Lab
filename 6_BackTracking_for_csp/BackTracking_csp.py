def map_coloring(graph, colors, color_to_node):

    if all(node in color_to_node for node in graph):
        return True  # All nodes have been colored

    for color in colors:
        node = next(node for node in graph if node not in color_to_node)
        if is_valid_color(graph, node, color, color_to_node):
            color_to_node[node] = color
            if map_coloring(graph, colors, color_to_node):
                return True
            color_to_node.pop(node)  # Backtrack
    return False

def is_valid_color(graph, node, color, color_to_node):
    
    for neighbor in graph[node]:
        if neighbor in color_to_node and color_to_node[neighbor] == color:
            return False
    return True

graph={}

n=int(input("Enter the number of nodes :"))

for i in range(n):
    name=input("Enter the name of the node :").upper()
    graph[name]=input("Enter the neighbours with space :").upper().split()

colors = ["Red", "Green", "Blue"]

color_to_node = {}
if map_coloring(graph, colors, color_to_node):
    print("A valid coloring is found:")
    for node, color in color_to_node.items():
        print(f"{node}: {color}")
else:
    print("No valid coloring exists.")
