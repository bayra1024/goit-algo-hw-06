import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])]

    while stack:
        current_vertex, path = stack.pop()

        if current_vertex == goal:
            return path

        visited.add(current_vertex)

        for edge in graph.edges(current_vertex):
            neighbor = edge[1]
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return []


def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_vertex, path = queue.popleft()

        if current_vertex == goal:
            return path

        visited.add(current_vertex)

        for edge in graph.edges(current_vertex):
            neighbor = edge[1]
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return []


# Створення графа
G = nx.DiGraph()

for i in range(1, 16):
    G.add_node(i)

edges = [
    (1, 2, {"weight": 2}),
    (1, 3, {"weight": 3}),
    (2, 4, {"weight": 4}),
    (2, 5, {"weight": 5}),
    (3, 6, {"weight": 6}),
    (3, 7, {"weight": 7}),
    (4, 8, {"weight": 8}),
    (4, 9, {"weight": 9}),
    (5, 10, {"weight": 10}),
    (5, 11, {"weight": 11}),
    (6, 12, {"weight": 12}),
    (6, 13, {"weight": 13}),
    (7, 14, {"weight": 14}),
    (7, 15, {"weight": 15}),
    (1, 4, {"weight": 3}),
    (1, 5, {"weight": 4}),
    (2, 6, {"weight": 6}),
    (2, 7, {"weight": 7}),
    (3, 8, {"weight": 9}),
    (3, 9, {"weight": 10}),
    (4, 10, {"weight": 12}),
    (4, 11, {"weight": 14}),
    (5, 12, {"weight": 16}),
    (5, 13, {"weight": 18}),
    (6, 14, {"weight": 20}),
    (6, 15, {"weight": 22}),
    (1, 8, {"weight": 5}),
    (2, 9, {"weight": 8}),
    (3, 10, {"weight": 11}),
    (4, 11, {"weight": 14}),
    (5, 12, {"weight": 16}),
    (6, 13, {"weight": 18}),
    (7, 14, {"weight": 20}),
    (7, 15, {"weight": 22}),
    (6, 10, {"weight": 30}),
    (4, 7, {"weight": 25}),
    (7, 11, {"weight": 35}),
    (7, 12, {"weight": 40}),
    (11, 14, {"weight": 45}),
    (11, 15, {"weight": 50}),
]

G.add_edges_from(edges)

pos = {
    1: (0, 0),
    2: (1, 1),
    3: (1, -1),
    4: (2, 2),
    5: (2, 0),
    6: (2, -2),
    7: (3, 1),
    8: (3, 3),
    9: (3, -1),
    10: (3, -3),
    11: (4, 0),
    12: (4, 2),
    13: (4, -2),
    14: (5, 1),
    15: (5, -1),
}

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=700,
    node_color="#ffff66",
    font_size=8,
    font_color="#ff00ff",
    font_weight="bold",
    edge_color="#00ff00",
    width=2,
    arrowsize=30,
)

print("\nDFS:", dfs(G, 1, 15))


print("\nBFS:", bfs(G, 1, 15))


nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()
