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
import sys
from PQHeap import insert, extractMin
from bitIO import BitReader, BitWriter
from DictBinTree import DictBinTree
from HuffmanTree import HuffmanTreeCreator

class HuffmanNode:
    def __init__(self, symbol=None, frequency=0):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

class Decode():
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile
        self.frequency_table = []
        self.huffman_tree_root = None
        self.decoded_data = ""
        self.huffman_tree_creator = None
    
    def scan_frequency_table(self):
        with open(self.infile, 'rb') as f:
            bit_reader = BitReader(f)

            for i in range(256):
                frequency = bit_reader.readint32bits()
                self.frequency_table.append(frequency)
            bit_reader.close()

            for i, freq in enumerate(self.frequency_table):
                print(f"Byte {i}: Frequency {freq}")
    
    def construct_huffman_tree(self):
        self.huffman_tree_creator = HuffmanTreeCreator(self.frequency_table)
        # PriorityQ = []

        # #Her laver vi leaf nodes som vi sætter inde i PriorityQ
        # for symbol, frequency in enumerate(self.frequency_table):
        #     if frequency > 0:
        #         node = HuffmanNode(symbol, frequency)
        #         insert(PriorityQ, node)

        # #Nu bygger vi huffman træet
        # while len(PriorityQ) > 1:
        #     left_child = extractMin(PriorityQ)
        #     right_child = extractMin(PriorityQ)
        #     #Laver parent node ## ER I TVIVL OM DEN SKAL HAVE SYMBOL MED SIG??? se python kode her: https://www.geeksforgeeks.org/huffman-decoding/
        #     parent_frequency = left_child.frequency + right_child.frequency
        #     parent_node = HuffmanNode(None, parent_frequency)
        #     parent_node.left = left_child
        #     parent_node.right = right_child

        #     #Indsætter parent node tilbage i PriorityQ

        #     insert(PriorityQ, parent_node)
        
        # #Laver rod til huffman træet med den sidste værdi
        # self.huffman_tree_root = PriorityQ[0]

    def decode_encoded_data(self):
        bit_reader = BitReader(open(self.infile, 'rb'))
        output_file = open(self.outfile, 'wb')
        root_node = self.huffman_tree_creator.huffman_tree.data
        current_node = root_node
        total_bytes = sum(self.frequency_table)
        bytes_decoded = 0

        for i in range(256):
            bit_reader.readint32bits()
        
        while bytes_decoded < total_bytes:
            bit = bit_reader.readbit()

            if bit is None:
                break

            if bit == 0:
                current_node = current_node.left.data
            else:
                current_node = current_node.right.data
            
            if current_node is None:
                raise ValueError("Invalid encoded data or huffman tree")
            
            print(f"Read bit: {bit}, traversing to node: {current_node.root if current_node else 'None'}")
            
            if current_node.left is None and current_node.right is None:
                print(f"Writing symbol: {current_node.root}")
                # Skriver en hel byte
                output_file.write(bytes([current_node.root]))
                bytes_decoded += 1
                current_node = self.huffman_tree_creator.huffman_tree.data
            
        output_file.close()
        bit_reader.close()

    def do_decode(self):
        self.scan_frequency_table()
        self.construct_huffman_tree()
        self.decode_encoded_data()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python Decode.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
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