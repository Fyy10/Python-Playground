from typing import List


def floyd(graph: List[List[int]]) -> List[List[int]]:
    """
    graph: adjacent matrix
    """
    # dp[k][i][j]: min cost from i to j through 0, 1, ..., k
    # dp[-1][i][j] = graph[i][j]
    # dp[k][i][j] = min(dp[k-1][i][j], dp[k-1][i][k] + dp[k-1][k][j])
    # ans: dp[n-1][i][j]

    # note that dp[k-1][i][k] <= dp[k][i][k], and dp[k][i][k] <= dp[k-1][i][k]
    # therefore dp[k][i][k] == dp[k-1][i][k]
    # same for dp[k][k][j] == dp[k-1][k][j]
    # so we can update graph inplace
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph
