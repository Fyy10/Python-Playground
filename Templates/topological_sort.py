from collections import deque

def topological_sort(n, edges):
    """
    Args:
        n: num of nodes
        edges: list of [node_from, node_to]
    Returns:
        result: sorted list of nodes, return None if there is no valid sort
    """

    result = []
    # in_degree[i]: num of edges that point to node i
    in_degree = [0] * n
    # next_nodes[i]: the nodes that node i points to
    next_nodes = [[] for _ in range(n)]

    for e in edges:
        in_degree[e[1]] += 1
        next_nodes[e[0]].append(e[1])

    nodes = deque()
    for i in range(n):
        if in_degree[i] == 0:
            nodes.append(i)

    num_visited = 0
    while nodes:
        node = nodes.popleft()
        result.append(node)
        num_visited += 1
        for next_node in next_nodes[node]:
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                nodes.append(next_node)

    if num_visited != n:
        return None
    return result


if __name__ == '__main__':
    n = 5
    edges = [[4, 1], [4, 2], [1, 3], [2, 3]]
    print(topological_sort(n, edges))
