import streamlit as st
from st_pages import get_nav_from_toml
import toml
import os

# -------------------------------
# CSS personnalisé
# -------------------------------
custom_css = """
    <style>
    /* Modifier l'arrière-plan de la page principale avec un dégradé */
    .stApp {
        background: linear-gradient(to bottom, rgba(13, 52, 4, 0.8), rgba(0, 0, 0, 0.8)) !important;
    }

    /* Modifier l'arrière-plan du volet de navigation (sidebar) avec un dégradé */
    section[data-testid="stSidebar"] {
        background: linear-gradient(to bottom, #666866, #333333) !important;
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
