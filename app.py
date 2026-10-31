import streamlit as st
from lab.ui import shell, footer
from lab.home import render_home

st.set_page_config(page_title="Molecular Studio", page_icon="🧬", layout="wide", initial_sidebar_state="collapsed")
shell("Home")
render_home()
footer()