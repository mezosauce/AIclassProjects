from layout import Map


def depth_first_search(map_obj, start, goal):
    # Stack stores (current_city, path_taken)
    stack = [(start, [start])]
    visited = set()
    nodes_expanded = 0

    while stack:
        current_city, path = stack.pop()

        if current_city in visited:
            continue

        nodes_expanded += 1
        visited.add(current_city)

        if current_city == goal:
            return path, nodes_expanded

        # Get neighbors and add to stack
        # To match the "first child" logic often used in DFS,
        # we can reverse the neighbors if we want to expand them in a specific order,
        # but standard DFS just pushes them onto the stack.
        neighbors = map_obj.get_neighbors(current_city)
        for neighbor_city, _ in reversed(neighbors):
            if neighbor_city not in visited:
                new_path = list(path)
                new_path.append(neighbor_city)
                stack.append((neighbor_city, new_path))

    return None, nodes_expanded


if __name__ == "__main__":
    romania_map = Map()

    # Store results for table
    results = []

    test_cases = [
        ("Arad", "Bucharest"),
        ("Sibiu", "Mehadia"),
        ("Oradea", "Eforie"),
        ("Timisoara", "Giurgiu"),
        ("Neamt", "Drobeta")
    ]

    print("--- Depth First Search Testing ---")

    for start_city, goal_city in test_cases:
        path, nodes = depth_first_search(romania_map, start_city, goal_city)
        
        # Calculate path cost
        cost = 0
        if path:
            for i in range(len(path) - 1):
                distance = romania_map.get_distance(path[i], path[i+1])
                if distance:
                    cost += distance
        
        results.append({
            'test_case': f'{start_city} → {goal_city}',
            'path': ' → '.join(path) if path else 'No path',
            'cost': cost,
            'nodes': nodes
        })

    # Print results table
    print("\n" + "="*100)
    print("DEPTH FIRST SEARCH RESULTS SUMMARY")
    print("="*100)
    print(f"{'Test Case':<25} {'Path Cost':<12} {'Nodes Expanded':<18} {'Path'}")
    print("-"*100)
    
    for result in results:
        print(f"{result['test_case']:<25} {result['cost']:<12} {result['nodes']:<18} {result['path']}")
    
    print("="*100)
