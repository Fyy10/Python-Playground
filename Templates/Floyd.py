from typing import List


def floyd(graph: List[List[int]]) -> List[List[int]]:
    """
    graph: adjacent matrix
    """
    n = len(graph)
    for k in range(1, n + 1):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k - 1] + graph[k - 1][j])
    return graph
