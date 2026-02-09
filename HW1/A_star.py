import heapq
from layout import Map, Node



def a_star_search(map_obj, start, goal, heuristic_method="lower"):
    # Priority Queue
    open_list = []

    # Determine heuristic function
    if heuristic_method == "upper":
        h_start = map_obj.estimate_upper_bound(start, goal)
    else:
        h_start = map_obj.estimate_lower_bound(start, goal)

    start_node = Node(start, None, 0, h_start)
    heapq.heappush(open_list, start_node)

    # Keep track of visited cities to avoid cycles and redundant work
    visited = set()

    # Keep track of best g-score to allow re-discovery of better paths if necessary
    # (Though with consistent heuristics, the first expansion is optimal)
    g_scores = {start: 0}

    nodes_expanded = 0

    while open_list:
        current_node = heapq.heappop(open_list)

        # If we've already processed this node with a better or equal g, skip
        if current_node.city in visited:
            continue

        nodes_expanded += 1
        visited.add(current_node.city)

        # Check goal
        if current_node.city == goal:
            path = []
            while current_node:
                path.append(current_node.city)
                current_node = current_node.parent
            return path[::-1], nodes_expanded

        # Expand neighbors
        neighbors = map_obj.get_neighbors(current_node.city)
        for neighbor_city, distance in neighbors:
            tentative_g = current_node.g + distance

            # If we found a shorter path to neighbor, or haven't seen it yet
            if neighbor_city not in g_scores or tentative_g < g_scores[neighbor_city]:
                g_scores[neighbor_city] = tentative_g

                if heuristic_method == "upper":
                    h = map_obj.estimate_upper_bound(neighbor_city, goal)
                else:
                    h = map_obj.estimate_lower_bound(neighbor_city, goal)

                new_node = Node(neighbor_city, current_node, tentative_g, h)
                heapq.heappush(open_list, new_node)

    return None, nodes_expanded


if __name__ == "__main__":
    romania_map = Map()

    # Store results for table
    results = []

    test_configs = [
        ("Arad", "Bucharest"),
        ("Sibiu", "Mehadia"),
        ("Oradea", "Eforie"),
        ("Timisoara", "Giurgiu"),
        ("Neamt", "Drobeta")
    ]

    print("--- A* Search Testing ---")

    for start_city, goal_city in test_configs:
        for method in ["lower", "upper"]:
            path, nodes = a_star_search(romania_map, start_city, goal_city, method)
            
            # Calculate path cost
            cost = 0
            if path:
                for i in range(len(path) - 1):
                    distance = romania_map.get_distance(path[i], path[i+1])
                    if distance:
                        cost += distance
            
            results.append({
                'test_case': f'{start_city} → {goal_city}',
                'method': method.capitalize() + " Bound",
                'path': ' → '.join(path) if path else 'No path',
                'cost': cost,
                'nodes': nodes
            })

    # Print results table
    print("\n" + "="*100)
    print("A* SEARCH RESULTS SUMMARY")
    print("="*100)
    print(f"{'Test Case':<25} {'Heuristic':<15} {'Path Cost':<12} {'Nodes Expanded':<18} {'Path'}")
    print("-"*100)
    
    for result in results:
        print(f"{result['test_case']:<25} {result['method']:<15} {result['cost']:<12} {result['nodes']:<18} {result['path']}")
    
    print("="*100)
