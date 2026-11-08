"""
DSA Day 2 - Binary Search, O(log n)
Video: "1 crore me sirf 24 steps?" | CodewithTanvir

Rule: the array MUST be sorted.
"""


def binary_search(arr, x):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_trace(arr, x):
    """Same algorithm, but prints every step (the dry run from the video)."""
    lo, hi, step = 0, len(arr) - 1, 0
    while lo <= hi:
        step += 1
        mid = (lo + hi) // 2
        if arr[mid] == x:
            print(f"step {step}: mid={arr[mid]}  -> FOUND at index {mid}")
            return mid
        elif arr[mid] < x:
            print(f"step {step}: mid={arr[mid]}  -> go right")
            lo = mid + 1
        else:
            print(f"step {step}: mid={arr[mid]}  -> go left")
            hi = mid - 1
    print("not found")
    return -1


def worst_case_steps(n):
    """Max steps binary search needs for n elements = floor(log2 n) + 1."""
    return n.bit_length()


if __name__ == "__main__":
    arr = [3, 8, 12, 17, 25, 34, 41, 58, 63, 70]
    print(f"Searching for 63 in {len(arr)} numbers...")
    binary_search_trace(arr, 63)

    n = 1_00_00_000  # 1 crore
    print(f"\n1 crore elements: linear = {n:,} steps, binary = {worst_case_steps(n)} steps (worst case)")
