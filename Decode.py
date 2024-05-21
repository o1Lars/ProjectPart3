from bitIO import BitReader
import HuffmanTree
import sys
import os


class DecodeFile:
    def __init__(self, infile, outfile):
        self.script_path = os.path.abspath(os.path.dirname(__file__))
        self.infile_path = rf'{self.script_path}\{infile}'
        self.outfile_path = rf'{self.script_path}\{outfile}'

        self.infile_byte_count = 0
        self.frequency_table = []
        self.huffman_tree = None

        # Scan frequency table and decode the file
        self.scan_frequency_table_and_decode()

    def scan_frequency_table_and_decode(self):
        infile = self.infile_path
        with open(infile, 'rb') as f:
            bit_reader = BitReader(f)

            # Construct the frequency table and the Huffman tree
            for i in range(256):
                frequency = bit_reader.readint32bits()
                self.frequency_table.append(frequency)
                self.infile_byte_count += frequency

            # Reconstruct Huffman Tree from the frequency table
            huffman_tree_creator = HuffmanTree.HuffmanTreeCreator(self.frequency_table)
            self.huffman_tree = huffman_tree_creator.huffman_tree

            # Decode the rest of the file using the Huffman tree
            with open(self.outfile_path, 'wb') as out_file:
                bit_count = 0
                current_node = self.huffman_tree

                while bit_count < self.infile_byte_count:
                    bit = bit_reader.readbit()
                    if bit is None:
                        break

                    if bit == 0:
                        current_node = current_node.data.left
                    else:
                        current_node = current_node.data.right

                    if current_node.data.left is None and current_node.data.right is None:
                        out_file.write(bytes([current_node.data.root]))
                        current_node = self.huffman_tree  # Reset to the root for the next character
                        bit_count += 1

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    decoder = DecodeFile(input_file, output_file)
    print(decoder.infile_byte_count)
