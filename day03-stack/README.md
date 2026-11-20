# Day 3 – Stack: the secret behind Ctrl+Z

🎥 Video: [Ctrl+Z ka secret = STACK](VIDEO_LINK)

A stack is a pile of plates: the last plate you put on is the first one you take off. **LIFO: Last In, First Out.**

Every action you type is **pushed**. Ctrl+Z **pops** the last one.

| Operation | What it does | Time |
|---|---|---|
| `push(x)` | put on top | O(1) |
| `pop()` | take from top | O(1) |
| `peek()` | look at top | O(1) |

Used in: undo/redo, the browser back button, function calls and recursion, bracket matching.

| Language | Use |
|---|---|
| Python | `list` (`append`, `pop`) |
| Java | `ArrayDeque` (`push`, `pop`, `peek`), faster than the old `Stack` class |
| C++ | `std::stack` (`push`, `pop`, `top`) |

## Run
```bash
python stack.py
java StackDemo.java
g++ stack.cpp -o stack && ./stack
```

## Practice
- LeetCode 20 – Valid Parentheses (the `is_balanced` function here)
- LeetCode 155 – Min Stack
- LeetCode 739 – Daily Temperatures
