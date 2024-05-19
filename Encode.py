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
    """Creates an instance of the class EncodeFile. Works by creating an object, that reads a file byte-wise twice.
    First, the file is read once and each byte frequency is stored in a 256 element frequency table. Then the instance
    utilizes the frequency table to create an Huffman tree instance, which is used to encode the file with Huffman
    codes. Lastly, the Huffman codes a used to write the new coded bit representation to the output file."""
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile
        self.frequency_table = self.count_sort()
        self.huffman_tree = HuffmanTree.HuffmanTreeCreator(self.frequency_table)    # Instance of Huffman Tree
        self.huffman_codes_list = self.huffman_tree.huffman_codes                   # List of bytes Huffman coded

        """
        infile: Path object
            The absolute path to a file object
        outfile: Path object
            The absolute path to a file object
        """

    def count_sort(self):
        """Scans a file and return a frequency table of individual bytes from the file (0-255)"""

        frequency_table = [0] * 256

        with open(self.infile, 'rb') as file:
            # Read file byte by byte and +1 frequency of corresponding byte
            byte = file.read(1)
            while byte:
                frequency_table[byte[0]] += 1
                byte = file.read(1)

        return frequency_table

    def write_frequency_table(self):
        """Writes frequency table to output file."""
        with open(self.outfile, 'wb') as f:
            bit_writer = BitWriter(f)
            for frequency in self.frequency_table:
                bit_writer.writeint32bits(frequency)
            bit_writer.close()

# TODO
# Bruger vi nedenstående class, eller skal den slettes?
class SymbolHolder:
    def __init__(self, symbol=None, single_frequency=0):
        self.freq = single_frequency
        self.symbol = symbol


if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    encoder = EncodeFile(input_file, output_file)
    encoder.write_frequency_table()