class UnionFind:
    def __init__(self, n):
        self.father = list(range(n))
        self.size = [1] * n
        self.n = n
        self.max_size = 1

    def check_index(self, i):
        if not 0 <= i < self.n:
            raise ValueError('index should be in the range [0, {}), but got {}'.format(self.n, i))

    def root(self, i):
        self.check_index(i)
        
        root_i = self.father[i]
        while self.father[root_i] != root_i:
            root_i = self.father[root_i]

        return root_i

    def connect(self, i, j):
        self.check_index(i)
        self.check_index(j)
        root_i = self.root(i)
        root_j = self.root(j)
        if root_i == root_j:
            return False

        if self.size[root_i] > self.size[root_j]:
            self.size[root_i] += self.size[root_j]
            self.father[root_j] = root_i
            self.max_size = self.size[root_i]
        else:
            self.size[root_j] += self.size[root_i]
            self.father[root_i] = root_j
            self.max_size = self.size[root_j]
        return True


if __name__ == '__main__':
    uf = UnionFind(10)
    uf.connect(0, 1)
    uf.connect(5, 6)
    print(uf.max_size)
