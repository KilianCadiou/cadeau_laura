import streamlit as st
from st_pages import get_nav_from_toml
import toml
import os

# -------------------------------
# CSS personnalisé
# -------------------------------
custom_css = """
    <style>
    /* Arrière-plan principal en blanc */
    .stApp {
        background: white !important;
    }

    /* Sidebar également en blanc */
    section[data-testid="stSidebar"] {
        background: white !important;
    }

    /* (Optionnel) texte en noir pour contraster */
    .stApp, section[data-testid="stSidebar"] * {
        color: black !important;
    }
    </style>
"""


st.markdown(custom_css, unsafe_allow_html=True)

# -------------------------------
# Chemin relatif vers le fichier TOML
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # dossier de streamlit_app.py
toml_path = os.path.join(BASE_DIR, ".streamlit", "pages.toml")

# Vérification que le fichier existe
if not os.path.isfile(toml_path):
    st.error(f"Fichier pages.toml non trouvé : {toml_path}")
else:
    # Charger et inspecter le fichier TOML
    config = toml.load(toml_path)
    print(config)  # Vérifie que les pages sont correctement chargées

    # Charger la navigation
    nav = get_nav_from_toml(toml_path)

    # Créer la navigation
    pg = st.navigation(nav)
    pg.run()
