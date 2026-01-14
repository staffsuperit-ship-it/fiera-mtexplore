import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Configurazione pagina
st.set_page_config(page_title="Registrazione Ospiti", page_icon="🍷")

# 2. Campi del modulo
st.title("Benvenuto!")
st.write("Inserisci i tuoi dati per rimanere in contatto con noi.")

with st.form("form_contatti", clear_on_submit=True):
    nome = st.text_input("Nome *")
    cognome = st.text_input("Cognome *")
    tel = st.text_input("Recapito telefonico")
    email = st.text_input("Indirizzo email *")
    azienda = st.text_input("Azienda")
    ruolo = st.text_input("Ruolo ricoperto")
    note = st.text_area("Note")
    
    submit = st.form_submit_button("Invia i dati")

# 3. Cosa succede quando l'utente preme "Invia"
if submit:
    if nome and cognome and email: # Controllo campi obbligatori
        # Qui tra poco aggiungeremo il pezzetto per salvare su Google
        st.success("Dati inviati correttamente!")
        
        # 4. Reindirizzamento
        st.markdown(f'<meta http-equiv="refresh" content="2; URL=https://www.mtexplore.it">', unsafe_allow_html=True)
        st.write("Verrai reindirizzato al sito mtexplore.it tra 2 secondi...")
    else:
        st.error("Per favore, compila i campi obbligatori (Nome, Cognome, Email)")
