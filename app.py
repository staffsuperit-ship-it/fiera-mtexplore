import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# 1. Configurazione della pagina (Titolo che appare nella scheda del browser)
st.set_page_config(page_title="Registrazione Ospiti MTExplore", page_icon="🍷")

# 2. Collegamento al tuo foglio Google
# Il link che mi hai passato è già inserito qui sotto
url_foglio = "https://docs.google.com/spreadsheets/d/1bvjEQY-XEm5sVoCQaxTGKyCP7s1xgVkrb2V_mKE-O9s/edit?usp=sharing"

# Creiamo la connessione
conn = st.connection("gsheets", type=GSheetsConnection)

# 3. Interfaccia Grafica
st.title("Benvenuto in MTExplore! 🍷")
st.write("Compila il modulo per ricevere i nostri aggiornamenti.")

# Creazione del form (i campi che hai richiesto)
with st.form("modulo_contatti", clear_on_submit=True):
    nome = st.text_input("Nome *")
    cognome = st.text_input("Cognome *")
    telefono = st.text_input("Recapito telefonico")
    email = st.text_input("Indirizzo email *")
    azienda = st.text_input("Azienda")
    ruolo = st.text_input("Ruolo ricoperto")
    note = st.text_area("Note")
    
    submit = st.form_submit_button("Invia i dati")

# 4. Logica di invio
if submit:
    # Verifichiamo che i campi obbligatori siano pieni
    if nome and cognome and email:
        try:
            # Creiamo una riga con i dati inseriti
            nuovi_dati = pd.DataFrame([{
                "Nome": nome,
                "Cognome": cognome,
                "Telefono": telefono,
                "Email": email,
                "Azienda": azienda,
                "Ruolo": ruolo,
                "Note": note,
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }])
            
            # Leggiamo i dati esistenti dal tuo foglio (Foglio1)
            df_esistente = conn.read(spreadsheet=url_foglio, worksheet="Foglio1")
            
            # Uniamo i vecchi dati con i nuovi
            df_aggiornato = pd.concat([df_esistente, nuovi_dati], ignore_index=True)
            
            # Carichiamo tutto sul foglio Google
            conn.update(spreadsheet=url_foglio, data=df_aggiornato, worksheet="Foglio1")
            
            st.success("Grazie! I tuoi dati sono stati salvati.")
            
            # Messaggio di redirect
            st.write("Verrai reindirizzato al sito mtexplore.it tra pochi secondi...")
            st.markdown(f'<meta http-equiv="refresh" content="3; URL=https://www.mtexplore.it">', unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Si è verificato un errore tecnico: {e}")
            st.info("Assicurati che il Foglio Google sia impostato su 'Chiunque abbia il link può modificare'")
    else:
        st.error("Per favore, compila tutti i campi obbligatori (*)")
