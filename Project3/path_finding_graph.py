from collections import deque

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', "F"]),
         'F': set(['C', "E"])}


def dfs_paths(graph, start, goal):

    stack = deque([([start], start)])

    while stack:

        path, vertex = stack.pop()

        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((path + [next], next))


print(list(dfs_paths(graph, 'A', 'F')))


def bfs_paths(graph, start, goal):

    queue = deque([([start], start)])

    while queue:

        path, vertex = queue.popleft()

        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((path + [next], next))


print(list(bfs_paths(graph, 'A', 'F')))
