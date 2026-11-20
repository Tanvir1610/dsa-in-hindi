"""
DSA Day 4 - Queue operations + why deque beats list | CodewithTanvir
"""
from collections import deque
import time

q = deque()
q.append("Rahul")      # enqueue (rear)
q.append("Priya")
q.append("Aman")
print("front:", q[0])          # peek front -> Rahul
print("dequeue:", q.popleft()) # Rahul leaves first (FIFO)
print("queue now:", list(q))

# Why deque? Remove 1 lakh items from the front of each:
n = 100_000
lst, dq = list(range(n)), deque(range(n))

t = time.perf_counter()
while lst:
    lst.pop(0)                 # O(n) each time: shifts everything left
t_list = time.perf_counter() - t

t = time.perf_counter()
while dq:
    dq.popleft()               # O(1) each time
t_deque = time.perf_counter() - t

print(f"\nlist.pop(0):    {t_list:.3f} s")
print(f"deque.popleft(): {t_deque:.3f} s")
