import sys

def main():
    input = sys.stdin.readline
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    text = input().strip()
    m = int(input())
    # Trie of reversed, lowercased dictionary words.
    nxt = [{}]
    terminal = [None]
    for _ in range(m):
        word = input().strip()
        rev = word.lower()[::-1]
        node = 0
        for ch in rev:
            to = nxt[node].get(ch)
            if to is None:
                to = len(nxt)
                nxt[node][ch] = to
                nxt.append({})
                terminal.append(None)
            node = to
        terminal[node] = word

    # dp[i] stores a predecessor position and chosen original word.
    prev = [-1] * (n + 1)
    chosen = [None] * (n + 1)
    prev[0] = 0
    for i in range(n):
        if prev[i] == -1:
            continue
        node = 0
        j = i
        while j < n:
            node = nxt[node].get(text[j], -1)
            if node == -1:
                break
            j += 1
            if terminal[node] is not None and prev[j] == -1:
                prev[j] = i
                chosen[j] = terminal[node]

    # The statement guarantees at least one decomposition.
    words = []
    pos = n
    while pos:
        words.append(chosen[pos])
        pos = prev[pos]
    print(' '.join(reversed(words)))

if __name__ == "__main__":
    main()
