# Interactive probabilistic solution. Flush every query and exit on -1.
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

def is_possible_v(v, x):
    # If o == x, then OR implies v is a submask of x,
    # while AND implies v is a supermask of x.
    return (v & ~x) == 0 or (v & x) == x

def main():
    t = read_int()
    rng = random.SystemRandom()
    LIMIT = 1 << 30
    FULL = LIMIT - 1

    for _ in range(t):
        # Keep x balanced so the ambiguous family of possible v values
        # is a very small fraction of all 30-bit masks.
        positions = rng.sample(range(30), 15)
        x = sum(1 << bit for bit in positions)
        print(x, flush=True)
        o = read_int()

        if o != x:
            outside = o & (FULL ^ x)
            if outside:
                # OR: any 1 outside x is certainly a 1 in v.
                bit = outside & -outside
                print(0, bit, flush=True)
                r = read_int()
                b = 0 if (r & bit) else 1
            else:
                # AND: any missing 1-bit of x is certainly 0 in v.
                missing = x & (FULL ^ o)
                bit = missing & -missing
                print(0, bit, flush=True)
                r = read_int()
                b = 1 if (r & bit) else 0
            print(b, flush=True)
        else:
            # Both operators remain possible. Random masks make the two
            # candidate hidden values overwhelmingly unlikely to both satisfy
            # the required submask/supermask condition.
            m0 = rng.randrange(LIMIT)
            m1 = rng.randrange(LIMIT)
            while m1 == m0:
                m1 = rng.randrange(LIMIT)
            print(m0, m1, flush=True)
            r = read_int()
            candidate0 = r ^ m0
            candidate1 = r ^ m1
            valid0 = is_possible_v(candidate0, x)
            valid1 = is_possible_v(candidate1, x)
            if valid0 and not valid1:
                b = 0
            elif valid1 and not valid0:
                b = 1
            else:
                # The randomized collision probability is tiny (about 2^-14
                # for a balanced 30-bit x); no deterministic one-shot
                # decision is possible in this exceptional overlap.
                b = rng.randrange(2)
            print(b, flush=True)

if __name__ == "__main__":
    main()
