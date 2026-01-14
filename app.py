import streamlit as st
import requests
import json
from datetime import datetime

# 1. Configurazione della pagina
st.set_page_config(page_title="Registrazione Ospiti MTExplore", page_icon="🍷", layout="centered")

# 2. DEFINIZIONE DEL CSS (La scatola che conteneva l'errore)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            header {visibility: hidden !important;}
            [data-testid="viewerBadge"] {display: none !important;}
            .stAppDeployButton {display: none !important;}
            div[data-testid="stStatusWidget"] {display: none !important;}
            #stDecoration {display: none !important;}
            .block-container {padding-top: 1rem !important; padding-bottom: 1rem !important;}
            </style>
            """

# Applichiamo il CSS
st.markdown(hide_st_style, unsafe_allow_html=True)

# 3. Il tuo URL di Google Apps Script
URL_RICEVITORE = "https://script.google.com/macros/s/AKfycbz57txqpB5RU-ykBZmnzaX5SR-G8TzWXbOBPh6MfscLmaxADXzwp4qy7Bntqe1z25Pk/exec"

# 4. Contenuto della Web App
st.title("Benvenuto in MTExplore! 🍷")
st.write("Compila il modulo per ricevere i nostri aggiornamenti.")

with st.form("modulo_fiera", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome *")
    with col2:
        cognome = st.text_input("Cognome *")
    
    telefono = st.text_input("Recapito telefonico")
    email = st.text_input("Indirizzo email *")
    azienda = st.text_input("Azienda")
    ruolo = st.text_input("Ruolo ricoperto")
    note = st.text_area("Note")
    
    st.write("---")
    submit = st.form_submit_button("INVIA I DATI")

if submit:
    if nome and cognome and email:
        payload = {
            "Nome": nome, 
            "Cognome": cognome, 
            "Telefono": telefono, 
            "Email": email, 
            "Azienda": azienda, 
            "Ruolo": ruolo, 
            "Note": note, 
            "Data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        try:
            response = requests.post(URL_RICEVITORE, data=json.dumps(payload))
            if response.status_code == 200:
                st.balloons()
                st.success(f"Grazie {nome}! Dati salvati.")
                st.markdown('<meta http-equiv="refresh" content="3; URL=https://www.mtexplore.it">', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Errore: {e}")
    else:
        st.warning("Compila i campi obbligatori (*)")

st.markdown("<center><small>MTExplore - Lead Generation System</small></center>", unsafe_allow_html=True)
