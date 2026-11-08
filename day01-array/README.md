# Day 1 – Array: why access is O(1)

🎥 Video: [Array me 7 lakhwa element 1 step me kaise?](VIDEO_LINK)

An array stores elements **side by side** (contiguous memory). So the address of any index comes from one formula:

```
address = start + index × size
```

For `start = 1000` and 4-byte ints: index 7 → `1000 + 7 × 4 = 1028`. Index 7 or index 7,00,000, it's still one calculation. That's **O(1)**.

| Operation | Time | Why |
|---|---|---|
| Access `arr[i]` | O(1) | address formula |
| Search (unsorted) | O(n) | check every element |
| Insert / delete in middle | O(n) | elements shift |

## Run
```bash
python array_access.py
java ArrayAccess.java
g++ array_access.cpp -o array_access && ./array_access
```
The C++ version prints **real memory addresses**, so you can see each `int` sitting exactly 4 bytes after the previous one.

## Practice
- LeetCode 1480 – Running Sum of 1d Array
- LeetCode 1929 – Concatenation of Array
