#tarvelling salesman



from itertools import permutations

def total_distance(graph, path):
    total_dist = 0
    for i in range(len(path) - 1):
        total_dist += graph[path[i]][path[i + 1]]
    total_dist += graph[path[-1]][path[0]]  
    return total_dist

def travelling_salesman(graph, start, city_names):
    cities = list(range(len(graph)))
    cities.remove(start)
    min_path = None
    min_distance = float('inf')
    for perm in permutations(cities):
        current_path = [start] + list(perm)
        current_distance = total_distance(graph, current_path)
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = current_path
    min_path.append(start)
    min_path_names = [city_names[i] for i in min_path]  
    return min_path_names, min_distance

def main():
    n = int(input("Enter the number of cities: "))
    city_names = []
    for i in range(n):
        city_name = input(f"Enter the name of city {i + 1}: ")
        city_names.append(city_name)
    graph = []
    print("\nEnter the distance matrix (use 0 for the distance between a city and itself):")
    for i in range(n):
        row = list(map(int, input(f"Enter distances from {city_names[i]} to other cities: ").split()))
        graph.append(row)
    start_city = input("\nEnter the starting city: ")
    start = city_names.index(start_city)
    min_path, min_distance = travelling_salesman(graph, start, city_names)
    print("\nMinimum distance:", min_distance)
    print("Optimal path:", " -> ".join(min_path))

main()

