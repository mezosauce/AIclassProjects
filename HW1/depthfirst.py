from layout import Map

def depth_first_search(map_obj, start, goal):
    """
    Implements Depth First Search algorithm.
    
    Args:
        map_obj: Instance of Map class
        start: Start city name
        goal: Goal city name
        
    Returns:
        tuple: (path_list, nodes_expanded_count)
    """
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
    
    print("--- Depth First Search: Arad to Bucharest ---")
    start_city = "Arad"
    goal_city = "Bucharest"
    
    path, count = depth_first_search(romania_map, start_city, goal_city)
    print(f"Path: {path}")
    print(f"Nodes Expanded: {count}")
    
    print("\n--- Depth First Search: Sibiu to Mehadia ---")
    start_city = "Sibiu"
    goal_city = "Mehadia"
    
    path, count = depth_first_search(romania_map, start_city, goal_city)
    print(f"Path: {path}")
    print(f"Nodes Expanded: {count}")
