# Eksempelprogram, som viser brugen af Element sammen med PQHeap.py fra del I.

import sys
import PQHeap # Dette er gruppens PQHeap.py fra del I.
from Element import Element

pq = PQHeap.createEmptyPQ() # Opret en tom prioritetskÃ¸.

for line in sys.stdin:
    # Man opretter et nyt element med kaldet Element(key,data), som
    # sÃ¦tter vÃ¦rdier i dets felter key og data. Dette vises her med et
    # heltal som key og en tilfÃ¦ldig string som data. I del III skal
    # data i stedet vÃ¦re trÃ¦er (se projektbeskrivelsen for del III).
    e = Element(int(line),"Some appropriate data")
    # IndsÃ¦t det nye Element i prioritetskÃ¸en.
    PQHeap.insert(pq,e)

while len(pq) > 0:
    # Udtag det Element fra prioritetskÃ¸en, som har mindste key.
    e = PQHeap.extractMin(pq)
    # TilgÃ¥ og print dets felter key og data.
    extractedKey = e.key
    extractedData = e.data
    print(extractedKey)
    print(extractedData)