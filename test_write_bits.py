from bitIO import BitWriter, BitReader
from random import randint

frequency_table = [0] * 256 #[randint(0, 1) for i in range(10)]
frequency_table[5] = 1
print(frequency_table)

def write_frequency_table():
    """Writes frequency table to output file."""

    outfile = r"C:\Users\Chris\Documents\ProjectPart3\test_write_bits.txt"

    with open(outfile, 'wb') as f:
        bit_writer = BitWriter(f)
        for frequency in frequency_table:
            bit_writer.writeint32bits(frequency)
        bit_writer.close()
def _scan_frequency_table():
    infile = r"C:\Users\Chris\Documents\ProjectPart3\test_one_enc.txt"
    table = []
    with open(infile, 'rb') as f:
        bit_reader = BitReader(f)

        # Get each frequency and store byte length
        for i in range(256):
            frequency = bit_reader.readint32bits()
            table.append(frequency)
        bit_reader.close()

    print(table)

#write_frequency_table()
_scan_frequency_table()