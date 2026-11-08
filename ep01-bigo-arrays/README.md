# Episode 1 – Big-O Notation + Arrays

🎥 Video: [Big O Notation Explained in 3 Minutes (Hindi)](VIDEO_LINK)

| File | What it shows |
|---|---|
| `big_o_table.py` | The Big-O table from the video: steps for n = 10 vs n = 10,00,000 |
| `arrays.py` | The Python array code from the video (access, append, traverse, insert) |
| `ArrayBasics.java` | The Java array code from the video (fixed size, `.length`) |
| `find_duplicate.py` | Interview Q2: brute force O(n²) vs hash set O(n), with timing |

## Array operations
| Operation | Time | Why |
|---|---|---|
| Access `arr[i]` | O(1) | address formula |
| Search | O(n) | check every element |
| Insert / delete | O(n) | shifting |
| Insert at end | O(1)* | amortized (dynamic array) |

## Array vs Linked List (Interview Q1)
| | Array | Linked List |
|---|---|---|
| Memory | contiguous | scattered nodes |
| Access | O(1) | O(n) |
| Insert at start | O(n) | O(1) |
| Size | fixed (dynamic arrays grow) | dynamic |

## Run
```bash
python big_o_table.py
python arrays.py
python find_duplicate.py
java ArrayBasics.java
```

## Practice
- LeetCode 217 – Contains Duplicate
- LeetCode 1 – Two Sum
- LeetCode 26 – Remove Duplicates from Sorted Array
