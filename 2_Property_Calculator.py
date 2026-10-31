import pandas as pd
import streamlit as st
from lab.ui import shell,heading,footer
from lab.core import props,lipinski
shell("Property Calculator");heading("UNDERSTAND","Property Calculator","Calculate common descriptors and screen against Lipinski's rule of five.")
s=st.text_input("SMILES",value="CC(=O)Oc1ccccc1C(=O)O")
if st.button("Calculate properties",type="primary"):
 try:
  with st.spinner("Calculating descriptors…"):st.session_state["props"]=(s,props(s))
 except Exception as e:st.session_state.pop("props",None);st.error(str(e))
if st.session_state.get("props"):
 old,p=st.session_state["props"]
 if old!=s:st.info("Run the calculator again to refresh the displayed results.")
 cols=st.columns(4)
 for c,k in zip(cols,["Molecular weight (Da)","LogP","TPSA (Å²)","Rings"]):c.metric(k,p[k])
 st.markdown("#### Descriptor details");st.dataframe(pd.DataFrame([{"Property":k,"Value":str(v)} for k,v in p.items()]),width="stretch")
 checks=lipinski(p);st.markdown("#### Lipinski rule-of-five screen");st.success("Passes all four thresholds." if all(checks.values()) else f"Exceeds {sum(not x for x in checks.values())} of 4 thresholds.")
 st.dataframe(pd.DataFrame([{"Criterion":k,"Result":"Pass" if v else "Exceeds"} for k,v in checks.items()]),hide_index=True,width="stretch")
 st.download_button("Download properties CSV",pd.DataFrame([p]).to_csv(index=False),file_name="molecular-properties.csv")
footer()
