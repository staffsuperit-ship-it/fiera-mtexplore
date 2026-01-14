# --- CODICE PER PULIRE L'INTERFACCIA (Versione Super Aggressiva) ---
hide_st_style = """
            <style>
            /* Nasconde il menu in alto a destra */
            #MainMenu {visibility: hidden !important;}
            /* Nasconde il footer "Made with Streamlit" */
            footer {visibility: hidden !important;}
            /* Nasconde la barra superiore */
            header {visibility: hidden !important;}
            /* Nasconde il badge rosso "Hosted with Streamlit" in basso a destra */
            .viewerBadge_container__1QSob {display: none !important;}
            .stAppDeployButton {display: none !important;}
            [data-testid="viewerBadge"] {display: none !important;}
            /* Rimuove decorazioni e barre di stato */
            div[data-testid="stStatusWidget"] {display: none !important;}
            #stDecoration {display: none !important;}
            /* Ottimizza lo spazio su mobile */
            .block-container {padding-top: 1rem !important; padding-bottom: 1rem !important;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
