# Assignment 1
# . Sparse Array with a Linked list implementation
#
# Name: Jacob Negri
# SN: 13165429

# importing node to be used in the sparse array class
from Node import Node

# The spase array class including the functions:
# _init_, fill(seq), _getitem_(j), _setitem_(j,e), _len_(), get_usage(), Find_index, print_list

class SparseArray(object):

    # Constructing an initially empty SparseArray of size n
    def __init__(self, n, r=None):
        # initial empty node pointer for start
        self.root = Node()
        # initial empty node pointer for end
        self.last = Node()
        # set size of SparseArray as variable n
        self.size = n
        # initial set of non-empty element variable
        self.use = 0

    # Returns the length of the array
    def __len__(self):
        return self.size

    # Setting
    def __setitem__(self, j, e):
        i = self.find_index(j)
        new_node = Node(e, i, self.root)
        self.root = new_node
        self.use += 1

    def __getitem__(self, j):
        i = self.find_index(j)
        this_node = self.root
        while this_node is not None:
            if this_node.get_index() == i:
                return this_node.element
            else:
                this_node = this_node.get_next()
        return None

    def fill(self, seq):
        if len(seq) < self.size:
            print(len(seq))
            for x in range(len(seq)):
                self[x] = seq[x]
        else:
            print("ValueError: sequence longer than sparse array")
            raise SystemExit

    def get_usage(self):
        return self.use

    def find_index(self, j):
        if -1 * self.size < j < 0:
            return self.size - abs(j)
        elif 0 <= j < self.size:
            return j
        else:
            print("IndexError: index out of range")
            raise SystemExit

    def print_list(self):
        print("Sparse Array:")
        this_node = self.root
        while this_node.has_next():
            print(this_node.to_string())
            this_node = this_node.get_next()


# Crating the sample output as seen in the assignment task sheet
array = SparseArray(1000000)
print(len(array))
print(array.get_usage())
array[999999] = 42
print(array[999999])
print(array[-1])
print(array.get_usage())
print(array[0])
print(array[0] is None)
print(array[1000000])


