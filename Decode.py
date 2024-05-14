"""
This module provides the Decode module. The module is designed to read a file, with the first part being a frequency
table. The module then decodes the rest of the file using Huffmans algorithm with the frequency table.

Requirements
------------
Python 3.7 or higher.
PQHeap.py
bitIO.py

Notes
-----
Module is created as part of the group project for the final exam of DS814 Algoritmer og Datastrukturer forår 2024.

Projektgrupe:
Chris Thorbjørn Eichmuller Vandborg
cvand15@student.sdu.dk

Lars Mogensen
lmoge23@student.sdu.dk

"""

# Create class for decoding
# readint32bits()
# create Huffmanstree as in encode module
# Get sum of numbers from frequency table
# Read file bit by bit
    # Use sum of frequency table to stop program (due to filler bits at the end)
# readBit(1)
# traverse Huffman tree while reading bits
    # when leaf is reached, write byte
    # write(bytes([n]))