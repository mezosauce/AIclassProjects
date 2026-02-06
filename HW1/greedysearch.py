import heapq
from layout import Map

from A_star import Node


def greedy_search(graph, start, goal, heuristic_fn="lower"):

    open_list = []

    if heuristic_fn == "upper":
        start_h = graph.estimate_upper_bound(start, goal)
    else:
        start_h = graph.estimate_lower_bound(start, goal)

    start_node = Node(start, None, 0, start_h)

    heapq.heappush(open_list, start_node)
    visted = set()

    # Keep track of best g-score to allow re-discovery of better paths if necessary
    g_scores = {start: 0}
    
    nodes_expanded = 0
    
    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.city in visted:
            continue
            
        nodes_expanded += 1
        visted.add(current_node.city)
        
        if current_node.city == goal:
            path = []
            while current_node:
                path.append(current_node.city)
                current_node = current_node.parent
            return path[::-1], nodes_expanded

        for neighbor, distance in graph.get_neighbors(current_node.city):
            g = current_node.g + distance

            if neighbor in g_scores and g >= g_scores[neighbor]:
                continue

            g_scores[neighbor] = g
            
            if heuristic_fn == "upper":
                h = graph.estimate_upper_bound(neighbor, goal)
            else:
                h = graph.estimate_lower_bound(neighbor, goal)

            neighbor_node = Node(neighbor, current_node, g, h)
            heapq.heappush(open_list, neighbor_node)
                                          
    return None, nodes_expanded
    
if __name__ == "__main__":
    romania_map = Map()

    # Store results for table
    results = []

    # Test Case 1: Arad to Bucharest
    print("--- Test Case 1: Arad to Bucharest ---")
    start_city = "Arad"
    goal_city = "Bucharest"

    # Method 1: Lower Bound (Admissible)
    print("Method 1: Lower Bound (Admissible):")
    path_lower, nodes_lower = greedy_search(romania_map, start_city, goal_city, heuristic_fn="lower")
    print(f"Path: {path_lower}")
    print(f"Nodes expanded: {nodes_lower}")
    
    # Calculate path cost
    cost_lower = 0
    if path_lower:
        for i in range(len(path_lower) - 1):
            distance = romania_map.get_distance(path_lower[i], path_lower[i+1])
            if distance:
                cost_lower += distance
    
    results.append({
        'test_case': 'Arad → Bucharest',
        'method': 'Lower Bound',
        'path': ' → '.join(path_lower) if path_lower else 'No path',
        'cost': cost_lower,
        'nodes': nodes_lower
    })

    # Method 2: Upper Bound (Non-Admissible)
    print("\nMethod 2: Upper Bound (Non-Admissible):")
    path_upper, nodes_upper = greedy_search(romania_map, start_city, goal_city, heuristic_fn="upper")
    print(f"Path: {path_upper}")
    print(f"Nodes expanded: {nodes_upper}")
    
    # Calculate path cost
    cost_upper = 0
    if path_upper:
        for i in range(len(path_upper) - 1):
            distance = romania_map.get_distance(path_upper[i], path_upper[i+1])
            if distance:
                cost_upper += distance
    
    results.append({
        'test_case': 'Arad → Bucharest',
        'method': 'Upper Bound',
        'path': ' → '.join(path_upper) if path_upper else 'No path',
        'cost': cost_upper,
        'nodes': nodes_upper
    })

    # Test Case 2: Sibiu to Mehadia
    print("\n--- Test Case 2: Sibiu to Mehadia ---")
    start_city = "Sibiu"
    goal_city = "Mehadia"

    # Method 1: Lower Bound (Admissible)
    print("Method 1: Lower Bound (Admissible):")
    path_lower, nodes_lower = greedy_search(romania_map, start_city, goal_city, heuristic_fn="lower")
    print(f"Path: {path_lower}")
    print(f"Nodes expanded: {nodes_lower}")
    
    # Calculate path cost
    cost_lower = 0
    if path_lower:
        for i in range(len(path_lower) - 1):
            distance = romania_map.get_distance(path_lower[i], path_lower[i+1])
            if distance:
                cost_lower += distance
    
    results.append({
        'test_case': 'Sibiu → Mehadia',
        'method': 'Lower Bound',
        'path': ' → '.join(path_lower) if path_lower else 'No path',
        'cost': cost_lower,
        'nodes': nodes_lower
    })

    # Method 2: Upper Bound (Non-Admissible)
    print("\nMethod 2: Upper Bound (Non-Admissible):")
    path_upper, nodes_upper = greedy_search(romania_map, start_city, goal_city, heuristic_fn="upper")
    print(f"Path: {path_upper}")
    print(f"Nodes expanded: {nodes_upper}")
    
    # Calculate path cost
    cost_upper = 0
    if path_upper:
        for i in range(len(path_upper) - 1):
            distance = romania_map.get_distance(path_upper[i], path_upper[i+1])
            if distance:
                cost_upper += distance
    
    results.append({
        'test_case': 'Sibiu → Mehadia',
        'method': 'Upper Bound',
        'path': ' → '.join(path_upper) if path_upper else 'No path',
        'cost': cost_upper,
        'nodes': nodes_upper
    })

    # Print results table
    print("\n" + "="*100)
    print("GREEDY SEARCH RESULTS SUMMARY")
    print("="*100)
    print(f"{'Test Case':<25} {'Heuristic':<15} {'Path Cost':<12} {'Nodes Expanded':<18} {'Path'}")
    print("-"*100)
    
    for result in results:
        print(f"{result['test_case']:<25} {result['method']:<15} {result['cost']:<12} {result['nodes']:<18} {result['path']}")
    
    print("="*100)