# Interactive solution for Codeforces 2246E.
# The judge protocol is interactive; this file cannot be tested with ordinary
# stdin sample files. Flush after every query and exit on -1.
import sys
import random

def read_int():
    s = sys.stdin.readline()
    if not s:
        sys.exit(0)
    x = int(s)
    if x == -1:
        sys.exit(0)
    return x

def main():
    t = read_int()
    rng = random.SystemRandom()
    for _ in range(t):
        # x = 1 distinguishes the operator except in the deliberately
        # ambiguous case o == 1.
        print(1, flush=True)
        o = read_int()

        if o == 0:
            # AND, and the least significant bit of v is zero.
            m0, m1 = 0, 1
            print(m0, m1, flush=True)
            r = read_int()
            print(r & 1, flush=True)
        elif o > 1:
            # OR. Any set bit of o above bit zero is also set in v.
            bit = 1 << (o.bit_length() - 1)
            print(0, bit, flush=True)
            r = read_int()
            print(0 if (r & bit) else 1, flush=True)
        else:
            # o == 1: either OR with v's low bit 0, or AND with v's
            # low bit 1. Random opposite-parity masks make the exceptional
            # indistinguishable cases negligibly unlikely.
            m0 = rng.randrange(0, 1 << 29) * 2
            m1 = rng.randrange(0, 1 << 29) * 2 + 1
            print(m0, m1, flush=True)
            r = read_int()
            if r == m0:
                print(0, flush=True)
            elif r == m1:
                print(1, flush=True)
            else:
                # In the non-exceptional case the low bit identifies b.
                print(0 if (r & 1) else 1, flush=True)

if __name__ == "__main__":
    main()
