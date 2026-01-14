import streamlit as st
import requests
import json
from datetime import datetime

# 1. Configurazione della pagina
st.set_page_config(page_title="Registrazione Ospiti MTExplore", page_icon="🍷")

# 2. Il tuo link personale di Google (App Script)
URL_RICEVITORE = "https://script.google.com/macros/s/AKfycbz57txqpB5RU-ykBZmnzaX5SR-G8TzWXbOBPh6MfscLmaxADXzwp4qy7Bntqe1z25Pk/exec"

# 3. Interfaccia Grafica
st.title("Benvenuto in MTExplore! 🍷")
st.write("Compila il modulo per ricevere i nostri aggiornamenti e listini.")

# Creazione del form
with st.form("modulo_contatti", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome *")
    with col2:
        cognome = st.text_input("Cognome *")
    
    telefono = st.text_input("Recapito telefonico")
    email = st.text_input("Indirizzo email *")
    azienda = st.text_input("Azienda")
    ruolo = st.text_input("Ruolo ricoperto")
    note = st.text_area("Note (es. vitigni di interesse, richieste particolari)")
    
    st.write("---")
    submit = st.form_submit_button("INVIA I DATI")

# 4. Logica di invio dati
if submit:
    if nome and cognome and email:
        # Prepariamo il pacchetto dati (Payload)
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
            # Mandiamo i dati a Google
            with st.spinner('Salvataggio in corso...'):
                response = requests.post(URL_RICEVITORE, data=json.dumps(payload))
            
            if response.status_code == 200:
                st.balloons()
                st.success(f"Grazie {nome}! I tuoi dati sono stati salvati correttamente.")
                st.info("Verrai reindirizzato al sito mtexplore.it tra 3 secondi...")
                
                # Script per il reindirizzamento automatico
                st.markdown(f'<meta http-equiv="refresh" content="3; URL=https://www.mtexplore.it">', unsafe_allow_html=True)
            else:
                st.error("Errore del server Google. Riprova tra un istante.")
        
        except Exception as e:
            st.error(f"Errore di connessione: {e}")
    else:
        st.warning("Per favore, compila i campi obbligatori contrassegnati con l'asterisco (*)")

# 5. Footer semplice
st.markdown("---")
st.caption("MTExplore - Fiera 2024")
