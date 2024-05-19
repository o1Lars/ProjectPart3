"""
This module provides the HuffmanTreeCreator module. Module creates a Huffman Tree from a frequency table.
It gives the following methods:
-
-
-

Requirements
------------
Python 3.7 or higher.
PQHeap.py
bitIO.py
DictBinTree.py

Notes
-----
Module is created as part of the group project for the final exam of DS814 Algoritmer og Datastrukturer forår 2024.

Projektgrupe:
Chris Thorbjørn Eichmuller Vandborg
cvand15@student.sdu.dk

Lars Mogensen
lmoge23@student.sdu.dk

"""
from Element import Element
import PQHeap


class HuffmanTreeCreator:
    """Class creates an instance of a Huffman tree from a list of frequencies. Class supports encoding and decoding
    Huffman codes from the list of frequencies."""

    def __init__(self, frequency_table: list):
        """
        frequency: list
            a list of frequencies, where the index of the list is a wholenumber representing a byte and the element
            its frequency.
        """
        self.frequency_table = self._convert_int_to_elements(frequency_table)  # convert frequencies to elements
        PQHeap.build_min_heap(self.frequency_table)  # Rearrange into min priority queue
        self.huffman_tree = self._huffman_coding(self.frequency_table)  # create Huffman tree from table
        self.huffman_codes = self._create_huffman_codes_list()  # Store code mapping in list

    def _convert_int_to_elements(self, f_table: list) -> list:
        """Return a list of Elements created from a list of frequencies."""

        elements = []

        for index, frequency in enumerate(f_table):
            elements.append(Element(frequency, TreeNode(root=index)))  # populate list with Elements

        return elements

    def _huffman_coding(self, C: list):
        n = len(C)
        Q = C

        # Until one node left, grab 2 smallest elements in PQ and join together in tree
        for i in range(n - 1):
            z = Element(key=None, data=TreeNode())  # allocate new node
            x = PQHeap.extractMin(Q)
            y = PQHeap.extractMin(Q)
            z.data.left = x
            z.data.right = y
            z.key = x.key + y.key
            PQHeap.insert(Q, z)

        return PQHeap.extractMin(Q)

    def _create_huffman_codes_list(self):
        """Return the list huffman codes for each entry in the frequency table by recursively traversing the tree
        and appending each code to the table"""

        codes_list = [0 for num in range(256)]
        huffman_tree = self.huffman_tree
        bin_code = ''

        self._ordered_traversal(huffman_tree, codes_list, bin_code)

        return codes_list

    def _ordered_traversal(self, binary_tree, value_list, bite_code):
        """Recursively traverse a binary tree and append value to the list"""

        counter = 0

        if binary_tree is not None:
            counter += 1
            # If the node is a leaf (both left and right children are None),
            # append its key (byte value) and the binary code to the value_list
            if binary_tree.data.left is None and binary_tree.data.right is None:
                value_list[binary_tree.data.root] = bite_code
                return
            else:
                # Otherwise, continue traversing left/right
                self._ordered_traversal(binary_tree.data.left, value_list, bite_code + '0')
                self._ordered_traversal(binary_tree.data.right, value_list, bite_code + '1')


class TreeNode:
    """Creates a node/subtree with a key and the left and right child of the node"""

    def __init__(self, root=-1, left_child=None, right_child=None):
        """
        Parameters
        ----------
        key, int=None
            The key value of the node
        """
        self.root = root
        self.left = left_child
        self.right = right_child
