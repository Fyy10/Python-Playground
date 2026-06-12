# Templates

- [Templates](#templates)
  - [Graph Algorithms](#graph-algorithms)
  - [String Algorithms](#string-algorithms)
  - [Tree And Range Query Structures](#tree-and-range-query-structures)
  - [Linear Data Structures](#linear-data-structures)
  - [Selection Algorithms](#selection-algorithms)

Reusable Python templates for common data structures and algorithms.

## Graph Algorithms

| Template | Description |
| --- | --- |
| [`Dijkstra.py`](Dijkstra.py) | Single-source shortest paths for weighted graphs, with both enumeration and heap-based implementations. |
| [`Floyd.py`](Floyd.py) | Floyd-Warshall all-pairs shortest paths over an adjacency matrix. |
| [`mst.py`](mst.py) | Minimum spanning tree with Kruskal's algorithm. |
| [`topological_sort.py`](topological_sort.py) | Kahn-style topological sort for directed graphs, returning `None` when a valid ordering does not exist. |
| [`UnionFind.py`](UnionFind.py) | Disjoint set union with union by size, used by graph connectivity and Kruskal-style workflows. |

## String Algorithms

| Template | Description |
| --- | --- |
| [`Boyer-Moore.py`](Boyer-Moore.py) | Boyer-Moore substring search using the bad character rule. |
| [`KMP.py`](KMP.py) | Knuth-Morris-Pratt substring search with prefix table preprocessing. |
| [`Rabin-Karp.py`](Rabin-Karp.py) | Rabin-Karp substring search with rolling hash support. |
| [`Trie.py`](Trie.py) | Trie for word insertion, exact search, and prefix search. |

## Tree And Range Query Structures

| Template | Description |
| --- | --- |
| [`lca.py`](lca.py) | Lowest common ancestor in a binary tree. |
| [`morris_traversal.py`](morris_traversal.py) | Inorder Morris traversal with constant extra space. |
| [`segment_tree.py`](segment_tree.py) | Segment tree with configurable merge function, point updates, and range queries. |
| [`sparse_table.py`](sparse_table.py) | Sparse table for static range queries, including O(1) idempotent queries and O(log n) non-overlapping queries. |

## Linear Data Structures

| Template | Description |
| --- | --- |
| [`LRUCache.py`](LRUCache.py) | LRU cache implemented with a hash map and doubly linked list. |
| [`MinQueue.py`](MinQueue.py) | Queue with O(1) minimum lookup using a monotonic queue. |
| [`MinStack.py`](MinStack.py) | Stack with O(1) minimum lookup, including auxiliary-stack and difference-encoding variants. |
| [`PriorityQueue.py`](PriorityQueue.py) | Small wrapper around Python's `heapq` module. |

## Selection Algorithms

| Template | Description |
| --- | --- |
| [`quick_select.py`](quick_select.py) | Hoare-style quickselect for finding the k-th smallest element. |
