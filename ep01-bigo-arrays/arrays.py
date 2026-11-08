"""
Episode 1 - Arrays (code shown in the video) | CodewithTanvir
Python's list is a dynamic array: it grows by itself when needed.
"""
arr = [10, 20, 30, 40]

print(arr[2])        # access O(1)
arr.append(50)       # end pe add (amortized O(1))

for x in arr:        # traverse O(n)
    print(x)

arr.insert(0, 5)     # insert at the start: everything shifts -> O(n)
print(arr)
