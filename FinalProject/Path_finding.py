import math


class Node:

    def __init__(self, index=None, parent=None):

        self.index = index
        self.parent = parent

        self.f = 0
        self.g = 0
        self.h = 0

    def __eq__(self, other):
        return self.index == other.index

    def __lt__(self, other):

        return self.f < other.f


def shortest_path(map, start, goal):

    if start not in map["intersections"] or goal not in map["intersections"]:

        return False

    unvisited_nodes = []
    visited_nodes = []

    start_node = Node(index=start)
    unvisited_nodes.append(start_node)

    goal_node = Node(index=goal)

    while unvisited_nodes:

        unvisited_nodes.sort()

        # Return the node with the lowest f value
        current_node = unvisited_nodes.pop(0)

        if current_node in visited_nodes:
            continue

        visited_nodes.append(current_node)

        if current_node == goal_node:
            path = []
            current = current_node

            while current:
                path.append(current.index)
                current = current.parent

            return path[::-1]

        # Generate children of a given node

        children = []

        for connect_index in map["roads"][current_node.index]:

            new_node = Node(parent=current_node, index=connect_index)
            children.append(new_node)

        # Loop through children

        for child in children:

            for node in visited_nodes:
                if child == node:
                    continue

            child.g = current_node.g + \
                calculate_distance(map, child.index, current_node.index)
            child.h = calculate_distance(map, child.index, goal_node.index)
            child.f = child.g + child.h

            for node in unvisited_nodes:
                if child.f > node.f:
                    continue

            unvisited_nodes.append(child)


def calculate_distance(map, point1, point2):

    return math.sqrt(math.pow(map["intersections"][point1][0] - map["intersections"][point2][0], 2) +
                     math.pow(map["intersections"][point1][1] - map["intersections"][point2][1], 2))


map = {}

map["intersections"] = {0: [0.7798606835438107, 0.6922727646627362],
                        1: [0.7647837074641568, 0.3252670836724646],
                        2: [0.7155217893995438, 0.20026498027300055],
                        3: [0.7076566826610747, 0.3278339270610988],
                        4: [0.8325506249953353, 0.02310946309985762],
                        5: [0.49016747075266875, 0.5464878695400415],
                        6: [0.8820353070895344, 0.6791919587749445],
                        7: [0.46247219371675075, 0.6258061621642713],
                        8: [0.11622158839385677, 0.11236327488812581],
                        9: [0.1285377678230034, 0.3285840695698353]}


map["roads"] = {0: [7, 6, 5],
                1: [4, 3, 2],
                2: [4, 3, 1],
                3: [5, 4, 1, 2],
                4: [1, 2, 3],
                5: [7, 0, 3],
                6: [0, 8],
                7: [0, 5],
                8: [6, 9],
                9: [8]}

start, goal = 1, 9


path = shortest_path(map, start, goal)
print(f"The path from {start} to {9} is: {path}")
