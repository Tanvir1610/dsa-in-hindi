"""
Episode 1 - Big-O in real numbers | CodewithTanvir
Reproduces the table from the video: how many steps for n = 10 vs n = 10,00,000.
"""
import math


def steps(n):
    return {
        "O(1)": 1,
        "O(log n)": math.ceil(math.log2(n)),
        "O(n)": n,
        "O(n log n)": math.ceil(n * math.log2(n)),
        "O(n^2)": n * n,
    }


def indian(num):
    """Format with Indian grouping: 1000000 -> 10,00,000"""
    s = str(num)
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return ",".join(parts) + "," + tail


if __name__ == "__main__":
    small, big = steps(10), steps(10_00_000)
    print(f"{'Big-O':<12}{'n = 10':>10}{'n = 10,00,000':>26}")
    for k in small:
        print(f"{k:<12}{indian(small[k]):>10}{indian(big[k]):>26}")
    print("\nO(n^2) at 10 lakh = 1 lakh crore steps (10^12). That's why O(n^2) fails on big inputs.")
