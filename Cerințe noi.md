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

---

# Partea nouă a laboratorului 1: Ingestie și analiză Big Data cu DWH, streaming și dashboarduri

Realizați un proiect individual folosind dataset-ul ales anterior, cu o dimensiune de minimum 2 GB (recomandat: 2–5 GB). Continuați în același notebook Colab/Jupyter. Etapele 1 și 2 de mai jos reiau lucrări deja atribuite: păstrați codul și rezultatele existente și reutilizați-le, fără să refaceți sau să înlocuiți implementarea.

## Ce există deja în notebook

| Domeniu | Implementat în notebook | Ce trebuie completat pentru partea nouă |
|---|---|---|
| Ingestie și stocare (Etapele 1–2 de mai jos) | Sursă CSV, schemă explicită, afișarea schemei și eșantionului, numărarea rândurilor; scriere și recitire Parquet, Parquet partiționat și Delta partiționat, cu verificări de schemă și număr de rânduri. | Reutilizați celulele și rezultatele. Asigurați-vă că prezentarea precizează sursa, linkul, dimensiunea și semnificația datelor și că dataset-ul îndeplinește pragul de minimum 2 GB. Păstrați comparația și verificările existente; adăugați numai informația sau măsurătoarea care lipsește. |
| Comparație și Delta (Etapele 1–2 de mai jos) | Tabel de comparație pentru sursă, Parquet, Parquet partiționat și Delta; mediane pentru citire, filtrare și agregare; verificarea partițiilor și `PartitionFilters`; istoric Delta cu încărcare inițială, append, update și delete și comparație cu versiunea 0. | Reutilizați rezultatele și concluziile deja generate. Nu recreați aceste experimente decât dacă este necesar pentru a obține rezultate valide în mediul de prezentare. |
| Curățare și transformare (Etapa 3 de mai jos) | Verificări pentru valori lipsă și duplicate, tratarea lor, conversia/tipizarea datelor, derivarea anului, agregări descriptive și un exemplu de join cu date despre districte. | Extindeți etapa existentă, fără a o rescrie: adăugați raportul clar înainte/după și verificările pentru valori sau tipuri invalide, cel puțin încă o coloană derivată dacă este necesar, filtrul justificat, salvarea separată în `data/processed_delta`, analize Spark SQL și graficele cerute. |
| DWH, OLAP, streaming și dashboard | Nu sunt implementate în notebook-ul actual: nu există schemă stea cu operații OLAP, flux Kafka–Spark Structured Streaming–MongoDB sau dashboard alimentat din MongoDB. | Sunt componente noi și trebuie adăugate în continuarea notebook-ului, fără a modifica rezultatele etapelor existente. |

În notebook-ul existent sunt raportate 8.645.530 de rânduri, iar comparația măsoară sursa la aproximativ 2,29 GB. Reconfirmați dimensiunea efectivă a dataset-ului folosit la prezentare. Codul existent recreează directorul generat `data/delta` pentru a porni istoricul experimentului de la versiunea 0; nu folosiți acel director pentru date pe care doriți să le păstrați și nu îl ștergeți în etapele noi. Pentru datele curățate folosiți calea separată `data/processed_delta`, iar pentru DWH și streaming folosiți tabele, directoare și variabile dedicate.

Toate cerințele de mai jos sunt obligatorii, cu excepția celor marcate opționale. Evaluarea finală se face prin prezentarea proiectului, demonstrarea rezultatelor și răspunsuri la întrebări.

## 1. Ingestia și stocarea datelor

Reutilizați implementarea și rezultatele existente pentru această etapă. Nu recreați celulele de ingestie, benchmark, partiționare și istoric Delta doar pentru a dubla conținutul. Completați următoarele numai dacă informația nu este deja prezentată:

- Indicați sursa și linkul dataset-ului, dimensiunea lui și semnificația datelor. Dataset-ul trebuie să aibă minimum 2 GB; dimensiunea recomandată este 2–5 GB.
- Păstrați cele patru variante: CSV/JSON original, Parquet, Parquet partiționat și Delta Lake partiționat. Verificați schema și numărul de rânduri după salvare și recitire.
- Prezentați un tabel comparativ pentru cele patru variante: spațiul ocupat și timpii pentru citire, aceeași filtrare și aceeași agregare. Pentru timpi, utilizați mediana a trei execuții. Calculați diferența de spațiu față de sursă.
- Demonstrați partițiile și `PartitionFilters`. Pentru Delta Lake, prezentați minimum patru versiuni: încărcarea inițială, append, update și delete. Afișați istoricul și comparați versiunea 0 cu versiunea curentă.

**De prezentat:** tabelul comparativ, planul de execuție, istoricul Delta și o concluzie bazată pe măsurători despre avantajele și limitele formatelor.

## 2. Curățarea, transformarea și analiza descriptivă

Continuați celulele existente de curățare și transformare; nu eliminați sau înlocuiți verificările, rezultatele și join-ul deja prezentate.

