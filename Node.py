class Node(object):

    def __init__(self, d=None, i=None, n=None):
        # element characteristic for node type
        self.element = d
        # node index characteristic for node type
        self.index = i
        # linked list pointer for node
        self.next_node = n

    def get_next(self):
        # return next node
        return self.next_node

    def get_data(self):
        # returning the element data
        return self.element

    def set_data(self, d):
        # Setting the element with data
        self.element = d

    def get_index(self):
        # returning the index value
        return self.index

    def to_string(self):
        return "Element: " + str(self.element)

    def has_next(self):
        if self.get_next() is None:
            return False
        return True