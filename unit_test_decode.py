import unittest
from unittest.mock import MagicMock, mock_open
from Decode import Decode

class TestDecode(unittest.TestCase):
    def setUp(self):
        self.input_file = "small_test_file.txt"
        self.output_file = "test_output2.txt"
    
    def tearDown(self):
        pass
    
    def test_decode_encoded_data(self):
        # Mocking the BitReader and BitWriter
        with unittest.mock.patch('bitIO.BitReader') as mock_bit_reader, \
             unittest.mock.patch('bitIO.BitWriter') as mock_bit_writer:
            
            # Mocking the BitReader's readbit method
            mock_readbit = MagicMock(side_effect=[0, 1, None])  # Simulating 010 as input data
            mock_bit_reader.return_value.readbit = mock_readbit

            # Mocking the frequency table
            mock_frequency_table = [1, 1, 0, 0]  # Simulating a frequency table
            
            # Initializing the Decode object
            decode = Decode(self.input_file, self.output_file)
            decode.frequency_table = mock_frequency_table
            
            # Mocking the constructed Huffman tree
            mock_root_node = MagicMock()
            decode.huffman_tree_root = mock_root_node
            
            # Running the decode_encoded_data method
            decode.decode_encoded_data()
            
            # Asserting the writebit and writeint32bits calls on the BitWriter
            mock_bit_writer.return_value.writebit.assert_has_calls([MagicMock(0), MagicMock(1), MagicMock(1)])
            mock_bit_writer.return_value.writeint32bits.assert_called_once_with(1)  # Asserting for the leaf symbol

if __name__ == '__main__':
    unittest.main()
