"""
# Floyd-Warshall Algorithm

Given a directed or an undirected weighted graph G with n vertices.
The task is to find the length of the shortest path d[i][j] between each pair of vertices i and j.

The graph may have negative weight edges, but no negative weight cycles.

This algorithm can also be used to detect the presence of negative cycles.
The graph has a negative cycle if at the end of the algorithm,
the distance from a vertex v to itself is negative.

# Description of the Algorithm

Before kth phase, d[i][j] stores the length of the shortest path between i and j,
which contains only the vertices {1, 2, ..., k-1} as internal vertices in the path.
i.e. d[i][j] is equal to the length of the shortest path from i to j,
if this path is allowed to enter only the vertex with numbers smaller than k
(the beginning and end of the path are not restricted by this property).

For k = 0, d[i][j] = w[i][j], or infinity if there is no edge between i and j.

If the shorter path passes through the k, then we can split the shortest path between i and j into two paths:
the path between i and k, and the path between k and j.
Both paths only use internal vertices of {1, 2, ..., k-1},
so we already have computed the lengths of those paths before.

We obtain:
# d[i][j] = min(d[i][j], d[i][k] + d[k][j])

In kth phase, iterate over all pairs of vertices and recalculate d[i][j]

Time Complexity: O(n^3)
"""

from typing import List

def floyd_warshall(adj: List[List[int]], eps: float = 0) -> List[List[int]]:
  INF = float('inf')
  n = len(adj)
  d = [[INF] * n for _ in range(n)]

  for i in range(n):
    for j in adj[i]:
      d[i][j] = adj[i][j]

  for k in range(n):
    for i in range(n):
      for j in range(n):
        # Handles negative and float weights
        if d[i][k] < INF and d[k][j] < INF and d[i][k] + d[k][j] < d[i][j] - eps:
          d[i][j] = d[i][k] + d[k][j]

  return d
