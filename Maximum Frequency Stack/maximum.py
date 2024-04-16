"""
Maximum.
"""

from collections import defaultdict, deque

class FreqStack:
    """
    FreqStack.
    """
    def __init__(self):
        self.freq_map = defaultdict(int)
        self.grouped_stack = defaultdict(deque)
        self.max_freq = 0

    def push(self, val: int) -> None:
        """
        Push.
        """
        self.freq_map[val] += 1
        freq = self.freq_map[val]
        self.max_freq = max(self.max_freq, freq)
        self.grouped_stack[freq].append(val)

    def pop(self) -> int:
        """
        Pop.
        """
        val = self.grouped_stack[self.max_freq].pop()
        self.freq_map[val] -= 1
        if not self.grouped_stack[self.max_freq]:
            self.max_freq -= 1
        return val
