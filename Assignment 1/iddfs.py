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

def iddfs(graph, start, goal):
    """Perform Iterative Deepening Depth-First Search (IDDFS)"""
    depth = 0
    call_count = 0 # Initialize call counter

    while True:
        visited = set()
        path = []
        found, count = dls(graph, start, goal, depth, visited, path, 0)
        call_count += count # Aggregate the count of calls

        if found:
            return path, call_count

        depth += 1

def dls(graph, node, goal, depth, visited, path, call_count):
    """Depth-Limited Search (DLS) with call counting"""
    call_count += 1 # Increment call count each time the function is called

    if node == goal: # Base Case
        path.append(node)
        return True, call_count
    if depth == 0: # Also Base Case
        return False, call_count

    visited.add(node)
    path.append(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            found, call_count = dls(graph, neighbor, goal, depth - 1, visited, path, call_count) # Recursion
            if found:
                return True, call_count

    path.pop() # No need to keep these
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

        path, call_count = iddfs(graph, start, end)

        if path:
            print(" -> ".join(path))
            print(f"{call_count} calls") # Displays the number of calls
        else:
            print("No path found.")

if __name__ == "__main__":
    """I heard keeping this is good practice in Python"""
    main()
