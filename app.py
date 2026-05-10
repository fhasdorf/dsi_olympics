import streamlit as st
import pandas as pd
import altair as alt

# 1. Seitenkonfiguration für Streamlit (optional, aber sieht besser aus)
st.set_page_config(page_title="Olympia Segel-Analyse", layout="wide")

# 2. Titel und journalistischer "Hook" (Der Text für die Agentur)
st.title("Die unsichtbare Revolution im Segelsport")
st.markdown("""
**Warum Olympia-Seglerinnen heute völlig anders trainieren müssen als vor 20 Jahren.**

Historische Daten zeigen einen drastischen Wandel: Der durchschnittliche Body Mass Index (BMI) bei olympischen Seglerinnen ist massiv gesunken. Doch das ist kein Zufall und hat wenig mit Fitnesstrends zu tun. 

Es ist die pure **Physik des Bootes**. 

Wähle links die verschiedenen Bootsklassen aus, um zu sehen, wie der Wechsel von schweren Kielbooten zu agilen Skiffs und Windsurfern das physische Anforderungsprofil der Athletinnen radikal verändert hat.
""")


@st.cache_data # Wichtig: Caching, damit die App schnell bleibt
def load_data():
    
    df = pd.read_csv('physical_evolution.csv')
    df['bmi'] = df['weight'] / ((df['height'] / 100) ** 2)
    sailing_women = df[(df['sport_name'] == 'Sailing') & (df['sex'] == 'F')].copy()
    sailing_evolution = sailing_women.groupby(['year', 'event_name'])['bmi'].mean().reset_index()
    return sailing_evolution

data = load_data()

# 4. Interaktivität: Multiselect für die Bootsklassen
st.sidebar.header("Filter")
available_events = data['event_name'].unique()
selected_events = st.sidebar.multiselect(
    "Wähle Bootsklassen zum Vergleich:",
    options=available_events,
    default=available_events # Zeigt am Anfang alle an
)

# 5. Daten filtern basierend auf der Auswahl
filtered_data = data[data['event_name'].isin(selected_events)]

# 6. Altair Chart erstellen
if not filtered_data.empty:
    chart = alt.Chart(filtered_data).mark_line(point=True).encode(
        x=alt.X('year:O', title='Olympisches Jahr'), # :O für Ordinal (diskrete Jahre)
        y=alt.Y('bmi:Q', title='Durchschnittlicher BMI', scale=alt.Scale(zero=False)), # :Q für Quantitativ
        color=alt.Color('event_name:N', title='Bootsklasse', legend=alt.Legend(orient='bottom')), # :N für Nominal
        tooltip=['year', 'event_name', alt.Tooltip('bmi:Q', format='.2f')] # Interaktiver Tooltip bei Hover!
    ).properties(
        width=800,
        height=500,
        title="Evolution des BMI bei olympischen Seglerinnen"
    ).interactive() # Macht den Chart zoom- und verschiebbar

    # Chart in Streamlit anzeigen
    st.altair_chart(chart, use_container_width=True)
else:
    st.warning("Bitte wähle mindestens eine Bootsklasse in der Seitenleiste aus.")

# 7. Fazit / Erklärung (Dynamisch anpassen je nach Auswahl ist möglich, hier statisch)
st.markdown("""
---
**Die Analyse zeigt:**
* **Schwere Kielboote** erforderten traditionell mehr Masse an der Kante, was sich in einem höheren durchschnittlichen BMI widerspiegelt.
* **Moderne Skiffs und Windsurfen** setzen High-Performance-Materialien voraus. Hier zählen extreme Agilität, Ausdauer und ein geringes Leistungsgewicht.
""")
