import bitIO
import sys
from PQHeap import insert, extractMin

class Encode:
    def __init__(self):
        self.infile = infile
        
    # trin 1 - hyppighedstabel. Filen skal læses 1 byte ad gangen.
    def count_sort(self):
        #først læs filen som bytes
        list_of_bytes = []
        byte = self.infile.read(1)
        while byte:
            list_of_bytes.append(byte[0]) #Laver bytestring om til heltal
            byte = self.infile.read(1)
        
        #Laver hyppighedstabel med 256 elementer
        count_sort_table = [0] * 256
        return count_sort_table


    def huffman_algo(self, count_sort_table):
        priorityQ = []
        #For alle bytes, også dem med 0
        for i in range(256):
            insert(priorityQ, (count_sort_table[i], i)) #Indsætter for hyppighed og byteværdi

        #Huffman algo

        for i in range(len(priorityQ) - 1):
            #Extracter de to knuder med lowest frequency
            freq1 = extractMin(priorityQ)
            byte1 = i #Unpacker return value
            i += 1
            freq2 = extractMin(priorityQ)
            byte2 = i 
            

            #Laver nye knuder
            new_node = freq1 + freq2
            insert(priorityQ, new_node)
            root = priorityQ[0]

        return root

infile = open(sys.argv[1], 'rb')
outfile = open(sys.argv[2], 'wb')
bitstreamin = bitIO.BitReader(infile)
bitstreamout = bitIO.BitWriter(outfile)
i = bitstreamin.readint32bits()
print(i)
bitstreamout.writeint32bits(i)

encoder = Encode()
count_table = encoder.count_sort()
huffman_tree = encoder.huffman_algo(count_table)