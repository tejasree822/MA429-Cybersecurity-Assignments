import sys

class RollbackParityDSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.parity = [0] * n
        self.bad = 0
        self.history = []

    def find(self, x):
        p = 0
        while self.parent[x] != x:
            p ^= self.parity[x]
            x = self.parent[x]
        return x, p

    def add_edge(self, u, v):
        ru, pu = self.find(u)
        rv, pv = self.find(v)
        if ru == rv:
            self.history.append((0, self.bad))
            if pu == pv:
                self.bad += 1
            return
        if self.size[ru] < self.size[rv]:
            ru, rv = rv, ru
            pu, pv = pv, pu
        self.history.append((1, rv, ru, self.size[ru], self.bad))
        self.parent[rv] = ru
        self.parity[rv] = pu ^ pv ^ 1
        self.size[ru] += self.size[rv]

    def snapshot(self):
        return len(self.history)

    def rollback(self, snap):
        while len(self.history) > snap:
            item = self.history.pop()
            if item[0] == 0:
                self.bad = item[1]
            else:
                _, child, root, old_size, old_bad = item
                self.parent[child] = child
                self.parity[child] = 0
                self.size[root] = old_size
                self.bad = old_bad

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = data[0], data[1]
    edges = {}
    intervals = []
    p = 2
    for t in range(q):
        u, v = data[p] - 1, data[p + 1] - 1
        p += 2
        if u > v:
            u, v = v, u
        edge = (u, v)
        if edge in edges:
            start = edges.pop(edge)
            if start < t:
                intervals.append((start, t, edge))
        else:
            edges[edge] = t
    for edge, start in edges.items():
        intervals.append((start, q, edge))

    size = 1
    while size < q:
        size <<= 1
    seg = [[] for _ in range(2 * size)]
    for left, right, edge in intervals:
        l, r = left + size, right + size
        while l < r:
            if l & 1:
                seg[l].append(edge)
                l += 1
            if r & 1:
                r -= 1
                seg[r].append(edge)
            l >>= 1
            r >>= 1

    dsu = RollbackParityDSU(n)
    ans = [""] * q

    def dfs(node, left, right):
        snap = dsu.snapshot()
        for u, v in seg[node]:
            dsu.add_edge(u, v)
        if right - left == 1:
            if left < q:
                ans[left] = "YES" if dsu.bad == 0 else "NO"
        else:
            mid = (left + right) >> 1
            dfs(node << 1, left, mid)
            dfs(node << 1 | 1, mid, right)
        dsu.rollback(snap)

    dfs(1, 0, size)
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
