import sys
MOD = 1_000_000_007

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.sz = [1] * n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if self.sz[a] < self.sz[b]:
            a, b = b, a
        self.p[b] = a
        self.sz[a] += self.sz[b]

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n, m, k = next(it), next(it), next(it)
    c = [next(it) for _ in range(n)]
    groups = {}
    for _ in range(m):
        u, v = next(it) - 1, next(it) - 1
        x = c[u] ^ c[v]
        groups.setdefault(x, []).append((u, v))

    # For a fixed virus mask x, precisely the edges with c[u]^c[v] == x
    # constrain their endpoints to have equal infection status.
    # The number of valid subsets is 2^(number of DSU components).
    total_masks = 1 << k
    answer = ((total_masks - len(groups)) % MOD) * pow(2, n, MOD)
    answer %= MOD
    for edges in groups.values():
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)
        components = sum(1 for i in range(n) if dsu.find(i) == i)
        answer = (answer + pow(2, components, MOD)) % MOD
    print(answer)

if __name__ == "__main__":
    main()
