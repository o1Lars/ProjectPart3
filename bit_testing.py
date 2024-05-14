path = r'C:\Users\Chris\Documents\ProjectPart3\DelIIITestFilerTilUdlevering\DelIIITestFilerTilUdlevering\KingJamesBible.txt'


frequency_table = [0] * 256

with open(path, 'rb') as file:

    # Read file byte by byte
    byte = file.read(1)
    while byte:
        frequency_table[byte[0]] += 1  # Increase frequency of byte +1
        byte = file.read(1)  # Read next byte

    print(frequency_table)