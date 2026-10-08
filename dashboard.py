import os

import pandas as pd
import streamlit as st
from pymongo import MongoClient


st.set_page_config(page_title="Crime Streaming", layout="wide")
st.title("Crime Streaming Dashboard")
st.caption("Agregări pe ferestre de eveniment salvate în MongoDB")

mongo_uri = os.environ.get("MONGODB_URI", "mongodb://mongodb:27017")
database_name = os.environ.get("MONGODB_DATABASE", "bigdata")
collection_name = os.environ.get("MONGODB_COLLECTION", "crime_windows")

if st.button("Reîncarcă datele", type="primary"):
    st.rerun()

try:
    with MongoClient(mongo_uri, serverSelectionTimeoutMS=3000) as client:
        client.admin.command("ping")
        documents = list(
            client[database_name][collection_name]
            .find(
                {},
                {
                    "_id": 0,
                    "window_start": 1,
                    "window_end": 1,
                    "incident_count": 1,
                    "arrest_count": 1,
                    "synthetic_timestamp_count": 1,
                },
            )
            .sort("window_start", -1)
            .limit(48)
        )
except Exception as exc:
    st.error(f"MongoDB nu este disponibil: {exc}")
    st.stop()

if not documents:
    st.info("Nu există încă ferestre în MongoDB. Porniți producerul și procesarea streaming.")
    st.stop()

windows = pd.DataFrame(documents)
windows["window_start"] = pd.to_datetime(windows["window_start"], utc=True).dt.tz_convert(None)
windows["window_end"] = pd.to_datetime(windows["window_end"], utc=True).dt.tz_convert(None)
windows = windows.sort_values("window_start")
windows["incident_count"] = windows["incident_count"].fillna(0).astype(int)
windows["arrest_count"] = windows["arrest_count"].fillna(0).astype(int)

incident_total = int(windows["incident_count"].sum())
arrest_total = int(windows["arrest_count"].sum())
arrest_rate = 100 * arrest_total / incident_total if incident_total else 0.0
latest_window = windows.iloc[-1]

metric_columns = st.columns(3)
metric_columns[0].metric("Incidente în ferestrele afișate", f"{incident_total:,}")
metric_columns[1].metric("Arestări în ferestrele afișate", f"{arrest_total:,}")
metric_columns[2].metric("Pondere arestări", f"{arrest_rate:.1f}%")

st.subheader("Incidente pe fereastră")
st.line_chart(windows, x="window_start", y="incident_count", x_label="Începutul ferestrei", y_label="Număr incidente")

st.subheader("Ferestre recente")
st.dataframe(
    windows.sort_values("window_start", ascending=False),
    use_container_width=True,
    hide_index=True,
)
st.caption(
    f"Ultima fereastră: {latest_window['window_start']:%Y-%m-%d %H:%M} UTC – "
    f"{latest_window['window_end']:%Y-%m-%d %H:%M} UTC. "
    "Valorile și rata sunt calculate pentru ferestrele afișate."
)
