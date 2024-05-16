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
from bitIO import BitReader

class Decode():
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile
        self.frequency_table = []
        self.huffman_tree = None
    
    def scan_frequency_table(self):
        with open(self.infile, 'rb') as f:
            bit_reader = BitReader(f)

            for i in range(256):
                frequency = bit_reader.readint32bits()
                self.frequency_table.append(frequency)
            bit_reader.close()
    
    def construct_huffman_tree(self):
        pass

    def decode_encoded_data(self):
        pass

    def do_decode(self):
        self.scan_frequency_table()
        self.construct_huffman_tree()
        self.decode_encoded_data()

if __name__ == "__main__":
    input_file = "Placeholder"
    output_file = "placeholder"
    decoder = Decode(input_file, output_file)
    decoder.do_decode()

        


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