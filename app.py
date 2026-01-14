import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# Configurazione pagina
st.set_page_config(page_title="Registrazione Ospiti MTExplore", page_icon="🍷")

# Link del foglio
url_foglio = "https://docs.google.com/spreadsheets/d/1bvjEQY-XEm5sVoCQaxTGKyCP7s1xgVkrb2V_mKE-O9s/edit?gid=0#gid=0"

# Connessione
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("Benvenuto in MTExplore! 🍷")

with st.form("modulo_contatti", clear_on_submit=True):
    nome = st.text_input("Nome *")
    cognome = st.text_input("Cognome *")
    telefono = st.text_input("Recapito telefonico")
    email = st.text_input("Indirizzo email *")
    azienda = st.text_input("Azienda")
    ruolo = st.text_input("Ruolo ricoperto")
    note = st.text_area("Note")
    submit = st.form_submit_button("Invia i dati")

if submit:
    if nome and cognome and email:
        try:
            # Creiamo il nuovo contatto
            nuovo_contatto = pd.DataFrame([{
                "Nome": nome,
                "Cognome": cognome,
                "Telefono": telefono,
                "Email": email,
                "Azienda": azienda,
                "Ruolo": ruolo,
                "Note": note,
                "Data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }])
            
            # Leggiamo i dati esistenti
            # Se il foglio è vuoto o dà errore, creiamo un dataframe vuoto
            try:
                df_esistente = conn.read(spreadsheet=url_foglio, worksheet="Foglio1")
            except:
                df_esistente = pd.DataFrame()

            # Uniamo i dati
            df_finale = pd.concat([df_esistente, nuovo_contatto], ignore_index=True)
            
            # Scriviamo sul foglio
            conn.update(spreadsheet=url_foglio, data=df_finale, worksheet="Foglio1")
            
            st.success("Dati salvati con successo!")
            st.write("Redirect in corso...")
            st.markdown(f'<meta http-equiv="refresh" content="2; URL=https://www.mtexplore.it">', unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Errore: {e}")
            st.info("Verifica che il foglio si chiami 'Foglio1' e che i permessi siano su 'Editor'")
    else:
        st.error("Compila i campi obbligatori!")
