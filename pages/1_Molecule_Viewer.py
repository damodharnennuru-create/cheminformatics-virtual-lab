import streamlit as st
from rdkit import Chem
from lab.ui import shell,heading,footer
from lab.core import mol,image,plot3d
shell("Molecule Viewer");heading("VISUALIZE","Molecule Viewer","Enter a SMILES string to inspect its molecular structure.")
s=st.text_input("SMILES",value="CC(=O)Oc1ccccc1C(=O)O",help="Example: ethanol is CCO; aspirin is CC(=O)Oc1ccccc1C(=O)O")
three=st.toggle("Generate interactive 3D conformer")
if st.button("Render molecule",type="primary"):
 m=mol(s)
 if not m:st.error("We couldn't read that SMILES. Check the notation and try again.")
 else:st.session_state["molview"]=(Chem.MolToSmiles(m),three)
state=st.session_state.get("molview")
if state:
 smi,show=state;a,b=st.columns([1.2,.8])
 with a:
  st.image(image(smi),width="stretch")
  if show:
   with st.spinner("Generating 3D conformer…"):
    try:st.plotly_chart(plot3d(smi),width="stretch")
    except Exception as e:st.warning(str(e))
 with b:
  st.markdown("#### Structure details");st.code(smi);st.write("Heavy atoms:",mol(smi).GetNumHeavyAtoms())
  st.download_button("Download canonical SMILES",smi,file_name="molecule.smi")
else:st.markdown('<div class="result-card">Enter a valid SMILES string and render it to view the structure.</div>',unsafe_allow_html=True)
footer()
