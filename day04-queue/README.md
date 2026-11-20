# Day 4 – Queue: who prints first?

🎥 Video: [Printer ko kaise pata kiska print pehle?](VIDEO_LINK)

A queue is the ticket-counter line: whoever comes first, leaves first. **FIFO: First In, First Out.** New items join at the **rear** (enqueue); work happens at the **front** (dequeue).

`printer.py` is the exact code from the video:
```
$ python printer.py
Rahul.pdf
deque(['Priya.pdf', 'Aman.pdf'])
```

| Operation | Python (`deque`) | Java (`ArrayDeque`) | C++ (`std::queue`) | Time |
|---|---|---|---|---|
| enqueue | `append(x)` | `offer(x)` | `push(x)` | O(1) |
| dequeue | `popleft()` | `poll()` | `pop()` | O(1) |
| front | `q[0]` | `peek()` | `front()` | O(1) |

> ⚠️ **Interview tip:** never use a Python `list` with `pop(0)` as a queue. It shifts every element, so it's O(n). Run `queue_basics.py` to see the speed difference yourself.

Used in: printers, CPU task scheduling, graph BFS, call-center lines.

## Run
```bash
python printer.py
python queue_basics.py
java PrinterQueue.java
g++ printer_queue.cpp -o printer_queue && ./printer_queue
```

## Practice
- LeetCode 232 – Implement Queue using Stacks
- LeetCode 933 – Number of Recent Calls
- LeetCode 622 – Design Circular Queue
