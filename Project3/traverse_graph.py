from collections import deque

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', "F"]),
         'F': set(['C', "E"])}


# Depth first search - traverse a graph - iterative method
def dfs(graph, start):

    visited, stack = set(), deque([start])

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)

        stack.extend(graph[vertex] - visited)

    return visited

# Breadth first search - traverse a graph - iterative method


def bfs(graph, start):

    visited, queue = set(), deque(start)

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.add(vertex)
            print(vertex)

        queue.extend(graph[vertex] - visited)

    return visited

# # Recursive
# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()

#     if start not in visited:
#         visited.add(start)
#         print(start)
#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited


print("DFS order")
traverse_graph_dfs = dfs(graph, 'A')

print("BFS order")
traverse_graph_bfs = bfs(graph, 'A')
