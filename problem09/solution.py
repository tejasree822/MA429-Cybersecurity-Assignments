import sys
from bisect import bisect_left

class RollbackDSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.history = []

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            self.history.append((0,))
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.history.append((1, b, a, self.size[a]))
        self.parent[b] = a
        self.size[a] += self.size[b]

    def snapshot(self):
        return len(self.history)

    def rollback(self, snap):
        while len(self.history) > snap:
            item = self.history.pop()
            if item[0]:
                _, child, root, old_size = item
                self.parent[child] = child
                self.size[root] = old_size

    def component_size(self, x):
        return self.size[self.find(x)]

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q, k = data[0], data[1], data[2]
    queries = []
    day_ends = []
    p = 3
    for i in range(q):
        typ = data[p]
        p += 1
        if typ == 1:
            x, y = data[p] - 1, data[p + 1] - 1
            p += 2
            queries.append((1, x, y))
        elif typ == 2:
            x = data[p] - 1
            p += 1
            queries.append((2, x))
        else:
            queries.append((3,))
            day_ends.append(i)

    # A meeting stays active through the current day and the next k-1
    # days. It expires immediately after the k-th subsequent day-end.
    size = 1
    while size < q:
        size <<= 1
    seg = [[] for _ in range(2 * size)]
    for i, query in enumerate(queries):
        if query[0] != 1:
            continue
        _, u, v = query
        edge = (u, v)
        pos = bisect_left(day_ends, i) + k - 1
        end = day_ends[pos] + 1 if pos < len(day_ends) else q
        if end <= i:
            continue
        l, r = i + size, end + size
        while l < r:
            if l & 1:
                seg[l].append(edge)
                l += 1
            if r & 1:
                r -= 1
                seg[r].append(edge)
            l >>= 1
            r >>= 1

    dsu = RollbackDSU(n)
    ans = []

    def dfs(node, left, right):
        snap = dsu.snapshot()
        for u, v in seg[node]:
            dsu.union(u, v)
        if right - left == 1:
            if left < q and queries[left][0] == 2:
                ans.append(str(dsu.component_size(queries[left][1])))
        else:
            mid = (left + right) >> 1
            dfs(node << 1, left, mid)
            dfs(node << 1 | 1, mid, right)
        dsu.rollback(snap)

    dfs(1, 0, size)
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
