import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.markdown(
    "<h3 style='text-align: center; color: white;'>Joyeux Anniversaire !</h3>",
    unsafe_allow_html=True
)

# Chemin vers le MP3 basé sur le fichier courant
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # dossier du script pages/
mp3_path_felix_radu = os.path.join(BASE_DIR, "..", "static", "Flix Radu - Allez viens_.mp3")  # remonte à STR/static/

# Vérifier que le fichier existe
if not os.path.isfile(mp3_path_felix_radu):
    st.error(f"Fichier MP3 non trouvé : {mp3_path_felix_radu}")
else:
    # Charger et encoder en base64
    with open(mp3_path_felix_radu, "rb") as f:
        mp3_bytes_felix_radu = f.read()
    b64_mp3_felix_radu = base64.b64encode(mp3_bytes_felix_radu).decode()

mp3_path_alien = os.path.join(BASE_DIR, "..", "static", "Loin_dici.mp3")  # remonte à STR/static/

# Vérifier que le fichier existe
if not os.path.isfile(mp3_path_alien):
    st.error(f"Fichier MP3 non trouvé : {mp3_path_alien}")
else:
    # Charger et encoder en base64
    with open(mp3_path_alien, "rb") as f:
        mp3_bytes_alien = f.read()
    b64_mp3_alien = base64.b64encode(mp3_bytes_alien).decode()

    # CSS personnalisé
    custom_css = """
        <style>
        .stApp {
            background-color: rgba(13, 52, 4, 0.6) !important;
        }
        section[data-testid="stSidebar"] {
            background-color: #666866 !important;
        }
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)




    st.markdown(
        "<h4 style='text-align: center; color: white;'>Chanson 1</h4>",
        unsafe_allow_html=True
    )

    html_code = f"""
    <div style="text-align:center;">
        <button id="playButton" style="
            background-color:#ff4444;
            border:none;
            border-radius:50%;
            width:200px;
            height:200px;
            font-size:40px;
            color:white;
            cursor:pointer;
        ">▶️</button>
        <audio id="myAudio" src="data:audio/mp3;base64,{b64_mp3_felix_radu}"></audio>
    </div>

    <script>
        const btn = document.getElementById("playButton");
        const audio = document.getElementById("myAudio");

        btn.addEventListener("click", () => {{
            if (audio.paused) {{
                audio.play();
                btn.textContent = "⏸️";  // change le bouton en pause
            }} else {{
                audio.pause();
                btn.textContent = "▶️";   // change le bouton en lecture
            }}
        }});
    </script>
    """

    components.html(html_code, height=250)


    st.markdown(
        "<h4 style='text-align: center; color: white;'>Chanson 2</h4>",
        unsafe_allow_html=True
    )

    html_code = f"""
    <div style="text-align:center;">
        <button id="playButton" style="
            background-color:#ff4444;
            border:none;
            border-radius:50%;
            width:200px;
            height:200px;
            font-size:40px;
            color:white;
            cursor:pointer;
        ">▶️</button>
        <audio id="myAudio" src="data:audio/mp3;base64,{b64_mp3_alien}"></audio>
    </div>

    <script>
        const btn = document.getElementById("playButton");
        const audio = document.getElementById("myAudio");

        btn.addEventListener("click", () => {{
            if (audio.paused) {{
                audio.play();
                btn.textContent = "⏸️";  // change le bouton en pause
            }} else {{
                audio.pause();
                btn.textContent = "▶️";   // change le bouton en lecture
            }}
        }});
    </script>
    """

    components.html(html_code, height=250)
