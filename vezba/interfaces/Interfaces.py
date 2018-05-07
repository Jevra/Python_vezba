class ListInterface(object):

    def add_element(self, element):
        raise NotImplementedError

    def delete_element(self, element):
        raise NotImplementedError


class StackInterface(object):

    def push(self, element):
        raise  NotImplementedError

    def pop(self):
        raise NotImplementedError


class QueueInterface(object):

    def add(self, element):
        raise NotImplementedError

    def remove(self):
        raise NotImplementedError


class TreeInterface(object):

    def add_node(self, element):
        raise NotImplementedError

    def remove_node(self):
        raise NotImplementedError

    def pre_order(self):
        raise NotImplementedError

    def in_order(self):
        raise NotImplementedError

    def post_order(self):
        raise NotImplementedError