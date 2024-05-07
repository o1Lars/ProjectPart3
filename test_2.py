import bitIO
import sys
from PQHeap import insert, extractMin
from Encode import MyEncode


# Test program to:
#
#   1) Demonstrate standard usage of bitIO.BitReader and
#      bitIO.BitWriter from the handed-out library bitIO. This usage
#      can be reused in your project part III code.
#
#   2) Demonstrate that a file must contain an integral number of
#      bytes, that is, an multiple of eight bits. Thus, the library
#      may need to add bits to the output when closing an output file.
#      Padding with zero bits is the choice made in the library.
#
# Run the program on some small text file (containing at least four
# bytes, preferably a few more) by
# 
#   python test.py infilename outfilename
# 
# This will copy the infile to outfile, while adding the character '@'
# to the end of it (after any newline, if the file ends with this),
# and along the way write some multi-digit integer and some bits to
# the screen. Read comments below to understand WHY this should be the
# behavior.

# Open input and output files, using binary mode (reading/writing bytes).
infile = open(sys.argv[1], 'rb')
outfile = open(sys.argv[2], 'wb')

# Create the BitReader/BitWriter using these files as input/output.
bitstreamin = bitIO.BitReader(infile)
bitstreamout = bitIO.BitWriter(outfile)

# Create an instance of MyEncode
encoder = MyEncode(infile)

# Generate frequency table using count_sort
frequency_table = encoder.count_sort()

# Perform Huffman encoding algorithm
huffman_tree = encoder.huffman_tree_creator(frequency_table)

# Now encode the input file using the Huffman tree and write to the output file
# You need to implement this part based on your Huffman encoding logic.

# Close the input and output files
bitstreamout.close()
bitstreamin.close()
