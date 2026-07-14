"""
Task 3: Queue
Contributor: Member B

Queue implemented from scratch using a singly linked structure
(no built-in queue/deque class used).
"""


class _Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def enqueue(self, value):
        node = _Node(value)
        if self._rear is None:
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        node = self._front
        self._front = node.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return node.value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._front.value

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def to_list(self):
        items = []
        current = self._front
        while current:
            items.append(current.value)
            current = current.next
        return items


if __name__ == "__main__":
    q = Queue()

    print("-- Queue demo --")
    q.enqueue("A")
    print("enqueue A ->", q.to_list())

    q.enqueue("B")
    print("enqueue B ->", q.to_list())

    q.enqueue("C")
    print("enqueue C ->", q.to_list())

    print("peek ->", q.peek())

    q.dequeue()
    print("dequeue   ->", q.to_list())

    q.enqueue("D")
    print("enqueue D ->", q.to_list())

    q.dequeue()
    print("dequeue   ->", q.to_list())

    q.dequeue()
    print("dequeue   ->", q.to_list())
