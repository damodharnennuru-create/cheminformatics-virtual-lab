import pandas as pd
import plotly.express as px
import streamlit as st
from rdkit import DataStructs
from lab.ui import shell,heading,footer
from lab.core import fp,props
shell("Similarity Search");heading("COMPARE","Similarity Search","Rank candidates using Morgan fingerprints and Tanimoto similarity.")
q=st.text_input("Query molecule SMILES",value="CCO")
candidates=st.text_area("Candidate SMILES · one per line",value="CCO\nCCCO\nCC(=O)O\nc1ccccc1",height=130)
radius=st.slider("Fingerprint radius",1,4,2)
if st.button("Search candidates",type="primary"):
 try:
  qfp=fp(q,radius);rows=[];invalid=[]
  for i,s in enumerate(candidates.splitlines(),1):
   s=s.strip()
   if not s:continue
   try:
    p=props(s);rows.append({"SMILES":p["Canonical SMILES"],"Tanimoto":DataStructs.TanimotoSimilarity(qfp,fp(s,radius)),"MW (Da)":p["Molecular weight (Da)"],"LogP":p["LogP"]})
   except Exception:invalid.append(f"Line {i}")
  rows.sort(key=lambda r:r["Tanimoto"],reverse=True)
  st.session_state["sim"]=(q,radius,rows,invalid)
 except Exception as e:st.error(str(e))
if st.session_state.get("sim"):
 oldq,oldr,rows,invalid=st.session_state["sim"]
 if oldq!=q or oldr!=radius:st.info("Run search again to refresh.")
 if rows:
  df=pd.DataFrame(rows);st.dataframe(df,width="stretch",hide_index=True)
  fig=px.bar(df.sort_values("Tanimoto"),x="Tanimoto",y="SMILES",orientation="h",range_x=[0,1],color="Tanimoto",color_continuous_scale=["#CFE3FA","#0071E3"])
  fig.update_layout(height=max(300,45*len(df)),margin=dict(l=0,r=0,t=10,b=0),paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",coloraxis_showscale=False)
  st.plotly_chart(fig,width="stretch");st.download_button("Download similarity results",df.to_csv(index=False),file_name="similarity-results.csv")
 else:st.warning("No valid candidate molecules.")
 if invalid:st.warning("Skipped invalid SMILES on lines: "+", ".join(invalid))
footer()
