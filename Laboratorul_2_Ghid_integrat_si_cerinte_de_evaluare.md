# **Lucrarea de laborator 2**

**De la date în Databricks la predicții și dashboard în Power BI**

Continuați laboratorul 1 cu un subset de **aproximativ 100 MB din același dataset curățat**, fără a repeta prelucrarea deja realizată. Folosiți **Databricks Free Edition** pentru date și modelare și **Power BI Desktop gratuit** pentru vizualizare.

## **1 Date în cloud și Delta Lake**

Încărcați subsetul în Databricks și organizați-l în tabele Delta, pregătite pentru modelare. Explicați pe scurt selecția datelor și organizarea lor.

**Rezultat:** date accesibile în Databricks, tabele Delta populate și codul de încărcare în notebook.

## **2 Un model predictiv**

Alegeți o problemă relevantă de regresie sau clasificare și antrenați **un singur model cu Spark MLlib**. Evaluați-l pe date separate de antrenare, interpretați performanța și explicați utilitatea predicțiilor.

**Rezultat:** model salvat și reutilizabil, evaluare prin **2 metrici și 1 grafic**, predicții salvate în Delta pentru dashboard. Nu se cere compararea mai multor modele.

## **3 Organizare fiabilitate și monitorizare**

Aplicați asupra fluxului de predicții:

- **Partiționare și copie de siguranță:** organizați datele în partiții și creați o copie separată. Explicați legătura și diferențele față de sharding și replicare automată.
- **Toleranță la erori:** simulați o întrerupere și demonstrați reluarea procesării fără pierderi sau duplicate.
- **Monitorizare:** urmăriți execuțiile și explicați cum identificați erorile și problemele de performanță.

**Rezultat:** demonstrații în notebook și dovezi ale recuperării și monitorizării. Nu se cere administrarea unui cluster sau implementarea replicării pe servere distincte.

## **4 Dashboard pentru stakeholderi**

Conectați Power BI Desktop la datele din Databricks și creați un raport interactiv care prezintă datele și predicțiile. Demonstrați filtrarea și actualizarea datelor.

**Rezultat:** fișier **.pbix** cu minimum **2 indicatori, 2 tipuri de grafice și 2 filtre**. Folosiți predicțiile în cel puțin un indicator și un grafic. Explicați **2 decizii** sprijinite de dashboard și limitele predicțiilor.

## **Predare și evaluare**

Predați în **Google Drive notebook-ul (.ipynb și HTML cu rezultate) și raportul Power BI (.pbix cu date importate)**. Includeți codul, explicațiile și dovezile demonstrațiilor; nu includeți parole sau tokenuri. **Nu se solicită prezentare cu slide-uri.**

Se evaluează **fluxul complet și reproductibil**, corectitudinea modelării, recuperarea după erori și utilitatea dashboardului. Demonstrați notebook-ul și raportul funcțional.
