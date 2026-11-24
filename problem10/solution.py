# Interactive solution: at most two queries.
# The judge returns f^c(r) for the requested exponent c and start r.
import sys

def ask(c, r):
    print("?", c, r, flush=True)
    line = sys.stdin.readline()
    if not line:
        sys.exit(0)
    value = int(line)
    if value == -1:
        sys.exit(0)
    return value

def main():
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line)
    # Let c = f^n(1). Since f maps an n-element set to itself,
    # after n applications the orbit has reached its cycle.
    c = ask(n, 1)
    steps = n - c
    r = 1 if steps == 0 else ask(steps, 1)
    # f^c(r) = f^c(f^(n-c)(1)) = f^n(1) = c.
    print("!", c, r, flush=True)

if __name__ == "__main__":
    main()
