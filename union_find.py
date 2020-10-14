class UnionFind:
    def __init__(self, n):
        self.n = n
        self.root = [i for i in range(n)]
        self.size = [1] * n
    
    def unite(self, x, y):
        if self.is_same(x, y):
            return
        x = self.parent(x)
        y = self.parent(y)
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.size[x] += self.size[y]
        self.root[y] = x 

    def parent(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def is_same(self, x, y):
        if self.parent(x) == self.parent(y):
            return True
        else:
            return False

    def roots(self):
        return [self.parent(i) for i in range(self.n)]

    def size_list(self):
        return [self.size[self.parent(i)] for i in range(self.n)]


if __name__ == "__main__":
    group = [2, 1, 4, 5, 8, 10, 3, 7, 6, 9]
    uf = UnionFind(len(group))
    for i in range(len(group)):
        uf.unite(i, group[i] − 1)
    print(uf.roots())
