from collections import deque
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, k, l = data[:3]
    xs = data[3:3+k]
    lengths = set(data[3+k:3+k+l])

    # Flipping [s, s+a-1] toggles only difference-array boundaries s-1 and s+a-1.
    # Thus each target ON cell contributes its two boundary tokens.
    tokens = []
    for x in xs:
        tokens.extend((x - 1, x))
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

    dist = [[-1] * (n + 1) for _ in range(m)]
    for i, start in enumerate(tokens):
        q = deque([start])
        dist[i][start] = 0
        while q:
            u = q.popleft()
            for v in graph[u]:
                if dist[i][v] == -1:
                    dist[i][v] = dist[i][u] + 1
                    q.append(v)

    # Pair up tokens. A pair costs the shortest path distance between them.
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
            d = dist[i][tokens[j]]
            if d != -1:
                best = min(best, d + dp[rest ^ bit])
            bits ^= bit
        dp[mask] = best
    print(-1 if dp[-1] >= INF else dp[-1])

if __name__ == "__main__":
    main()
