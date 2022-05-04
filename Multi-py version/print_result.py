def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
        
    # Add the start node manually
    path.append(int(start_node))

    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(path)
    
    return path, "{:.2f}".format(shortest_path[target_node])