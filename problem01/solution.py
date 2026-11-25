# NOT SUBMISSION-READY: shortest-path/T-join approach needs full performance validation
from collections import deque
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, k, l = data[:3]
    xs = data[3:3 + k]
    lengths = set(data[3 + k:3 + k + l])

    # In the difference representation, flipping [s, s+a) toggles
    # boundary positions s and s+a. The target boundaries are the odd
    # occurrences among x-1 and x for every required ON panel x.
    parity = set()
    for x in xs:
        for p in (x - 1, x):
            if p in parity:
                parity.remove(p)
            else:
                parity.add(p)
    tokens = sorted(parity)
    m = len(tokens)
    if m == 0:
        print(0)
        return

    graph = [[] for _ in range(n + 1)]
    for a in lengths:
        for u in range(n + 1 - a):
            v = u + a
            graph[u].append(v)
            graph[v].append(u)

    # Shortest-path metric between all boundary tokens.
    dist = [[-1] * m for _ in range(m)]
    for i, start in enumerate(tokens):
        d = [-1] * (n + 1)
        d[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in graph[u]:
                if d[v] == -1:
                    d[v] = d[u] + 1
                    q.append(v)
        for j, target in enumerate(tokens):
            dist[i][j] = d[target]

    # Minimum T-join in an unweighted graph = minimum perfect matching
    # in the shortest-path metric on the even-sized set of odd vertices.
    INF = 10**18
    size = 1 << m
    dp = [INF] * size
    dp[0] = 0
    for mask in range(1, size):
        if mask.bit_count() & 1:
            continue
        i = (mask & -mask).bit_length() - 1
        rest = mask ^ (1 << i)
        best = INF
        bits = rest
        while bits:
            bit = bits & -bits
            j = bit.bit_length() - 1
            if dist[i][j] != -1:
                best = min(best, dist[i][j] + dp[rest ^ bit])
            bits ^= bit
        dp[mask] = best
    print(-1 if dp[-1] >= INF else dp[-1])

if __name__ == "__main__":
    main()
