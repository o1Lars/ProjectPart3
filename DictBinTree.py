from __future__ import annotations
"""
This module provides DictBinTree, which is a class that constructs the data structure binary search tree with numbers as keys.
The class provides:
 - T.search(k), returns a bolean that return k's placement in the tree
 - T.insert(k), which inserts key k in the tree T
 - T.orderedTraversal(), which returns a list of keys in the tree T in sorted order.

Requirements
------------
Python 3.7 or higher.

Notes
-----
Module is created as part of the group project for the final exam of DS814 Algoritmer og Datastrukturer forår 2024.

Projektgrupe:
Chris Thorbjørn Eichmuller Vandborg
cvand15@student.sdu.dk

Lars Mogensen
lmoge23@student.sdu.dk


"""

class DictBinTree:
    """Constructs an unstructured binary search tree data structure intance."""

    def __init__(self):
        """
            represents the root node of the binary tree. If nothing is provided, root is None and tree is empty.
        """
        self.root = None

        #for key in keys:
        #self.root = DictBinTree.insert(self.root, key)

    # Public methods for the binary search tree
    def search(self, k: int) -> bool:
        """Return true if the k key is in the binary search tree

        Parameters
        ----------
        k: int
            k is an integer value key
        """
        if self.root.key == None:
            return False
        elif self._search(self.root, k):
            return True
        else:
            return False

    def insert(self, input_key: int) -> None:
        """Creates and inserts a new node with key k into the binary search tree

        Parameters
        ----------
        k, int:
            An integer value
        """
        self._insert(BinNode(input_key))

    def orderedTraversal(self) -> list[int]:
        """Returns a list of keys from the binary search tree in ascending order"""

        mylist=[]
        self._orderedTraversal(self.root, mylist)

        return mylist

    # private methods for the binary search tree
    def _search(self, x: BinNode, k: int) -> BinNode:
        """Return a pointer to a node with key k if one exists in the subtree

        Parameters
        ----------
        x, BinNode
            A pointer to a subtree
        k: int
            k is an integer value key
        """

        # base case
        if x is None or k == x.key:
            return x

        # Recursively search tree
        if k < x.key:
            return self._search(x.left, k)
        else:
            return self._search(x.right, k)

    def _insert(self, insert_binnode: BinNode) -> None:
        """Insert node z into binary search tree

        Parameters
        ----------
        z, BinNode:
            Node for which key is to be inserted into binary search tree
        """
        y = None
        x = self.root

        while x is not None:
            y = x
            if insert_binnode.key < x.key:
                x = x.left
            else:
                x = x.right
        if y == None:
            self.root = insert_binnode
        elif insert_binnode.key < y.key:
            y.left = insert_binnode
        else:
            y.right = insert_binnode



    def _orderedTraversal(self, node, mylist):
        """"""
        if node != None:
            self._orderedTraversal(node.left, mylist)
            mylist.append(node.key)
            self._orderedTraversal(node.right, mylist)


class   BinNode:
    """Creates a node/subtree with a key and the left and right child of the node"""
    def __init__(self, key: int=None):
        """
        Parameters
        ----------
        key, int=None
            The key value of the node
        """
        self.key = key
        self.left = None
        self.right = None

    #skal bruges til at repræsentere knuder i træer
    #du skal ikke bruge array struktur
    #skal indeholde to andre BinNodes (knudens venstre og højre børn), med værdi None hvis barnet ikke findes.
    # skal også indeholde nøgle K, men ikke nødvendigt med forælder i dette projekt
    #
