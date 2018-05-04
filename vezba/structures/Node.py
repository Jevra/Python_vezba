class Node(object):

    """Implementing one Node that contains information"""

    def __init__(self, information):
        self.next = None
        self.information = information

    def read_information(self):
        return str(self.information)