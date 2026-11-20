"""
DSA Day 3 - Stack (LIFO) | CodewithTanvir
Video: "Ctrl+Z ka secret = STACK"

In Python, a list is a stack: append() = push, pop() = pop. Both O(1).
"""


def undo_demo():
    stack = []
    for action in ["H", "i", "!"]:     # you type H, i, !
        stack.append(action)            # every action is pushed
        print(f"push({action})  ->  {stack}")
    print("Ctrl+Z  -> pop() removed", stack.pop())   # undo = pop the LAST action
    print("Text now:", "".join(stack))


def is_balanced(s):
    """Classic interview question: are the brackets balanced?  "{[()]}" -> True"""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


if __name__ == "__main__":
    undo_demo()
    print()
    for s in ["{[()]}", "([)]", "(("]:
        print(f"is_balanced({s!r}) = {is_balanced(s)}")
