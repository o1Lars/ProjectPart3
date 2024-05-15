from random import randint
from Element import Element
import DictBinTree
import PQHeap

frequency_table = [randint(0,10) for i in range(10)]

def _convert_int_to_Elements(f_table: list) -> list:
    """Return a list of Elements created from a list of frequencies."""

    elements = []

    for number in f_table:
        elements.append(Element(number, DictBinTree.BinNode()))       # populate list with Elements

    return elements

elements = _convert_int_to_Elements(frequency_table)
print([e.key for e in elements])

# rearrange elements into min priority queue
PQHeap.build_min_heap(elements)
print([e.key for e in elements])

def huffman_coding(C: list) -> int:

    n = len(C)
    Q = C

    for i in range(n - 1):
        z = DictBinTree.BinNode()   # allocate new node
        x = PQHeap.extractMin(Q)
        y = PQHeap.extractMin(Q)
        z.left = x
        z.right = y
        z.key = x.key + y.key
        PQHeap.insert(Q, Element(z.key, z))
        print(i)
    return PQHeap.extractMin(Q)

code = huffman_coding(elements)
print(code.data.left.key)

def _orderedTraversal(node, mylist):
    """"""

    if node is not None:
        print(node)
        _orderedTraversal(node.data.left, mylist)
        mylist.append(node.key)
        _orderedTraversal(node.data.right, mylist)

    return mylist

mylist = []
print(_orderedTraversal(code, mylist))