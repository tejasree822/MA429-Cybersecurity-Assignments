# NOT SUBMISSION-READY: O(n^2) Python implementation has not passed maximum-constraint timing tests
import sys
from array import array

def main():
    input = sys.stdin.buffer.readline
    line = input().strip()
    if not line:
        return
    n = int(line)
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    # parent[root][v] is the neighbor of v on its path toward root;
    # sub[root][v] is the size of v's component after cutting that edge.
    parent = [array('i', [-1]) * n for _ in range(n)]
    sub = [array('i', [0]) * n for _ in range(n)]
    for root in range(n):
        par = parent[root]
        order = [root]
        par[root] = root
        for u in order:
            for v in g[u]:
                if v != par[u]:
                    par[v] = u
                    order.append(v)
        sizes = sub[root]
        for u in reversed(order):
            total = 1
            for v in g[u]:
                if par[v] == u:
                    total += sizes[v]
            sizes[u] = total

    # dp[u][v] is the best sum for a prefix of edge labels forming
    # a simple path whose endpoints are u and v.
    dp = [array('q', [-1]) * n for _ in range(n)]
    sys.setrecursionlimit(1000000)

    def solve(u, v):
        if u == v:
            return 0
        cached = dp[u][v]
        if cached != -1:
            return cached
        pu = parent[u][v]
        pv = parent[v][u]
        contribution = sub[u][v] * sub[v][u]
        value = contribution + max(solve(u, pu), solve(v, pv))
        dp[u][v] = value
        return value

    answer = 0
    for u in range(n):
        for v in range(n):
            if u != v:
                answer = max(answer, solve(u, v))
    print(answer)

if __name__ == "__main__":
    main()
