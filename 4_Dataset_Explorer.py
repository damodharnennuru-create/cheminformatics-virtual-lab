import pandas as pd
import plotly.express as px
import streamlit as st
from lab.core import read_data,props
from lab.ui import shell,heading,footer
shell("Dataset Explorer");heading("EXPLORE","Dataset Explorer","Upload CSV or SDF data, filter records, and inspect numeric distributions.")
f=st.file_uploader("Choose a dataset",type=["csv","sdf"])
if f:
 try:
  with st.spinner("Reading dataset…"):df=read_data(f.getvalue(),f.name)
  cols=[c for c in df.columns if str(c).strip().lower() in ("smiles","canonical_smiles","isomeric_smiles")]
  if cols:
   col=st.selectbox("SMILES column",cols)
   if st.button("Calculate descriptors"):
    vals=[]
    for s in df[col].fillna("").astype(str):
     try:vals.append(props(s))
     except Exception:vals.append({})
    desc=pd.DataFrame(vals,index=df.index)
    for k in desc:
     if k not in df:df[k]=desc[k]
  q=st.text_input("Filter rows",placeholder="Search across dataset")
  view=df if not q else df[df.astype(str).apply(lambda c:c.str.contains(q,case=False,na=False)).any(axis=1)]
  st.caption(f"{len(view):,} of {len(df):,} records");st.dataframe(view,width="stretch",height=360)
  nums=view.select_dtypes(include="number").columns.tolist()
  if nums:
   col=st.selectbox("Numeric property to chart",nums);fig=px.histogram(view,x=col,nbins=30,title=f"Distribution · {col}",color_discrete_sequence=["#0071E3"])
   fig.update_layout(height=350,margin=dict(l=0,r=0,t=45,b=0),paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)");st.plotly_chart(fig,width="stretch")
  st.download_button("Download filtered CSV",view.to_csv(index=False),file_name="molecule-dataset-filtered.csv")
 except Exception as e:st.error(f"Could not read this dataset: {e}")
else:st.markdown('<div class="result-card">Start with a CSV table or SDF structure file. Supported file size depends on your Streamlit deployment limits.</div>',unsafe_allow_html=True)
footer()
