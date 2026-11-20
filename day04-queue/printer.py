"""
DSA Day 4 - Queue (FIFO) | CodewithTanvir
Video: "Printer ko kaise pata kiska print pehle?"

Use collections.deque: append() = enqueue, popleft() = dequeue. Both O(1).
Don't use list.pop(0) for a queue: it shifts every element, O(n).
"""
from collections import deque

prints = deque()
prints.append("Rahul.pdf")
prints.append("Priya.pdf")
prints.append("Aman.pdf")

print(prints.popleft())   # pehle aaya
print(prints)             # baaki line
