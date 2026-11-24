import sys
MOD = 1_000_000_007
MAX_LEN = 100
MAX_SUM = 25 * MAX_LEN

def build_dp():
    dp = [[0] * (MAX_SUM + 1) for _ in range(MAX_LEN + 1)]
    dp[0][0] = 1
    for length in range(1, MAX_LEN + 1):
        window = 0
        for s in range(MAX_SUM + 1):
            window += dp[length - 1][s]
            if s - 26 >= 0:
                window -= dp[length - 1][s - 26]
            dp[length][s] = window % MOD
    return dp

def main():
    input = sys.stdin.readline
    t_line = input().strip()
    if not t_line:
        return
    t = int(t_line)
    dp = build_dp()
    out = []
    for _ in range(t):
        word = input().strip()
        total = sum(ord(ch) - 97 for ch in word)
        # Every legal operation transfers one unit between adjacent letters.
        # Hence the connected component consists exactly of bounded
        # 0..25 vectors with the same total sum.
        out.append(str((dp[len(word)][total] - 1) % MOD))
    print('\n'.join(out))

if __name__ == "__main__":
    main()
