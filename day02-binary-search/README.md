# Day 2 – Binary Search: 1 crore numbers, 24 steps

🎥 Video: [1 crore me sirf 24 steps?](VIDEO_LINK)

Open the middle. Target bigger? Throw away the left half. Smaller? Throw away the right half. Every step cuts the data in **half**, so 1 crore (10⁷) elements need at most **24** steps.

> ⚠️ Works only on a **sorted** array.

Dry run from the video (target 63):
```
[3, 8, 12, 17, 25, 34, 41, 58, 63, 70]
step 1: mid=25  -> go right
step 2: mid=58  -> go right
step 3: mid=63  -> FOUND at index 8
```

| | Time | Space |
|---|---|---|
| Linear search | O(n) | O(1) |
| Binary search | **O(log n)** | O(1) |

**Interview tip:** write `mid = lo + (hi - lo) / 2` in Java/C++. `(lo + hi) / 2` can overflow when `lo + hi` exceeds the int limit. Python ints don't overflow, so `(lo + hi) // 2` is fine there.

## Run
```bash
python binary_search.py
java BinarySearch.java
g++ binary_search.cpp -o binary_search && ./binary_search
```

## Practice
- LeetCode 704 – Binary Search
- LeetCode 35 – Search Insert Position
- LeetCode 34 – Find First and Last Position of Element in Sorted Array
