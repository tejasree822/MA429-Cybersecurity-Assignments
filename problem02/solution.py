# NOT SUBMISSION-READY: randomized interactive strategy has a nonzero failure probability
# Randomized interactive solution. Flush every query and exit on -1.
import sys
import random

FULL = (1 << 30) - 1

def read_int():
    line = sys.stdin.readline()
    if not line:
        sys.exit(0)
    value = int(line)
    if value == -1:
        sys.exit(0)
    return value

def possible(v, x):
    # o == x is possible for OR when v is a submask of x,
    # and for AND when v is a supermask of x.
    return (v & (FULL ^ x)) == 0 or (v & x) == x

def main():
    t = read_int()
    rng = random.SystemRandom()
    for _ in range(t):
        # A balanced mask makes both ambiguous families small:
        # 2^15 possible submasks and 2^15 possible supermasks.
        positions = rng.sample(range(30), 15)
        x = sum(1 << bit for bit in positions)
        print(x, flush=True)
        o = read_int()

        if o != x:
            outside = o & (FULL ^ x)
            if outside:
                # OR: a set bit outside x must also be set in v.
                bit = outside & -outside
                print(0, bit, flush=True)
                r = read_int()
                b = 0 if (r & bit) else 1
            else:
                # AND: a missing bit inside x must be zero in v.
                missing = x & (FULL ^ o)
                bit = missing & -missing
                print(0, bit, flush=True)
                r = read_int()
                b = 1 if (r & bit) else 0
            print(b, flush=True)
        else:
            # For each possible answer, decode its candidate v. With random
            # masks, the chance both candidates pass the sub/supermask test
            # is about 2^-14. This remains a randomized solution.
            m0 = rng.randrange(1 << 30)
            m1 = rng.randrange(1 << 30)
            while m1 == m0:
                m1 = rng.randrange(1 << 30)
            print(m0, m1, flush=True)
            r = read_int()
            ok0 = possible(r ^ m0, x)
            ok1 = possible(r ^ m1, x)
            if ok0 and not ok1:
                b = 0
            elif ok1 and not ok0:
                b = 1
            else:
                # Rare collision: the protocol gives no deterministic way
                # to disambiguate this single reply for these chosen masks.
                b = rng.randrange(2)
            print(b, flush=True)

if __name__ == "__main__":
    main()
