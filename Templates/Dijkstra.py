import heapq
import math
from typing import List


def dijkstra_enum(graph: List[List[int]], n: int, start: int) -> List[int]:
    """
    n nodes: 0, 1, 2, ..., n-1
    m edges: len(graph)
    weight of u -> v: graph[u][v]
    Time complexity: O(n^2)
    Space complexity: O(n^2) (with adjacent matrix)
    """
    # dist[node]: min dist from start to node
    dist = [math.inf] * n
    dist[start] = 0
    # when dist[node] is optimal, mark node as visited
    visited = [False] * n

    # at most n steps needed
    for _ in range(n):
        # find an unvisited node with the minimum dist[node]
        min_node = -1
        min_dist = math.inf
        for node in range(n):
            if not visited[node] and dist[node] < min_dist:
                min_node = node
                min_dist = dist[node]

        # all nodes are visited, problem solved
        if min_node < 0:
            break

        # the node with min dist[node] is considered optimal
        visited[min_node] = True
        # update dist for node's neighbors
        for nxt, w in graph[min_node]:
            nxt_dist = min_dist + w
            if nxt_dist < dist[nxt]:
                dist[nxt] = nxt_dist

    return dist


def dijkstra_heap(graph: List[List[int]], n: int, start: int) -> List[int]:
    """
    n nodes: 0, 1, 2, ..., n-1
    m edges: len(graph)
    weight of u -> v: graph[u][v]
    Time complexity: O(m log m)
    Space complexity: O(m) (with adjacent list)
    """
    # dist[node]: min dist from start to node
    dist = [math.inf] * n
    dist[start] = 0
    # min heap stores (min_dist, node)
    # there may by multiple nodes with different min_dist exist in heap simultaneously
    # only the smallest min_dist is optimal
    heap = [(0, start)]

    while heap:
        # get an node with min curr_dist, note that curr_dist may be outdated
        curr_dist, node = heapq.heappop(heap)

        if curr_dist > dist[node]:
            # curr_dist is not optimal, skip
            continue

        # for all the neighbors, if a smaller dist[nxt] is found, add it to heap
        for nxt, w in graph[node]:
            nxt_dist = curr_dist + w
            if nxt_dist < dist[nxt]:
                dist[nxt] = nxt_dist
                heapq.heappush(heap, (nxt_dist, nxt))

    return dist
