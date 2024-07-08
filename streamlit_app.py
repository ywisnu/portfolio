
# Online Python - IDE, Editor, Compiler, Interpreter

import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

# --- SHARED ON ALL PAGES ---
st.sidebar.text("Made ")


# --- RUN NAVIGATION ---
pg.run()


