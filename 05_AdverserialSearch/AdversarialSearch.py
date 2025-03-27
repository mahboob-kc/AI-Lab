def create_tree():
    tree = {}
    n = int(input("Enter the number of non-leaf nodes: "))
    for _ in range(n):
        node = input("Enter the name of non-leaf node: ")
        children = input(f"Enter the children of {node}: ").split()
        tree[node] = children

    m = int(input("Enter the number of leaf nodes: "))
    for _ in range(m):
        leaf = input('Enter the name of leaf node: ')
        value = int(input(f'Enter the value of {leaf} node :'))
        tree[leaf] = value
  
    return tree

def minmax(node,tree,ismaximizing):
    if isinstance(tree[node],int):
        print(f"Tree Node {node} with value {tree[node]}")
        return tree[node],[node]
    print(f'Exploring Node {node}')

    if ismaximizing:
        best_value = float('-inf')
        best_path = []

        for child in tree[node]:
            value , path = minmax(child,tree,False)
            if value > best_value:
                best_value = value
                best_path = [node] + path
    else:
        best_value = float('inf')
        best_path = []
        for child in tree[node]:
            value , path = minmax(child,tree,True)
            if value<best_value:
                best_value = value
                best_path = [node] + path
    
    print(f'Node {node} has value {best_value}')
    return best_value,best_path

tree = create_tree()
root = input('Enter Root node :')
print("\n\nMIN-MAX\n")
best_value , best_node = minmax(root,tree,True)

print("BEST VALUE: ",best_value,"\nBEST PATH :",best_node)
print("\n\nAlpha-beta\n")
def pruning(node, tree, alpha, beta, ismaximizing, pruned_nodes=None):
    if pruned_nodes is None:
        pruned_nodes = []

    if isinstance(tree[node], int):
        print(f"Tree Node {node} with value {tree[node]}")
        return tree[node], [node], pruned_nodes
    
    if ismaximizing:
        best_value = float('-inf')
        best_path = []
        for child in tree[node]:
            value, path, pruned_nodes = pruning(child, tree, alpha, beta, False, pruned_nodes)
            if value > best_value:
                best_value = value
                best_path = path
            alpha = max(alpha, best_value)
            if beta <= alpha:
                pruned_nodes.extend(tree[node][tree[node].index(child)+1:])
                print(f"Pruning at node {node} during maximizing with alpha={alpha} and beta={beta}")
                break
        return best_value, [node] + best_path, pruned_nodes
    else:
        best_value = float('inf')
        best_path = []
        for child in tree[node]:
            value, path, pruned_nodes = pruning(child, tree, alpha, beta, True, pruned_nodes)
            if value < best_value:
                best_value = value
                best_path = path
            beta = min(beta, best_value)
            if beta <= alpha:
                pruned_nodes.extend(tree[node][tree[node].index(child)+1:])
                print(f"Pruning at node {node} during minimizing with alpha={alpha} and beta={beta}")
                break
        return best_value, [node] + best_path, pruned_nodes

best_value, best_path, pruned_nodes = pruning(root, tree, float('-inf'), float('inf'), True)
print(f"Best value: {best_value}")
print(f"Best path: {best_path}")
print(f"Pruned nodes: {pruned_nodes}")
