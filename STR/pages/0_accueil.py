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
mp3_path_terrenoire = os.path.join(BASE_DIR, "..", "static", "terrenoire.mp3")  # remonte à STR/static/

# Vérifier que le fichier existe
if not os.path.isfile(mp3_path_terrenoire):
    st.error(f"Fichier MP3 non trouvé : {mp3_path_terrenoire}")
else:
    # Charger et encoder en base64
    with open(mp3_path_terrenoire, "rb") as f:
        mp3_bytes_terrenoire = f.read()
    b64_mp3_terrenoire = base64.b64encode(mp3_bytes_terrenoire).decode()

mp3_path_alien = os.path.join(BASE_DIR, "..", "static", "Loin_dici.mp3")  # remonte à STR/static/

# Vérifier que le fichier existe
if not os.path.isfile(mp3_path_alien):
    st.error(f"Fichier MP3 non trouvé : {mp3_path_alien}")
else:
    # Charger et encoder en base64
    with open(mp3_path_alien, "rb") as f:
        mp3_bytes_alien = f.read()
    b64_mp3_alien = base64.b64encode(mp3_bytes_alien).decode()

# 🔹 Chemin vers ton fichier enregistrement.m4a
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
m4a_path = os.path.join(BASE_DIR, "..", "static", "enregistrement.m4a")

# Vérifier que le fichier existe
if not os.path.isfile(m4a_path):
    st.error(f"Fichier non trouvé : {m4a_path}")
else:
    # Charger et encoder en base64
    with open(m4a_path, "rb") as f:
        m4a_bytes = f.read()
    b64_m4a = base64.b64encode(m4a_bytes).decode()

    
# CSS personnalisé
custom_css = """
    <style>
    /* Fond principal en noir */
    .stApp {
        background-color: black !important;
    }

    /* Sidebar en noir */
    section[data-testid="stSidebar"] {
        background-color: black !important;
    }

    /* Texte en blanc pour la lisibilité */
    .stApp, section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Boutons et champs en noir avec bordures blanches */
    .stButton>button, .stTextInput>div>div>input, textarea, select {
        background-color: black !important;
        color: white !important;
        border: 1px solid white !important;
    }
    </style>
"""


st.markdown(custom_css, unsafe_allow_html=True)
st.markdown(
    "<h4 style='text-align: center; color: white;'>Message</h4>",
    unsafe_allow_html=True
)

html_code = f"""
<div style="text-align:center; background-color:black; height:100vh; display:flex; justify-content:center; align-items:center;">
    <button id="playButton" style="
        background-color:white;
        border:2px solid white;
        border-radius:50%;
        width:200px;
        height:200px;
        font-size:40px;
        color:white;
        cursor:pointer;
    ">▶️</button>
    <audio id="myAudio" autoplay muted src="data:audio/mp3;base64,{b64_m4a}"></audio>
</div>

<script>
    const btn = document.getElementById("playButton");
    const audio = document.getElementById("myAudio");

    // Volume max
    audio.volume = 1.0;

    // Dès que l'audio peut jouer, enlever le muet et lancer la lecture
    audio.addEventListener("canplaythrough", () => {{
        audio.muted = false;
        audio.play().catch(() => {{
            console.log("Lecture automatique bloquée par le navigateur.");
        }});
    }});

    // Bouton ▶️ / ⏸️
    btn.addEventListener("click", (event) => {{
        event.stopPropagation(); // empêche d'interférer avec autoplay
        if (audio.paused) {{
            audio.play();
            btn.textContent = "⏸️";
        }} else {{
            audio.pause();
            btn.textContent = "▶️";
        }}
    }});
</script>
"""

components.html(html_code, height=250)

st.markdown(
    "<h4 style='text-align: center; color: white;'>Chanson</h4>",
    unsafe_allow_html=True
)

html_code = f"""
<div style="text-align:center; background-color:black; height:100vh; display:flex; justify-content:center; align-items:center;">
    <button id="playButton" style="
        background-color:white;
        border:2px solid white;
        border-radius:50%;
        width:200px;
        height:200px;
        font-size:40px;
        color:white;
        cursor:pointer;
    ">▶️</button>
    <audio id="myAudio" src="data:audio/mp3;base64,{b64_mp3_terrenoire}"></audio>
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
    "<h4 style='text-align: center; color: white;'>Un Film</h4>",
    unsafe_allow_html=True
)

# html_code = f"""
# <div style="text-align:center; background-color:black; height:100vh; display:flex; justify-content:center; align-items:center;">
#     <button id="playButton" style="
#         background-color:white;
#         border:2px solid white;
#         border-radius:50%;
#         width:200px;
#         height:200px;
#         font-size:40px;
#         color:white;
#         cursor:pointer;
#     ">▶️</button>
#     <audio id="myAudio" src="data:audio/mp3;base64,{b64_mp3_alien}"></audio>
# </div>

# <script>
#     const btn = document.getElementById("playButton");
#     const audio = document.getElementById("myAudio");

#     btn.addEventListener("click", () => {{
#         if (audio.paused) {{
#             audio.play();
#             btn.textContent = "⏸️";  // change le bouton en pause
#         }} else {{
#             audio.pause();
#             btn.textContent = "▶️";   // change le bouton en lecture
#         }}
#     }});
# </script>
# """


# components.html(html_code, height=250)


st.markdown(
    """
    <div style="text-align: center;">
    <a href="https://www.primevideo.com/detail/0KEKSSZG48Q1P3TH9AQ4LB6C6G/ref=atv_sr_fle_c_sre999aa_1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B0866RLQYQ&qid=1756241638748" target="_blank">
        <img src="https://raw.githubusercontent.com/KilianCadiou/cadeau_laura/main/STR/img/pdf_82a53edc-36af-11e9-8fee-a66a916a465e.jpg" width="500">
    </a>
    """,
    unsafe_allow_html=True
    )
