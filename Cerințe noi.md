2. Încărcarea CSV sau JSON cu schemă explicită
•	Plasați setul de date original în data/raw. Păstrați formatul primit: CSV sau JSON.
•	Definiți explicit schema coloanelor și încărcați datele într-un DataFrame PySpark. Nu utilizați inferSchema în varianta finală.
•	Afișați schema, primele înregistrări și numărul total de rânduri.
•	Alegeți o filtrare și o agregare relevante pentru setul vostru de date. Aceleași operații vor fi executate pentru toate formatele.
3. Salvarea și recitirea datelor în Parquet
•	Salvați DataFrame-ul în data/parquet, în modul overwrite.
•	Citiți din nou datele din Parquet și verificați că numărul de rânduri și schema corespund datelor inițiale.
4. Compararea dimensiunilor și a timpului
•	Măsurați dimensiunea directorului sursă și a directorului Parquet.
•	Calculați diferența în MB și procentul de spațiu economisit sau suplimentar ocupat de Parquet.
•	Măsurați în cod timpul pentru citire, filtrare și agregare asupra sursei și a datelor Parquet.
•	Executați exact aceeași interogare și declanșați procesarea prin count() sau collect(). Repetați fiecare test de trei ori și calculați mediana.
Model pentru măsurarea timpului
from time import perf_counter
from statistics import median
``` 
def measure(operation, repeats=3):
    times = []
    for _ in range(repeats):
        start = perf_counter()
        operation()  # use count() or collect()
        times.append(perf_counter() - start)
    return times, median(times)
```
5. Salvarea unui Parquet partiționat
•	Alegeți o coloană cu un număr rezonabil de valori distincte, de exemplu an, lună, regiune sau categorie. Nu utilizați un identificator unic.
•	Salvați datele în data/parquet_partitioned folosind partitionBy.
•	Măsurați aceeași interogare și pentru Parquet partiționat, folosind trei execuții și mediana.
6. Verificarea partițiilor și PartitionFilters
•	Examinați directoarele create și explicați legătura dintre numele directoarelor și valorile coloanei de partiționare.
•	Executați aceeași filtrare pe Parquet nepartiționat și partiționat. Folosiți explain("formatted") și identificați PartitionFilters.
7. Crearea unui tabel Delta partiționat
•	Salvați DataFrame-ul în data/delta, în format Delta și cu aceeași coloană de partiționare.
•	Citiți tabelul Delta și verificați schema și numărul de rânduri.
•	Măsurați aceeași interogare și pentru Delta Lake, folosind trei execuții și mediana.
8. Inspectarea fișierelor Delta
•	Verificați directoarele de partiții, fișierele Parquet și directorul _delta_log.
•	Arătați că datele tabelului Delta sunt păstrate în fișiere Parquet, iar _delta_log păstrează istoricul tranzacțiilor.
9. Crearea versiunilor Delta
•	Creați cel puțin patru versiuni ale tabelului: încărcarea inițială, un append, un update și un delete. Modificările trebuie să poată fi demonstrate prin interogări.
10. Istoricul și citirea versiunii 0
•	Afișați istoricul tabelului Delta și identificați operația corespunzătoare fiecărei versiuni.
•	Citiți versiunea 0 cu versionAsOf și comparați-o cu versiunea curentă prin numărul de rânduri și câteva înregistrări afectate.

# Concluzia

În notebook, prezentați o comparație finală între formatul sursă, Parquet, Parquet partiționat și Delta Lake. Includeți dimensiunea pe disc, mediana timpului de citire, mediana filtrării, suportul pentru partiționare și existența istoricului versiunilor. Concluzia trebuie să fie bazată pe valorile măsurate, nu doar pe definiții teoretice.

Ce prezentați la următorul laborator
1. 	Notebook-ul executabil, cu toate celulele rulate și fără erori.
2. Directoarele data/parquet, data/parquet_partitioned și data/delta.
3. Comparația măsurată a dimensiunilor și timpilor.
4. Structura partițiilor și planul de execuție care conține PartitionFilters.
5. Istoricul Delta și citirea versiunii 0 prin time travel.
6. O demonstrație scurtă în care explicați alegerile și concluziile obținute.
