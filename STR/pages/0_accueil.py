import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# -------------------------------
# Chemin vers le MP3 basé sur le fichier courant
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # dossier du script
mp3_path = os.path.join(BASE_DIR, "..", "static", "Flix_Radu_Allez_viens.mp3")  # remonte d'un niveau

# Vérifier que le fichier existe
if not os.path.isfile(mp3_path):
    st.error(f"Fichier MP3 non trouvé : {mp3_path}")
else:
    # Charger et encoder en base64
    with open(mp3_path, "rb") as f:
        mp3_bytes = f.read()
    b64_mp3 = base64.b64encode(mp3_bytes).decode()

    # -------------------------------
    # CSS personnalisé
    # -------------------------------
    custom_css = """
        <style>
        /* Arrière-plan de la page principale */
        .stApp {
            background-color: rgba(13, 52, 4, 0.6) !important;
        }
        /* Arrière-plan du sidebar */
        section[data-testid="stSidebar"] {
            background-color: #666866 !important;
        }
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    st.markdown("""
        <style>
            .page-break { page-break-before: always; }
        </style>
    """, unsafe_allow_html=True)

    # -------------------------------
    # Colonnes et bouton lecture
    # -------------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            "<h4 style='text-align: center; color: white;'>Chanson 1</h4>",
            unsafe_allow_html=True
        )

        # HTML + JS pour bouton lecture
        html_code = f"""
        <div style="text-align:center;">
            <button id="playButton" style="
                background-color:#ff4444;
                border:none;
                border-radius:50%;
                width:100px;
                height:100px;
                font-size:40px;
                color:white;
                cursor:pointer;
            ">▶️</button>
            <audio id="myAudio" src="data:audio/mp3;base64,{b64_mp3}"></audio>
        </div>

        <script>
            const btn = document.getElementById("playButton");
            const audio = document.getElementById("myAudio");
            btn.addEventListener("click", () => {{
                audio.play();
            }});
        </script>
        """

        components.html(html_code, height=200)
