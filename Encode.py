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
import sys
from bitIO import BitWriter
import HuffmanTree


class EncodeFile:
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile
        self.frequency_table = self.count_sort()
        self.huffman_tree = HuffmanTree.HuffmanTreeCreator(self.frequency_table)
        self.huffman_codes_list = self.huffman_tree.huffman_codes


    # trin 1 - hyppighedstabel. Filen skal læses 1 byte ad gangen.
    def count_sort(self):
        """Scans a file and creates a  frequency table of individual bytes from the file (0-255)"""

        frequency_table = [0] * 256

        with open(self.infile, 'rb') as file:
            # Read file byte by byte
            byte = file.read(1)
            while byte:
                frequency_table[byte[0]] += 1  # Increase frequency of byte +1
                byte = file.read(1)  # Read next byte

        return frequency_table

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


if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    encoder = EncodeFile(input_file, output_file)
    encoder.write_frequency_table()