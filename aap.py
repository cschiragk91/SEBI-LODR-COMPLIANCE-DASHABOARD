import streamlit as st
import json
from datetime import datetime, timedelta
from utils import calculate_due

with open('data/compliances.json') as f:
    compliances = json.load(f)

st.title("SEBI LODR Compliance Dashboard")

today = datetime.today()

upcoming = []
overdue = []
all_data = []

for c in compliances:
    due = calculate_due(c)

    if due:
        status = "OK"

        if due < today:
            status = "Overdue"
            overdue.append((c["name"], due))
        elif due <= today + timedelta(days=7):
            status = "Upcoming"
            upcoming.append((c["name"], due))

        all_data.append((c["name"], c["regulation"], due.date(), status))
    else:
        all_data.append((c["name"], c["regulation"], "Event Based", "Manual"))

st.subheader("Overdue")
for o in overdue:
    st.write(o)

st.subheader("Upcoming (7 Days)")
for u in upcoming:
    st.write(u)

st.subheader("All Compliances")
st.table(all_data)
