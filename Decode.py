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
    
    def scan_frequency_table(self):
        with open(self.infile, 'rb') as f:
            bit_reader = BitReader(f)

            for i in range(256):
                frequency = bit_reader.readint32bits()
                self.frequency_table.append(frequency)
            bit_reader.close()
    
    def construct_huffman_tree(self):
        PriorityQ = []

        #Her laver vi leaf nodes som vi sætter inde i PriorityQ
        for symbol, frequency in enumerate(self.frequency_table):
            if frequency > 0:
                node = HuffmanNode(symbol, frequency)
                insert(PriorityQ, node)

        #Nu bygger vi huffman træet
        while len(PriorityQ) > 1:
            left_child = extractMin(PriorityQ)
            right_child = extractMin(PriorityQ)
            #Laver parent node ## ER I TVIVL OM DEN SKAL HAVE SYMBOL MED SIG??? se python kode her: https://www.geeksforgeeks.org/huffman-decoding/
            parent_frequency = left_child.frequency + right_child.frequency
            parent_node = HuffmanNode(None, parent_frequency)
            parent_node.left = left_child
            parent_node.right = right_child

            #Indsætter parent node tilbage i PriorityQ

            insert(PriorityQ, parent_node)
        
        #Laver rod til huffman træet med den sidste værdi
        self.huffman_tree_root = PriorityQ[0]

    def decode_encoded_data(self):
        bit_reader = BitReader(open(self.infile, 'rb'))
        bit_writer = BitWriter(open(self.outfile, 'wb'))
        current_node = self.huffman_tree_root

        #OrderedTraversal gennemføres nu på træet
        while True:
            bit = bit_reader.readbit()

            if bit is None:
                break

            ##Bestem om vi skal til venstre eller højre i træet
            if bit == 0:
                current_node = current_node.left
            else:
                current_node = current_node.right

            #Checker hvis current_node er None:
            if current_node is None:
                raise ValueError("Invalid encoded data or huffman tree construction")
            
            ##hvis vi har nået et leaf, så gemmer vi current_node
            if current_node.left is None and current_node.right is None:
                #skriver current til output fil
                bit_writer.writebit(1)
                bit_writer.writeint32bits(current_node.symbol)
                # genstarter og kør klar til næste iteration
                current_node = self.huffman_tree_root
        
        bit_writer.close()

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