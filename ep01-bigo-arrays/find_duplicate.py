"""
Episode 1 - Interview Q2: does the array have a duplicate? | CodewithTanvir
Brute force O(n^2)  vs  hash set O(n)
"""
import random
import time


def has_duplicate_brute(arr):
    n = len(arr)
    for i in range(n):              # compare every pair -> O(n^2)
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True
    return False


def has_duplicate_set(arr):
    seen = set()
    for x in arr:                   # one pass -> O(n), uses O(n) extra space
        if x in seen:
            return True
        seen.add(x)
    return False


if __name__ == "__main__":
    print(has_duplicate_set([1, 2, 3, 1]))   # True
    print(has_duplicate_set([1, 2, 3, 4]))   # False

    arr = random.sample(range(10_000_000), 5_000)   # 5000 unique numbers = worst case
    for fn in (has_duplicate_brute, has_duplicate_set):
        t = time.perf_counter()
        fn(arr)
        print(f"{fn.__name__:<22} {time.perf_counter() - t:.4f} s")
