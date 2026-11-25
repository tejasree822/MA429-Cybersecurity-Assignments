# Randomized interactive solution. The 29-one mask makes the ambiguous
# case extremely unlikely to remain ambiguous after the second query.
import sys
import random

def read_int():
    line = sys.stdin.readline()
    if not line:
        sys.exit(0)
    value = int(line)
    if value == -1:
        sys.exit(0)
    return value

def possible(v, x):
    return (v & x) == x or (v & (FULL ^ x)) == 0

FULL = (1 << 30) - 1

def main():
    t = read_int()
    rng = random.SystemRandom()
    for _ in range(t):
        # Exactly one zero bit; x is neither 0 nor FULL.
        zero_bit = 1 << rng.randrange(30)
        x = FULL ^ zero_bit
        print(x, flush=True)
        o = read_int()

        if o != x:
            outside = o & (FULL ^ x)
            if outside:
                # OR: this outside bit is certainly set in v.
                bit = outside & -outside
                print(0, bit, flush=True)
                r = read_int()
                b = 0 if (r & bit) else 1
            else:
                # AND: this missing x-bit is certainly zero in v.
                missing = x & (FULL ^ o)
                bit = missing & -missing
                print(0, bit, flush=True)
                r = read_int()
                b = 1 if (r & bit) else 0
            print(b, flush=True)
        else:
            # In this case v is either a supermask or a submask of x.
            # Random m0,m1 make both candidate values possible with
            # probability at most 2/2^29.
            m0 = rng.randrange(1 << 30)
            m1 = rng.randrange(1 << 30)
            while m1 == m0:
                m1 = rng.randrange(1 << 30)
            print(m0, m1, flush=True)
            r = read_int()
            v0 = r ^ m0
            v1 = r ^ m1
            ok0 = possible(v0, x)
            ok1 = possible(v1, x)
            if ok0 and not ok1:
                b = 0
            elif ok1 and not ok0:
                b = 1
            else:
                # Rare randomized collision; choose uniformly as prescribed
                # by the probabilistic strategy.
                b = rng.randrange(2)
            print(b, flush=True)

if __name__ == "__main__":
    main()
