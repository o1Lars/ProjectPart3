import unittest
from Encode import EncodeFile
from Encode import SymbolHolder

class TestEncodeFile(unittest.TestCase):
    def test_count_sort(self):
        sample_bytes = b'\x00\x01\x02\x02\x03\x03\x03\x04\x05'
        with open('sample_file.bin', 'wb') as f:
            f.write(sample_bytes)

        # Open the sample file for reading in binary mode
        with open('sample_file.bin', 'rb') as f:
            # Create an instance of EncodeFile
            your_instance = EncodeFile(f)

            # Call the count_sort method
            actual_symbol_holder = your_instance.count_sort()

        # Assert the correctness of the count_sort_table
        expected_count_sort_table = [1, 1, 2, 3, 1, 1] + [0] * 250
        expected_symbol_holders = []
        expected_symbol_holders.append(SymbolHolder(b'\x00', 1))
        expected_symbol_holders.append(SymbolHolder(b'\x01', 1))
        expected_symbol_holders.append(SymbolHolder(b'\x02', 2))
        expected_symbol_holders.append(SymbolHolder(b'\x03', 3))
        expected_symbol_holders.append(SymbolHolder(b'\x04', 1))
        expected_symbol_holders.append(SymbolHolder(b'\x05', 1))
        for i in range(250):
            expected_symbol_holders.append(SymbolHolder())

        for i in range(len(expected_symbol_holders)):
            self.assertEqual(expected_symbol_holders[i].symbol, actual_symbol_holder[i].symbol)
            self.assertEqual(expected_symbol_holders[i].freq, actual_symbol_holder[i].freq)

        # Clean up the sample file
        import os
        os.remove('sample_file.bin')
   
    def test_huffman_tree_creator_creates_expected_tree(self):
        sample_bytes = b'\x00\x01\x02\x02\x03\x03\x03\x04\x05'
        with open('sample_file.bin', 'wb') as f:
            f.write(sample_bytes)

        # Open the sample file for reading in binary mode
        with open('sample_file.bin', 'rb') as f:
            # Create an instance of EncodeFile
            your_instance = EncodeFile(f)

            # Call the count_sort method
            count_sort_table = your_instance.count_sort()

            actual_huffman_tree = your_instance.huffman_tree_creator(count_sort_table)
        
        # Assert the correctness
        expected_huffman_tree = [9, 5, 4, 2, 3, 2, 2, 0, 5, 1, 4]
        self.assertEqual(expected_huffman_tree, actual_huffman_tree)







if __name__ == '__main__':
    unittest.main()
