from ..interfaces import ListInterface


class List(ListInterface):

    """Implementing list"""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_element(self, element):
        if self.head is None:
            self.head = element
            self.tail = element
        else:
            self.tail.next = element
            self.tail = self.tail.next

    def delete_element(self, element):
        temp = self.head
        prev = None
        while temp.information != element.information and temp is not None:
            prev = temp
            temp = temp.next
        if temp == self.head:
            self.head = self.head.next
            del (temp)
        elif temp.next is None:
            prev.next = None
            del (temp)
        else:
            prev.next = temp.next
            del (temp)
