import sys
MOD = 1_000_000_007

def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n, m, k = next(it), next(it), next(it)
    c = [next(it) for _ in range(n)]

    # Group edges by the XOR value that makes their endpoints collide.
    edges = []
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        edges.append((c[u] ^ c[v], u, v))
    edges.sort()

    total_masks = 1 << k
    answer = ((total_masks - len(set(x for x, _, _ in edges))) % MOD) * pow(2, n, MOD)
    answer %= MOD

    i = 0
    while i < m:
        j = i + 1
        x = edges[i][0]
        while j < m and edges[j][0] == x:
            j += 1

        # For this x, every edge in this group forces its endpoints to
        # have the same infection status. Only touched vertices need DSU
        # storage: components in the full graph = n - successful unions.
        if j - i == 1:
            unions = 1
        else:
            parent = {}
            size = {}
            unions = 0

            def ensure(v):
                if v not in parent:
                    parent[v] = v
                    size[v] = 1

            for _, u, v in edges[i:j]:
                ensure(u)
                ensure(v)
                ru = find(parent, u)
                rv = find(parent, v)
                if ru != rv:
                    if size[ru] < size[rv]:
                        ru, rv = rv, ru
                    parent[rv] = ru
                    size[ru] += size[rv]
                    unions += 1

        components = n - unions
        answer = (answer + pow(2, components, MOD)) % MOD
        i = j

    print(answer)

if __name__ == "__main__":
    main()
