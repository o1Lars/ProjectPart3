import bitIO
import sys
from PQHeap import insert, extractMin
from DictBinTree import DictBinTree

class MyEncode:
    def __init__(self, infile):
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
        frequency_table = [0] * 256

        #tilføjer bytes fra list_of_bytes til vores count_sort_table
        for byte in list_of_bytes:
            frequency_table[byte] += 1
        
        return frequency_table
    
    def huffman_tree_creator(self, frequency_table):
        #Initierer prioritetskø 
        priorityQ = []
        for i in range(256):
            insert(priorityQ, frequency_table[i]) #Indsætter for hyppighed

        #Huffman_tree_creator

        for i in range(len(priorityQ) - 1):
            #Extracter de to knuder med lowest frequency
            freq1 = extractMin(priorityQ)
            byte1 = i #Unpacker return value
            i += 1
            freq2 = extractMin(priorityQ)
            
            new_node = freq1 + freq2
            insert(priorityQ, new_node)
            root = priorityQ[0] 

        return priorityQ

    def huffman_code(self, huffman_tree):
        pass

class SymbolHolder:
    def __init__(self, symbol=None, single_frequency=0):
        self.freq = single_frequency
        self.symbol = symbol



        