import streamlit as st
from lab.ui import shell,footer
shell("Home")
st.markdown('<div class="eyebrow">CHEMINFORMATICS · VIRTUAL LAB</div><h1 class="hero-title">Explore molecules.<br><span>Find what matters.</span></h1><p class="hero-copy">A focused toolkit for viewing structures, understanding molecular properties, comparing compounds, and exploring chemical datasets.</p>',unsafe_allow_html=True)
st.page_link("pages/1_Molecule_Viewer.py",label="Open molecule viewer →",icon="⚛")
st.write("")
cards=[("01 · VISUALIZE","Molecule Viewer","View SMILES as 2D structures and optional interactive 3D conformers.","pages/1_Molecule_Viewer.py"),("02 · UNDERSTAND","Property Calculator","Calculate common descriptors and screen Lipinski thresholds.","pages/2_Property_Calculator.py"),("03 · COMPARE","Similarity Search","Rank structures with Morgan fingerprints and Tanimoto similarity.","pages/3_Similarity_Search.py"),("04 · EXPLORE","Dataset Explorer","Filter CSV or SDF compounds, chart properties, and export results.","pages/4_Dataset_Explorer.py")]
for pair in (cards[:2],cards[2:]):
 cols=st.columns(2)
 for c,(ey,t,d,p) in zip(cols,pair):
  with c:
   st.markdown(f'<div class="tool-card"><div class="eyebrow">{ey}</div><h3>{t}</h3><p>{d}</p></div>',unsafe_allow_html=True);st.page_link(p,label=f"Explore {t} →")
st.markdown('<div class="note-card"><div class="eyebrow">BUILT FOR CLEAR THINKING</div><h2>Useful chemistry, without the clutter.</h2><p>Validated inputs, transparent calculations, and downloadable results in a calm workspace.</p></div>',unsafe_allow_html=True)
footer()
