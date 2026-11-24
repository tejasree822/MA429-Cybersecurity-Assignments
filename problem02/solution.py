# Interactive solution. Flush every query and terminate immediately on -1.
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

def main():
    t = read_int()
    rng = random.SystemRandom()
    LIMIT = 1 << 30
    for _ in range(t):
        # A random mask with both zero and one bits makes the o == x
        # ambiguity distinguishable using complementary masks.
        x = rng.randrange(1, LIMIT - 1)
        while x == 0 or x == LIMIT - 1:
            x = rng.randrange(1, LIMIT - 1)
        print(x, flush=True)
        o = read_int()

        if o != x:
            # A 1 outside x proves OR; a 0 inside x proves AND.
            outside = o & (LIMIT - 1 - x)
            if outside:
                op = "or"
                known_bit = outside & -outside  # v has this bit = 1
            else:
                op = "and"
                missing = x & (LIMIT - 1 - o)
                known_bit = missing & -missing  # v has this bit = 0

            m0, m1 = 0, known_bit
            print(m0, m1, flush=True)
            r = read_int()
            if op == "or":
                b = 0 if (r & known_bit) else 1
            else:
                b = 1 if (r & known_bit) else 0
            print(b, flush=True)
        else:
            # If o == x, then:
            # OR implies v is a submask of x; AND implies v is a supermask.
            # Set m0=x and m1=~x. The four (operator, b) cases have
            # disjoint signatures on the x and ~x bit positions.
            m0 = x
            m1 = (LIMIT - 1) ^ x
            print(m0, m1, flush=True)
            r = read_int()
            low_zero = (r & x) == 0
            high_zero = (r & (LIMIT - 1 ^ x)) == 0
            low_one = (r & x) == x
            high_one = (r & (LIMIT - 1 ^ x)) == (LIMIT - 1 ^ x)
            if low_zero or high_zero:
                b = 0
            elif low_one or high_one:
                b = 1
            else:
                # For nonempty x and its complement, the cases above
                # cover all valid replies under the protocol.
                sys.exit(0)
            print(b, flush=True)

if __name__ == "__main__":
    main()
