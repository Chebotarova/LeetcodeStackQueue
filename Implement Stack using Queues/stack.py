"""
Stack.
"""

class QueueNode:
    """
    QueueNode.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    """
    Queue.
    """
    def __init__(self):
        self.front = None
        self.rear = None

    def push(self, item):
        """
        Push.
        """
        new_node = QueueNode(item)
        if not self.rear:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def peek(self):
        """
        Peek.
        """
        if self.front:
            return self.front.value
        return None

    def pop(self):
        """
        Pop.
        """
        if self.front:
            value = self.front.value
            self.front = self.front.next
            if not self.front:
                self.rear = None
            return value
        return None

    def empty(self):
        """
        Empty.
        """
        return not self.front

class MyStack:
    """
    MyStack.
    """
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        """
        Push.
        """
        self.q2.push(x)
        while not self.q1.empty():
            self.q2.push(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        """
        Pop.
        """
        return self.q1.pop()

    def top(self) -> int:
        """
        Top.
        """
        return self.q1.peek()

    def empty(self) -> bool:
        """
        Empty.
        """
        return self.q1.empty()
