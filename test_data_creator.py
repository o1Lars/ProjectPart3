from PQHeap import insert, extractMin
from bitIO import BitWriter
from Decode import HuffmanNode

# Sample data to encode
data = "hello world"

# Create a frequency table
frequency_table = {}
for char in data:
    if char in frequency_table:
        frequency_table[char] += 1
    else:
        frequency_table[char] = 1

# Build the Huffman tree
PriorityQ = []
for symbol, frequency in frequency_table.items():
    node = HuffmanNode(symbol, frequency)
    insert(PriorityQ, node)

while len(PriorityQ) > 1:
    left_child = extractMin(PriorityQ)
    right_child = extractMin(PriorityQ)
    parent_frequency = left_child.frequency + right_child.frequency
    parent_node = HuffmanNode(None, parent_frequency)
    parent_node.left = left_child
    parent_node.right = right_child
    insert(PriorityQ, parent_node)

huffman_tree_root = PriorityQ[0]

# Encode the data
encoded_data = ""
for char in data:
    encoded_data += encode_char(huffman_tree_root, char)

# Write the frequency table and encoded data to a file
with open("encoded_test_file.bin", "wb") as f:
    bit_writer = BitWriter(f)
    
    # Write the frequency table
    for symbol, frequency in frequency_table.items():
        bit_writer.writeint32bits(frequency)
    
    # Write a marker to separate frequency table from encoded data
    bit_writer.writeint32bits(-1)
    
    # Write the encoded data
    for bit in encoded_data:
        bit_writer.writebit(int(bit))
    
    bit_writer.close()

print("Encoded data saved to 'encoded_test_file.bin'")
