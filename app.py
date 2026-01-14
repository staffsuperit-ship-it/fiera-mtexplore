import streamlit as st
import requests
import json
from datetime import datetime

# 1. Configurazione della pagina (Titolo scheda browser e Icona)
st.set_page_config(page_title="Registrazione Ospiti MTExplore", page_icon="🍷", layout="centered")

# --- CODICE PER PULIRE L'INTERFACCIA (Nasconde Menu, Footer e Header) ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            div[data-testid="stToolbar"] {visibility: hidden; height: 0%; position: fixed;}
            div[data-testid="stDecoration"] {visibility: hidden; height: 0%; position: fixed;}
            #stDecoration {display:none;}
            .stAppDeployButton {display:none;}
            /* Rimuove lo spazio bianco in alto */
            .block-container {padding-top: 2rem;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 2. Il tuo URL di Google Apps Script (Il ricevitore)
URL_RICEVITORE = "https://script.google.com/macros/s/AKfycbz57txqpB5RU-ykBZmnzaX5SR-G8TzWXbOBPh6MfscLmaxADXzwp4qy7Bntqe1z25Pk/exec"

# 3. Contenuto della Web App
st.title("Benvenuto in MTExplore! 🍷")
st.write("Compila il modulo per ricevere i nostri aggiornamenti e listini.")

# Creazione del modulo (Form)
with st.form("modulo_fiera", clear_on_submit=True):
    # Nome e Cognome sulla stessa riga
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome *")
    with col2:
        cognome = st.text_input("Cognome *")
    
    # Altri campi
    telefono = st.text_input("Recapito telefonico")
    email = st.text_input("Indirizzo email *")
    azienda = st.text_input("Azienda")
    ruolo = st.text_input("Ruolo ricoperto")
    
    # Area di testo per le note
    note = st.text_area("Note", placeholder="Inserisci qui eventuali richieste o interessi particolari...")
    
    st.write("---")
    # Tasto di invio
    submit = st.form_submit_button("INVIA I DATI")

# 4. Logica di invio dei dati
if submit:
    # Controllo campi obbligatori
    if nome and cognome and email:
        # Prepariamo i dati da inviare a Google
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
            with st.spinner('Salvataggio in corso...'):
                # Spediamo il pacchetto a Google Apps Script
                response = requests.post(URL_RICEVITORE, data=json.dumps(payload))
            
            if response.status_code == 200:
                st.balloons() # Effetto festa!
                st.success(f"Grazie {nome}! I tuoi dati sono stati salvati correttamente.")
                st.info("Verrai ora reindirizzato al sito mtexplore.it...")
                
                # Reindirizzamento automatico dopo 3 secondi
                redirect_code = '<meta http-equiv="refresh" content="3; URL=https://www.mtexplore.it">'
                st.markdown(redirect_code, unsafe_allow_html=True)
            else:
                st.error("Errore del server. Per favore riprova tra poco.")
        
        except Exception as e:
            st.error(f"Errore di connessione: {e}")
    else:
        st.warning("Attenzione: Nome, Cognome ed Email sono obbligatori (*)")

# Footer discreto
st.markdown("<br><br><center><small>MTExplore - Lead Generation System</small></center>", unsafe_allow_html=True)