- Verificați valorile lipsă, duplicatele și valorile sau tipurile invalide. Prezentați regulile aplicate și un tabel înainte/după cu numărul de rânduri afectate. Dacă datele sunt curate pentru una dintre verificări, demonstrați acest lucru prin rezultate.
- Realizați conversiile necesare, minimum două coloane derivate, un filtru justificat și o agregare. Includeți un join dacă este necesar; în caz contrar, explicați de ce nu se aplică. Join-ul cu informațiile despre districte deja existent poate fi păstrat și folosit dacă este potrivit analizei.
- Salvați rezultatul curățat separat în `data/processed_delta`, apoi recitiți-l și verificați schema și numărul de rânduri. Păstrați datele originale și rezultatele etapelor anterioare.
- Folosiți Spark SQL pentru minimum trei calcule diferite, relevante pentru date, de exemplu numărul de înregistrări pe categorie, suma unei valori numerice și media unei valori numerice. Prezentați rezultatele și formulați minimum o concluzie susținută de valorile obținute.
- Realizați minimum două grafice de tipuri diferite pe datele analizate, de exemplu histogramă și scatter plot. Fiecare trebuie să aibă titlu, axe și unități unde se aplică, precum și o interpretare de 1–2 fraze. În etapa 4 se adaugă graficul streaming, de un al treilea tip; proiectul va include astfel minimum trei tipuri de grafice.

**De prezentat:** verificările înainte/după, transformările, setul curățat, cele trei rezultate de analiză și graficele exploratorii cu interpretări. Explicați de ce verificarea calității datelor precedă calcularea rezultatelor numerice.

## 3. Modelarea DWH și operații OLAP

- Construiți o schemă stea cu minimum un tabel de fapte și trei tabele de dimensiuni. Precizați ce reprezintă un rând din tabelul de fapte, cheile și relațiile. Alegeți minimum două măsuri numerice calculate prin agregarea faptelor, de exemplu suma valorilor și numărul tranzacțiilor/evenimentelor.
- Includeți o diagramă a schemei DWH.
- Creați și populați tabelele din datele curățate. Puteți utiliza tabele Delta interogate prin Spark SQL sau o bază relațională. Verificați numărul de rânduri, unicitatea cheilor dimensiunilor și absența referințelor fără corespondent.
- Executați minimum patru operații OLAP distincte:
    - **Roll-up:** agregare la un nivel superior.
    - **Drill-down:** detaliere la un nivel inferior.
    - **Slice:** selectarea unei valori dintr-o dimensiune.
    - **Dice:** restrângere după minimum două dimensiuni.
- Pentru fiecare operație, precizați întrebarea de analiză și interpretați rezultatul. Patru variante ale aceleiași operații nu îndeplinesc cerința.

**De prezentat:** diagrama, codul de creare și încărcare, verificările și cele patru interogări cu rezultate și interpretări.

## 4. Streaming simulat cu Kafka și MongoDB

- Implementați fluxul DWH → producer Kafka → Kafka → Spark Structured Streaming → MongoDB. Citiți înregistrările din DWH în loturi și publicați-le treptat, cu pauze între loturi; nu încărcați întregul dataset în memoria producerului.
- Folosiți timestamp-ul evenimentului; dacă lipsește, adăugați unul artificial și explicați regula. Procesați mesajele în micro-batch-uri și realizați minimum o agregare pe ferestre temporale. Precizați durata ferestrei și metrica.
- Salvați agregările în MongoDB, împreună cu începutul și sfârșitul ferestrei. Demonstrați minimum trei ferestre cu rezultate și realizați minimum un grafic pe baza lor. Graficul trebuie să fie de un tip diferit de cele două din etapa 2, de exemplu un grafic liniar, și să includă titlu, axe/unități și o interpretare de 1–2 fraze.
- Pentru demonstrație puteți folosi un eșantion din DWH; indicați numărul de înregistrări și criteriul de selecție. Arătați un mesaj Kafka și documentele corespunzătoare salvate în MongoDB.
- Explicați în notebook: (1) de ce redarea datelor istorice din DWH este o simulare și cum ar arăta un flux din surse live; (2) rolul Kafka și dificultățile care pot apărea fără el; (3) limitele simulării și problemele reale care nu sunt reprezentate automat.

### Dashboard pentru streaming din MongoDB

- Includeți minimum doi indicatori numerici, un grafic pe ferestre și un tabel cu rezultatele ultimelor ferestre.
- Permiteți actualizarea manuală sau automată și demonstrați modificarea afișării după sosirea unui lot nou.

**De prezentat:** dashboard-ul de streaming funcțional și minimum două concluzii susținute de date, fiecare însoțită de o posibilă decizie pentru utilizator. Graficele din notebook pot fi reutilizate în dashboard. Capturile statice nu înlocuiesc demonstrarea actualizării dashboard-ului.

**Opțional:** adăugați watermark și demonstrați un eveniment întârziat; sau integrați o sursă live prin Kafka, cu agregări pe ferestre și watermark. Păstrați codul și rezultatele în același notebook.
