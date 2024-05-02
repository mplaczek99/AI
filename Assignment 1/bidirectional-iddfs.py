import json

def load_graph(filename):
    """Load the graph from a JSON file"""
    with open(filename, 'r') as file:
        data = json.load(file)
    graph = {}

    for node in data['nodes']:
        graph[node['name']] = set()
    for arc in data['arcs']:
        graph[arc['first']].add(arc['second'])
        graph[arc['second']].add(arc['first']) # Assuming undirected graph
    return graph

def bidirectional_iddfs(graph, start, goal):
    """Perform a bidirectional Iterative Deepening Depth-First Search"""
    depth = 0
    total_call_count = 0 # Initialize call counter

    while True:
        visited_from_start = set()
        visited_from_goal = set()
        path_from_start = []
        path_from_goal = []

        # Perform two DLS from both directions
        found_from_start, count_from_start = dls(graph, start, goal, depth, visited_from_start, path_from_start, 0, forward=True)
        found_from_goal, count_from_goal = dls(graph, goal, start, depth, visited_from_goal, path_from_goal, 0, forward=False)

        total_call_count += (count_from_start + count_from_goal) # Aggregate the count of calls

        # Check if there is an intersection
        intersection = visited_from_start.intersection(visited_from_goal)
        if intersection:
            # Combine paths at the first common node
            common_node = intersection.pop()
            path_to_meet = path_from_start[:path_from_start.index(common_node) + 1]
            path_from_meet = path_from_goal[:path_from_goal.index(common_node)]

            return path_to_meet + path_from_meet[::-1], total_call_count

        if found_from_start and found_from_goal:
            return [], total_call_count  # One of the DLS found the goal, this shouldn't happen in a correct setup

        depth += 1

def dls(graph, node, goal, depth, visited, path, call_count, forward):
    """Depth-Limited Search (DLS) for bidirectional search"""
    call_count += 1

    if node == goal:
        path.append(node)
        return True, call_count
    if depth == 0:
        return False, call_count

    visited.add(node)
    path.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            found, call_count = dls(graph, neighbor, goal, depth - 1, visited, path, call_count, forward)
            if found:
                return True, call_count

    path.pop()
    visited.remove(node)

    return False, call_count

def main():
    graph = load_graph('ctaTrain.json')

    while True:
        start = input("1st name: (or \"quit\" to quit) ").strip()
        if start.lower() == 'quit':
            break
        end = input("2nd name: (or \"quit\" to quit) ").strip()
        if end.lower() == 'quit':
           break

        path, call_count = bidirectional_iddfs(graph, start, end)

        if path:
            print(" -> ".join(path))
            print(f"{call_count} calls") # Displays the number of calls
        else:
            print("No path found.")

if __name__ == '__main__':
    main()
