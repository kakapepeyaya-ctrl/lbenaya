import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="LBENAYA GC2 - Site Officiel",
    page_icon="⚽",
    layout="centered"
)

# En-tête avec Logo et Titre
st.title("LBENAYA GC2")
st.caption("Site Officiel du Club - Saison 26/27")

# Affichage du logo
try:
    st.image("logo.jpg", width=180)
except:
    pass

st.divider()

# Section À propos
st.header("À propos du Club")
st.write(
    "Bienvenue sur la plateforme officielle de **LBENAYA GC2**. "
    "Engagement, discipline et esprit d'équipe sur et en dehors du terrain."
)

st.divider()

# Section Effectif / Squad List 26/27
st.header("Effectif 26/27 (Squad List)")

squad = [
    {"nom": "B. YASSER", "role": "Capitaine (C)", "is_captain": True},
    {"nom": "B. SALAH EDDINE", "role": "Joueur", "is_captain": False},
    {"nom": "E. MOUAD", "role": "Joueur", "is_captain": False},
    {"nom": "F. AYMANE", "role": "Joueur", "is_captain": False},
    {"nom": "O. WALID", "role": "Joueur", "is_captain": False},
    {"nom": "T. AYOUB", "role": "Joueur", "is_captain": False},
    {"nom": "Z. ACHRAF", "role": "Joueur", "is_captain": False},
]

# Affichage des joueurs sous forme de grilles dynamiques
col1, col2 = st.columns(2)

for index, player in enumerate(squad):
    target_col = col1 if index % 2 == 0 else col2
    with target_col:
        if player["is_captain"]:
            st.success(f"👑 **{player['nom']}**\n\n*{player['role']}*")
        else:
            st.info(f"⚽ **{player['nom']}**\n\n*{player['role']}*")

st.divider()
st.caption("© 2026 LBENAYA GC2. Tous droits réservés.")
