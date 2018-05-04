from ..interfaces import StackInterface


class Stack(StackInterface):

    """Implementation of stack using implemented list"""

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, element):
        if self.head is None:
            self.head = element
            self.tail = self.head
        else:
            self.head = element
            self.head.next = self.tail
            self.tail = self.head

    def pop(self):
        temp = self.head
        self.head = self.tail.next
        self.tail = self.tail.next
        return temp
