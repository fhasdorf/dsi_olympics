# ⛵ Olympia Segel-Analyse: Die unsichtbare Revolution

[See streamlit app]([https://beispiel.de](https://dsiolympicsfh.streamlit.app/))


Dieses Projekt analysiert die historische Entwicklung der körperlichen Merkmale von olympischen Athleten ab dem Jahr 1960. Der besondere Fokus dieses Deep Dives liegt auf dem **Segelsport der Frauen**. 

Die Daten zeigen einen drastischen Wandel: Der durchschnittliche Body Mass Index (BMI) bei olympischen Seglerinnen ist über die Jahrzehnte massiv gesunken. Diese interaktive Datenanalyse belegt, dass dieser Trend primär auf die technologische Evolution der olympischen Bootsklassen zurückzuführen ist – vom schweren Kielboot hin zu High-Performance-Skiffs und Windsurfern.

## Features
* **Datenbereinigung & Feature Engineering:** Transformation von Rohdaten und Berechnung des historischen Body Mass Index (BMI).
* **Interaktive Visualisierung:** Ein exploratives Dashboard, das es ermöglicht, verschiedene olympische Bootsklassen und deren physisches Anforderungsprofil im Zeitverlauf direkt miteinander zu vergleichen.

## Tech Stack
* **Python 3**
* **Pandas:** Für Data Wrangling, Aggregation und Feature Engineering.
* **Altair:** Für die Erstellung deklarativer, interaktiver Visualisierungen.
* **Streamlit:** Für das Frontend und die Bereitstellung als interaktive Web-App.

## Projektstruktur
* `app.py`: Der Hauptcode für das interaktive Streamlit-Dashboard.
* `physical_evolution.csv`: Der bereinigte und aggregierte Datensatz (erstellt via SQL-Extrakt aus einer relationalen PostgreSQL-Datenbank).
* `requirements.txt`: Liste aller benötigten Python-Abhängigkeiten.



