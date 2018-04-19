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

    # Setting a nodes indexing
    def __setitem__(self, j, e):
        i = self.find_index(j)
        new_node = Node(e, i, self.root)
        self.root = new_node
        self.use += 1

    # Getting a nodes index
    def __getitem__(self, j):
        i = self.find_index(j)
        current_node = self.root
        while current_node is not None:
            if current_node.get_index() == i:
                return current_node.element
            else:
                current_node = current_node.get_next()
        return None

    # filling the sparse array
    def fill(self, seq):
        if len(seq) < self.size:
            print(len(seq))
            for x in range(len(seq)):
                self[x] = seq[x]
        else:
            # raising a value error and exiting the system
            print("ValueError: sequence longer than sparse array")
            raise SystemExit

    # returning the number of non-empty elements
    def get_usage(self):
        return self.use

    # finds an index and returns the value stored in that index
    def find_index(self, j):
        if -1 * self.size < j < 0:
            return self.size - abs(j)
        elif 0 <= j < self.size:
            return j
        else:
            print("IndexError: index out of range")
            raise SystemExit

    # printing the sparse array
    def print_sparse_array(self):
        print("Sparse Array:")
        current_node = self.root
        while current_node.has_next():
            print(current_node.to_string())
            current_node = current_node.get_next()


# Commented out in order to run the Sparse array testing:
    # Crating the sample output as seen in the assignment task sheet
    # array = SparseArray(1000000)
    # print(len(array))
    # print(array.get_usage())
    # array[999999] = 42
    # print(array[999999])
    # print(array[-1])
    # print(array.get_usage())
    # print(array[0])
    # print(array[0] is None)
    # print(array[1000000])


