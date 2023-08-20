# Minimum Spanning Tree
from UnionFind import UnionFind


# Kruscal's Algorithm
def mst_Kruskal(n, edges):
    uf = UnionFind(n)
    sorted_edges = sorted(edges, key=lambda x:x[2])
    cost = 0
    selected_edges = []

    for edge in sorted_edges:
        if uf.connect(edge[0], edge[1]):
            cost += edge[2]
            selected_edges.append(edge)

        if uf.max_size == n:
            return cost, selected_edges

    return None


if __name__ == '__main__':
    n = 5
    edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
    cost, selected = mst_Kruskal(n, edges)
    print(cost)
    print(selected)
