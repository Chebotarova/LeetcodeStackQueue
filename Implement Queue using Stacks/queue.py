"""
Queue.
"""

class Node:
    """
    Node.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    """
    Stack.
    """
    def __init__(self):
        self.top = None

    def push(self, item):
        """
        Push.
        """
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Pop.
        """
        if self.is_empty():
            return None
        popped = self.top
        self.top = self.top.next
        return popped.value

    def peek(self):
        """
        Peek.
        """
        if self.is_empty():
            return None
        return self.top.value

    def is_empty(self):
        """
        Empty.
        """
        return self.top is None

class MyQueue:
    """
    MyQueue.
    """
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        """
        Push.
        """
        self.stack1.push(x)

    def pop(self) -> int:
        """
        Pop.
        """
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Peek.
        """
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def empty(self) -> bool:
        """
        Empty.
        """
        return self.stack1.is_empty() and self.stack2.is_empty()
