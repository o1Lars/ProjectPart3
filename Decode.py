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

from bitIO import BitReader, BitWriter
import HuffmanTree
import sys
import os


class DecodeFile():
    """Creates an instance of the class DecodeFile. Works by creating an object, that reads a Huffman decoded file.
    First, it is assumed the first 256 bytes of the file is the frequency table that is needed to decode the Huff codes.
    Second, a Huffman tree binary tree object is created from the frequency table. Lastly, the rest of the file is read
    bit by bit and decoded from huffman codes to bytes and written to the outfile object."""

    def __init__(self, infile, outfile):
        """
        infile: Path object
            The absolute path to a file object
        outfile: Path object
            The absolute path to a file object
        """
        # store paths
        self.script_path = os.path.abspath(os.path.dirname(__file__))
        self.infile_path = rf'{self.script_path}\{infile}'
        self.outfile_path = rf'{self.script_path}\{outfile}'

        self.infile_byte_count = 0
        self.frequency_table = []
        self._scan_frequency_table()  # Get frequency table and byte count from infile

        # Recreate Huffman tree, comparable to the one used to encode the file
        self.huffyfied_table = HuffmanTree.HuffmanTreeCreator(self.frequency_table)
        self.huffman_tree = self.huffyfied_table.huffman_tree  # Instance of Huffman Tre

        # Decode rest of file and read original bytes to outfile
        self.decode_encoded_data()

    def _scan_frequency_table(self):
        """Scan input file and get frequency table and byte count of infile"""

        infile = self.infile_path
        frequency_table = self.frequency_table

        with open(infile, 'rb') as f:
            bit_reader = BitReader(f)

            # Get each frequency and store byte length
            for i in range(256):
                frequency = bit_reader.readint32bits()
                frequency_table.append(frequency)
                self.infile_byte_count += frequency
            bit_reader.close()

            # TODO DEL
            """for i, freq in enumerate(frequency_table):
                print(f"Byte {i}: Frequency {freq}")"""

    def decode_encoded_data(self):
        """Scan infile and decode the files huffyfied codes and write bytes to outfile"""

        infile_path = self.infile_path
        outfile_path = self.outfile_path
        byte_count = self.infile_byte_count
        huff_tree = self.huffman_tree
        print('bytes', byte_count)
        # Open infile
        with open(infile_path, 'rb') as in_file:
            print('file opened')
            bit_reader = BitReader(in_file)

            # Skip first 256 bytes (frequencies)
            for _ in range(256):
                bit_reader.readint32bits()

            # Open outfile
            with open(outfile_path, 'wb') as out_file:
                print('outfile opened')
                # write to file each byte
                for _ in range(byte_count):
                    decode_bits = True
                    current_node = huff_tree
                    print(current_node)
                    print('test')
                    while decode_bits:
                        bit = bit_reader.readbit()

                        # Traverse tree left/right until leaf is found
                        if bit is None:
                            break


                        # TODO check if needed below
                        """if current_node is None:
                            raise ValueError("Invalid encoded data or huffman tree")"""


                        if current_node.data.left is None and current_node.data.right is None:
                            print(f"Writing symbol: {current_node.data.root} | {bytes([current_node.data.root])}")
                            # Skriver en hel byte
                            out_file.write(bytes([current_node.data.root]))
                            decode_bits = False
                        elif bit == 0:
                            current_node = current_node.data.left
                        else:
                            current_node = current_node.data.right


if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    encoder = DecodeFile(input_file, output_file)
    print(encoder.infile_byte_count)
