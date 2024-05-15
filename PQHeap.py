# Rolf: Ikke godkendt. I skal genaflevere ved at maile en løsning til
# mig, som fikser problemet med extractMin (og evt. også polerer på
# insert). Send snarest muligt, og senest 10. maj.

"""
This module provides PQHeap, which creates an instance of the min-heap priority queue data structure

Requirements
------------
Python 3.7 or higher.

Notes
-----
Module is created as part of the group project for the final exam of DS814 Algoritmer og Datastrukturer forår 2024.

Projektgrupe:
Chris Thorbjørn Eichmuller Vandborg
cvand15@student.sdu.dk
cvand15

Lars Mogensen
lmoge23@student.sdu.dk


"""
from typing import List


def parent(i: int) -> int:
    """Return the index of the parent node of i from a heap like data structure

    i
        index of a node in heap like priority queue data structure, default is None.
    :return: int
    """
    return (i - 1) // 2


def left(i: int) -> int:
    """Return the index of the left child node of i from a heap like data structure

    i
        index of a node in heap like priority queue data structure, default is None.
    :return: int
    """
    return (2 * i) + 1


def right(i: int) -> int:
    """Return the index of the right child node of i from a heap like data structure

    i
        index of a node in heap like priority queue data structure, default is None.
    :return: int
    """
    return (2 * i) + 2


def build_min_heap(arr: List[int]) -> None:
    """Takes a regular python list and builds a min-heap data structure in place

    arr
        list of integers.
    :return: None. Reorders list in place.
    """

    heap_size = len(arr)

    for i in range(heap_size // 2, -1, -1):
        min_heapify(arr, i)


def min_heapify(arr: List[int], i: int) -> None:
    """Takes a regular python list and orders it as a min-heap data structure

    arr
        list of integers.
    i
        index of key
    :return: None. min-heapifies list in place.
    """

    # Initialize variables for tracking child/parent node(s)
    left_child = left(i)  # Left child index
    right_child = right(i)  # Right child index
    smallest = i

    # Check for its left child
    if left_child < len(arr) and arr[left_child] < arr[smallest]:
        smallest = left_child

    # Check for its right child
    if right_child < len(arr) and arr[right_child] < arr[smallest]:
        smallest = right_child

    # If the smallest element is not the current node, swap them and recursively call min_heapify
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, smallest)


def extractMin(priority_q: List[int]) -> int:
    """
    Return the key of the element with the least priority from a heap like priority queue data structure
    and keeps the list in min-heap structure

    priority_q
        A non-empty list of elements in a heap like data structure, Default is None
    :return: int
    """

# Rolf: Dette har intet med pseudokoden i bogen at gøre. Tiden for
# jeres kode er O(n), men skulle være O(log n).

# Pop er første element i en liste tager O(liste længde) tid. I skal:
#  - Gemme/kopiere elementet på plads 0 (så det kan returneres til sidst).
#  - Flytte sidste element op på plads 0.
#  - Lave pop() uden argument (og dermed på sidste plads)
#  - Udføre MinHeapify på roden, hvad der tager O(log n) tid (IKKE
#       BuildHeap, som tager O(n) tid).

    # NY extract min
    if len(priority_q) > 0:
        min_val = priority_q[0]
        priority_q[0] = priority_q[-1]
        priority_q.pop()
        min_heapify(priority_q, 0)
        return min_val
    else:
        return None

def insert(priority_q: List[int], num: int) -> List[int]:
    """
    Insert key into priority_q.

    priority_q
        A non-empty list of elements in a heap like data structure, Default is None
    num
        An integer value that will be inserted into priority_q, Default is None
    :return: None:
    """
    priority_q.append(num)

    i = len(priority_q) - 1
    while i > 0 and priority_q[parent(i)] > priority_q[i]:
        parent_index = parent(i)
        priority_q[i], priority_q[parent_index] = priority_q[parent_index], priority_q[i]
        i = parent_index

    return priority_q

def createEmptyPQ():
    """
    Return an empty heap like priority queue data structure

    :return: Empty priority queue
    """

    return []
