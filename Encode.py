"""
This module provides the Encode module. The module is designed to read a file, with the first part being a frequency
table. The module then decodes the rest of the file using Huffmans algorithm with the frequency table.

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

import bitIO
import sys
from PQHeap import insert, extractMin
from DictBinTree import DictBinTree
from Element import Element
from bitIO import BitWriter

class EncodeFile:
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile
        self.frequency_table = self.count_sort()


    # trin 1 - hyppighedstabel. Filen skal læses 1 byte ad gangen.
    def count_sort(self):
        """Scans a file and creates a  frequency table of individual bytes from the file (index 0-255)"""

        frequency_table = [0] * 256

        # Read file byte by byte
        byte = self.infile.read(1)
        while byte:
            frequency_table[byte[0]] += 1   # Increase frequency of byte +1
            byte = self.infile.read(1)      # Read next byte
    
        return frequency_table

    def huffman_tree_creator(self, frequency_table):
        # Initierer prioritetskø
        priorityQ = []
        for i in range(256):
            insert(priorityQ, frequency_table[i])  # Indsætter for hyppighed

        # Huffman_tree_creator

        for i in range(len(priorityQ) - 1):
            # Extracter de to knuder med lowest frequency
            freq1 = extractMin(priorityQ)
            byte1 = i  # Unpacker return value
            i += 1
            freq2 = extractMin(priorityQ)

            new_node = freq1 + freq2
            insert(priorityQ, new_node)
            root = priorityQ[0]

        return priorityQ

    def huffman_code(self, huffman_tree):
        pass

    def write_frequency_table(self):
        """Writes requency table to output file."""
        with open(self.outfile, 'wb') as f:
            bit_writer = BitWriter(f)
            for frequency in self.frequency_table:
                bit_writer.writeint32bits(frequency)
            bit_writer.close()

class SymbolHolder:
    def __init__(self, symbol=None, single_frequency=0):
        self.freq = single_frequency
        self.symbol = symbol


if __name__ == 'main':
    input_file = 'placeHolder'  # TODO
    output_file = 'placeHolder'  # TODO
    encoder = EncodeFile(input_file, output_file)
    encoder.write_frequency_table()
