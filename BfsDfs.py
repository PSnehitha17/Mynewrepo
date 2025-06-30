from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node] - visited)

    return result

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]

    for neighbor in graph[start] - visited:
        result.extend(dfs(graph, neighbor, visited))

    return result


def create_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))

    for _ in range(num_nodes):
        node = input("Enter node: ")
        neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
        graph[node] = set(neighbors)

    return graph

graph = create_graph()
start_node = input("Enter the starting node: ")

print("BFS Traversal:", bfs(graph, start_node))
print("DFS Traversal:", dfs(graph, start_node))
