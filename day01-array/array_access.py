"""
DSA Day 1 - Array access is O(1)
Video: "Array me 7 lakhwa element 1 step me kaise?" | CodewithTanvir

Why? An array sits in contiguous memory, so the address of any index is one formula:
    address = start + index * size
"""


def address_of(start, index, size):
    """Address of arr[index] when the array starts at `start` and each element is `size` bytes."""
    return start + index * size


def linear_find(arr, target_index):
    """The slow way: walk from the start, counting each step. O(n)."""
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if i == target_index:
            return arr[i], steps
    return None, steps


if __name__ == "__main__":
    # Same numbers as the video: start = 1000, int = 4 bytes
    start, size = 1000, 4
    print("Address formula: start + index * size")
    print("index 7      ->", address_of(start, 7, size))        # 1028
    print("index 7,00,000 ->", address_of(start, 700_000, size))  # 2801000 (one step either way)

    arr = list(range(1_000_000))          # 10 lakh elements
    value, steps = linear_find(arr, 700_000)
    print(f"\nCounting one by one: {steps:,} steps")
    print(f"Direct access arr[700000] = {arr[700_000]}  ->  1 step, O(1)")
