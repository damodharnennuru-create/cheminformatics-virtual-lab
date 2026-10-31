import io
import pandas as pd
import streamlit as st
from rdkit import Chem,DataStructs
from rdkit.Chem import AllChem,Crippen,Descriptors,Draw,rdMolDescriptors,rdFingerprintGenerator
@st.cache_data(show_spinner=False)
def _binary(smiles):
 m=Chem.MolFromSmiles(str(smiles).strip());return m.ToBinary() if m else None
def mol(smiles):
 b=_binary(smiles);return Chem.Mol(b) if b else None
def props(smiles):
 m=mol(smiles)
 if m is None:raise ValueError("Could not parse SMILES. Check atom symbols, brackets, and bond notation.")
 return {"Canonical SMILES":Chem.MolToSmiles(m),"Molecular weight (Da)":round(Descriptors.MolWt(m),3),"LogP":round(Crippen.MolLogP(m),3),"TPSA (Å²)":round(rdMolDescriptors.CalcTPSA(m),3),"H-bond donors":int(rdMolDescriptors.CalcNumHBD(m)),"H-bond acceptors":int(rdMolDescriptors.CalcNumHBA(m)),"Rotatable bonds":int(rdMolDescriptors.CalcNumRotatableBonds(m)),"Rings":int(rdMolDescriptors.CalcNumRings(m))}
def image(smiles):return Draw.MolToImage(mol(smiles),size=(720,450)).convert("RGB")
def fp(smiles,radius=2):
 m=mol(smiles)
 if m is None:raise ValueError("Invalid SMILES.")
 return rdFingerprintGenerator.GetMorganGenerator(radius=radius,fpSize=2048).GetFingerprint(m)
def lipinski(p):return {"Molecular weight ≤ 500":p["Molecular weight (Da)"]<=500,"LogP ≤ 5":p["LogP"]<=5,"H-bond donors ≤ 5":p["H-bond donors"]<=5,"H-bond acceptors ≤ 10":p["H-bond acceptors"]<=10}
def plot3d(smiles):
 import plotly.graph_objects as go
 m=Chem.AddHs(mol(smiles))
 if m.GetNumAtoms()>100:raise ValueError("3D preview supports structures with 100 atoms or fewer.")
 params=AllChem.ETKDGv3();params.randomSeed=17
 if AllChem.EmbedMolecule(m,params)<0:raise ValueError("Could not generate a conformer.")
 AllChem.UFFOptimizeMolecule(m,maxIters=120);c=m.GetConformer();ps=[c.GetAtomPosition(i) for i in range(m.GetNumAtoms())]
 fig=go.Figure()
 for bond in m.GetBonds():
  i,j=bond.GetBeginAtomIdx(),bond.GetEndAtomIdx();fig.add_trace(go.Scatter3d(x=[ps[i].x,ps[j].x],y=[ps[i].y,ps[j].y],z=[ps[i].z,ps[j].z],mode="lines",line=dict(color="#A7A7AD",width=5),hoverinfo="skip",showlegend=False))
 symbols=[a.GetSymbol() for a in m.GetAtoms()]
 colors=["#4A90E2" if s=="C" else "#E05D5D" if s=="O" else "#4772BF" if s=="N" else "#D6A641" if s=="S" else "#999" for s in symbols]
 fig.add_trace(go.Scatter3d(x=[p.x for p in ps],y=[p.y for p in ps],z=[p.z for p in ps],mode="markers+text",text=symbols,textposition="top center",marker=dict(size=5,color=colors),hoverinfo="text",showlegend=False))
 fig.update_layout(height=460,margin=dict(l=0,r=0,t=0,b=0),paper_bgcolor="white",scene=dict(bgcolor="white",xaxis_visible=False,yaxis_visible=False,zaxis_visible=False,aspectmode="data"));return fig
@st.cache_data(show_spinner=False)
def read_data(data,filename):
 if filename.lower().endswith(".csv"):return pd.read_csv(io.BytesIO(data))
 if filename.lower().endswith(".sdf"):
  rows=[]
  for m in Chem.ForwardSDMolSupplier(io.BytesIO(data),removeHs=False):
   if m:
    r={k:m.GetProp(k) for k in m.GetPropNames()};r["SMILES"]=Chem.MolToSmiles(Chem.RemoveHs(m));r.update(props(r["SMILES"]));rows.append(r)
  if rows:return pd.DataFrame(rows)
  raise ValueError("No readable structures found in this SDF.")
 raise ValueError("Upload a CSV or SDF.")
