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