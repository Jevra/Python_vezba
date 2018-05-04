from ..interfaces import QueueInterface


class Queue(QueueInterface):

    """Implementing queue using list"""

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, element):
        if self.head is None:
            self.head = element
            self.tail = self.head
        else:
            self.tail.next = element
            self.tail = self.tail.next

    def remove(self):
        temp = self.head
        self.head = self.head.next
        return temp
