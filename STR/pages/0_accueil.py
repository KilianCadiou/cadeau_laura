import pandas as pd
import streamlit as st
import ast
from bs4 import BeautifulSoup
import pickle
import requests
import re
import plotly.express as px
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
from rapidfuzz import fuzz
from rapidfuzz import process
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns
import os

custom_css = """
    <style>
    /* Modifier l'arrière-plan de la page principale */
    .stApp {
        background-color: rgba(13, 52, 4, 0.6) !important;
    }

    /* Modifier l'arrière-plan du volet de navigation (sidebar) */
    section[data-testid="stSidebar"] {
        background-color: #666866 !important; /* Couleur gris foncé */
    }
    </style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

st.markdown("""
    <style>
        .page-break { page-break-before: always; }
    </style>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    st.markdown(
        "<h4 style='text-align: center; color: white;'>Chanson 1</h4>",
        unsafe_allow_html=True
    )
    st.audio('/Users/kilian/Documents/GitHub/cadeau_laura/STR/Flix Radu - Allez viens_.mp3')
