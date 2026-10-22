# Big Data Laboratory

Proiectul este configurat pentru GitHub Codespaces: containerul notebookului, Kafka și MongoDB pornesc împreună din `.devcontainer/devcontainer.json` și `docker-compose.yml`. Mediul Python este instalat din `requirements-codespaces.txt`; `requirements.txt` existent nu este folosit de Dockerfile.

## Pregătire

1. Înainte de rebuild, adăugați în Codespaces secretul `DATASET_URL` cu linkul de partajare publică Google Drive al snapshotului CSV. Linkul trebuie să permită descărcarea fără autentificare.
2. Rebuild/reopen Codespace pentru a aplica serviciile și dependențele. Verificați că serviciile `kafka`, `mongodb` și `workspace` sunt pornite.
3. Rulați verificarea din terminalul workspace:

```bash
python test.py
```

Testul validează execuția Spark locală, ping și write/read/delete în MongoDB, precum și produce/consume în Kafka. Adresele `kafka:9092` și `mongodb:27017` sunt disponibile în rețeaua Compose.

## Notebook

Deschideți `Laboratorul 1.ipynb`, selectați kernelul Python al Codespace-ului și rulați celulele în ordine. Celula de setup descarcă CSV-ul în `data/raw`, verifică headerul și dimensiunea minimă de 2 GiB, apoi îl redenumește atomic. Prima pornire Spark descarcă din Maven connectorul Structured Streaming pentru Kafka; este necesar acces la internet.

Nu comiteți CSV-ul și outputurile generate din `data/`; directorul este ignorat de Git. Celula veche de benchmark recreează `data/delta` pentru a porni istoricul la versiunea 0. Tabelele curate și DWH sunt scrise în căi separate.

## Dashboard

Pentru demonstrarea refresh-ului, rulați notebookul până după prima celulă de streaming. Porniți aplicația într-un terminal nou, apoi reveniți în notebook și rulați celula „Lot suplimentar”:

```bash
streamlit run dashboard.py --server.address 0.0.0.0 --server.port 8501
```

Codespaces va expune portul 8501. Dashboardul citește ultimele ferestre din colecția MongoDB `bigdata.crime_windows`; după publicarea lotului suplimentar, apăsați „Reîncarcă datele” și comparați indicatorii cu valorile inițiale.

## Resursa CSV

Setul de date este „Crimes - 2001 to Present” din portalul City of Chicago. Pentru reproducerea rezultatelor, folosiți snapshotul original de peste 2 GiB, nu o descărcare live cu un alt număr de rânduri. Dacă Google Drive cere autentificare sau quota-ul de descărcare este depășit, folosiți un link public funcțional pentru același snapshot; notebookul se oprește explicit dacă resursa nu poate fi verificată.

## Laboratorul 2: Databricks și Power BI

Laboratorul 2 continuă cu `data/processed_delta` produs de Laboratorul 1. Într-un Codespace nou, datele din `data/` nu sunt prezente deoarece directorul este ignorat de Git; rulați mai întâi celulele Lab 1 până la salvarea setului procesat. Notebookul Lab 2 nu reia descărcarea CSV-ului și nu repetă curățarea.

### Configurare Databricks

După modificarea `requirements-codespaces.txt`, faceți rebuild/reopen al Codespace-ului pentru instalarea `requests` și `python-dotenv`.

1. Copiați `.env.example` în `.env` pentru dezvoltare locală sau configurați `DATABRICKS_HOST` și `DATABRICKS_API` ca GitHub Codespaces Secrets. Opțional, configurați `DATABRICKS_VOLUME_PATH`. Nu comiteți `.env`; tokenul nu trebuie introdus în notebook.
2. În Databricks, creați un Unity Catalog Volume, implicit `workspace.default.lab2_files`. Dacă folosiți alt catalog/schema/volum, configurați aceeași cale în `DATABRICKS_VOLUME_PATH` și widgeturile `LAB2_CATALOG`, `LAB2_SCHEMA`, `LAB2_VOLUME` din notebook.
3. Deschideți `Laboratorul 2.ipynb` în kernelul Codespaces, lăsați faza `codespaces` și rulați celulele de pregătire/upload. Acestea creează subsetul Parquet reproductibil de aproximativ 100 MiB sub `data/lab2/`, verifică manifestul și transferă fișierele către Volume prin Databricks Files API.
4. Importați același notebook în workspace-ul Databricks, selectați `LAB2_PHASE=databricks` și rulați celulele cloud. Codespaces și Databricks nu împart filesystem-ul; accesul la Volume este prin path-ul Unity Catalog, nu prin calea locală `/workspaces/...`.

Notebookul produce tabela Delta de intrare, modelul MLlib, predicțiile, backup-ul, auditul și `lab2_powerbi_dashboard`. Tabelele generate au nume dedicate `lab2_*`; celula recovery recreează tabela de predicții demo cu același nume la fiecare rulare. Nu rulați celulele streaming din Lab 1 ca parte a acestui flux; Kafka și MongoDB nu sunt necesare pentru Lab 2.

### Power BI Service în browser

Conectați Power BI Service la endpoint-ul Databricks SQL și selectați `lab2_powerbi_dashboard`. Notebookul definește 2 KPI, un grafic cu coloane, un grafic liniar și filtrele pentru an și district. Folosiți refresh-ul și câmpurile `prediction_run_id`/`scored_at_utc` pentru a demonstra reîncărcarea.

Verificați devreme dacă licența Free oferă conectorul, refresh-ul și descărcarea `.pbix` pentru această sursă. Nu încărcați un CSV local ca substitut: rapoartele Service bazate pe fișiere CSV locale nu pot fi descărcate ca PBIX. Dacă exportul browserului nu este disponibil, ghidul de evaluare cere Power BI Desktop gratuit pentru livrabilul `.pbix`.

Predați notebookul executat și HTML-ul cu rezultate împreună cu `.pbix`. Păstrați fișierele de date sub `data/` și nu includeți tokenuri în Git sau în outputuri.