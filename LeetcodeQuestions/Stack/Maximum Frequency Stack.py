from collections import defaultdict
from typing import Counter


class FreqStack:
    # Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

    # Implement the FreqStack class:

    # FreqStack() constructs an empty frequency stack.
    # void push(int val) pushes an integer val onto the top of the stack.
    # int pop() removes and returns the most frequent element in the stack.
    # If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

    def __init__(self):
        self.freq = Counter()
        self.track = defaultdict(list)
        self.maxF = 0

    def push(self, val: int) -> None:
        freq = self.freq[val]
        self.freq = freq
        if freq > self.maxF:
            self.maxF = freq
        self.track[freq].append(val)

    def pop(self) -> int:
        ans = self.track[self.maxf].pop()
        self.freq[ans] -= 1
        if not self.track[self.maxF]:
            self.maxF -= 1
        return ans
