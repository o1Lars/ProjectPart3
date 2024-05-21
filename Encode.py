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
from bitIO import BitWriter, BitReader # TODO To forskellige bitIO imports, fix import og i koden
import HuffmanTree
import sys
import os


class EncodeFile:
    """Creates an instance of the class EncodeFile. Works by creating an object, that reads a file byte-wise twice.
    First, the file is read once and each byte frequency is stored in a 256 element frequency table. Then the instance
    utilizes the frequency table to create an Huffman tree instance, which is used to encode the file with Huffman
    codes. Lastly, the Huffman codes a used to write the new coded bit representation to the output file."""

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

        # Count frequencies, create Huffman Tree and codes list
        self.frequency_table = self.count_sort()
        self.huffman_tree = HuffmanTree.HuffmanTreeCreator(self.frequency_table)  # Instance of Huffman Tree
        self.huffman_codes_list = self.huffman_tree.huffman_codes  # List of bytes Huffman coded

        # Write frequency table and new huffyfied bytes to outfile
        self.write_huffyfied_bytes()

        # Test decoding directly in encoding
        # TODO Remember del
        self.decode_encoded_data()

    def count_sort(self):
        """Scans a file and return a frequency table of individual bytes from the file (0-255)"""

        infile = self.infile_path

        frequency_table = [0] * 256

        with open(infile, 'rb') as file:
            # Read file byte by byte and +1 frequency of corresponding byte
            byte = file.read(1)
            while byte:
                frequency_table[byte[0]] += 1
                byte = file.read(1)

        return frequency_table

    def write_huffyfied_bytes(self):
        """Scan infile byte for byte and write corresponding Huffman coded byte to outfile."""

        infile_path = self.infile_path
        outfile_path = self.outfile_path
        huff_codes = self.huffman_codes_list
        frequency_table = self.frequency_table

        # Open infile & out file
        with open(infile_path, 'rb') as in_file:
            with open(outfile_path, 'wb') as out_file:

                # Read file byte by byte
                byte = in_file.read(1)
                bit_writer = BitWriter(out_file)

                # Write frequency table to outfile
                for frequency in frequency_table:
                    print(frequency)
                    bit_writer.writeint32bits(frequency)


                # Code byte as huffman code
                while byte:
                    # TODO del
                    # bit list
                    bit_list = []
                    huffyfied_byte = huff_codes[byte[0]]
                    for bit in huffyfied_byte:
                        bit = int(bit)
                        bit_list.append(bit)
                        bit_writer.writebit(bit)
                    print(f"byte: {byte[0]} | huffman bits: {bit_list} | huff code: {huff_codes[byte[0]]}") # TODO DEL
                    byte = in_file.read(1)
                bit_writer.close()

    def decode_encoded_data(self):
        """Scan infile and decode the files huffyfied codes and write bytes to outfile"""

        infile_path = self.outfile_path
        outfile_path = r"C:\Users\Lars\Documents\Data Science\2 Semester\10 ECTS Algoritmer og Datastrukturer\ProjektDel3\wojak.jfif"
        byte_count = 11
        huff_tree = self.huffman_tree.huffman_tree

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
                    bit_list = [] # TODO slet, kun til test

                    while decode_bits:

                        bit = bit_reader.readbit()
                        #bit_list.append(bit) # TODO Slet kun til test
                        # Traverse tree left/right until leaf is found
                        if bit is None:
                            break
                        bit_list.append(bit) # TODO Slet kun til test


                        # TODO check if needed below
                        """if current_node is None:
                            raise ValueError("Invalid encoded data or huffman tree")"""


                        if bit == 0:
                            current_node = current_node.data.left
                        else:
                            current_node = current_node.data.right

                        if current_node.data.left is None and current_node.data.right is None:
                            print(f"Writing symbol: {current_node.data.root} | {bytes([current_node.data.root])} | bit list: {bit_list}")
                            # Write the decoded byte to output file
                            out_file.write(bytes([current_node.data.root]))
                            decode_bits = False


# TODO
# Slet nedenstående function. Skulle blot tjekke, at bits korrekt blev tilføjet til outfile
def test_out():
    file = r"C:\Users\Lars\Documents\Data Science\2 Semester\10 ECTS Algoritmer og Datastrukturer\ProjektDel3\wojak.jfif"

    with open(file, 'rb') as f:
        bit_reader = bitIO.BitReader(f)
        for i in range(100):
            print(bit_reader.readbit())


if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    encoder = EncodeFile(input_file, output_file)
    print(encoder.frequency_table)