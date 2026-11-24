from collections import defaultdict
import sys

def main():
    input = sys.stdin.readline
    line = input().strip()
    if not line:
        return
    n = int(line)
    adj = defaultdict(list)
    indeg = defaultdict(int)
    outdeg = defaultdict(int)
    for i in range(n):
        s = input().strip()
        a, b = s[:2], s[1:]
        adj[a].append((b, i))
        outdeg[a] += 1
        indeg[b] += 1
        indeg.setdefault(a, 0)
        outdeg.setdefault(b, 0)

    start = None
    plus = minus = 0
    for v in set(indeg) | set(outdeg):
        d = outdeg[v] - indeg[v]
        if d == 1:
            plus += 1
            start = v
        elif d == -1:
            minus += 1
        elif d != 0:
            print("NO")
            return
    if not ((plus == 1 and minus == 1) or (plus == 0 and minus == 0)):
        print("NO")
        return
    if start is None:
        start = next(iter(outdeg))

    # Hierholzer's algorithm on the de Bruijn multigraph.
    stack = [start]
    path = []
    while stack:
        v = stack[-1]
        if adj[v]:
            to, _ = adj[v].pop()
            stack.append(to)
        else:
            path.append(stack.pop())
    if len(path) != n + 1:
        print("NO")
        return
    path.reverse()
    answer = path[0] + ''.join(v[1] for v in path[1:])
    print("YES")
    print(answer)

if __name__ == "__main__":
    main()
