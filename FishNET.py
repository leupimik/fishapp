import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="FishNET",
    page_icon=":fish:",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://google.com/',
        'Report a bug': "https://google.com/",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.sidebar.write("Sidebartext")

st.title("FishNET :fish: ")

st.subheader("Fisch im Netz und keine Ahnung, ob es sich um eine gefährdete Fischart handelt?")
st.info("**FishNET** ist eine Fischerkennungs-App, die die häufigsten in der Schweiz vorkommenden Fische mittels automatischer Bilderkennung bestimmt und vor gefährdeten Fischarten warnt.")
st.info("Foto aufnehmen oder hochladen und in Sekundenschnelle der gefangene Fisch mit **FishNET** schnell und praktisch bestimmen.")

st.write("")

with st.expander("Foto hochladen"):
    file = st.file_uploader("")

with st.expander("Foto aufnehmen"):
    picture = st.camera_input("")

st.write("")

st.subheader("Dein Fisch")

st.subheader("Dein Ergebniss")