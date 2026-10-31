import streamlit as st
from lab.ui import shell,heading,footer
shell("About");heading("ABOUT THE LAB","A clear place to explore chemistry.","An independent learning aid for common cheminformatics workflows.")
st.markdown("""
### What you can do
- View SMILES as 2D structures and optional interactive 3D conformers.
- Calculate molecular weight, LogP, TPSA, hydrogen-bond counts, rotatable bonds, and rings.
- Screen against four Lipinski rule-of-five thresholds.
- Compare compounds using Morgan fingerprints and Tanimoto similarity.
- Explore CSV/SDF data, inspect distributions, and download filtered results.

### Calculation notes
Descriptors are calculated with RDKit. Similarity is a structural comparison aid, not a prediction of biological activity. Lipinski screening is a rule of thumb, not a drug-likeness determination.

### Data handling
Entered structures and uploaded files are processed in the current app session. No external AI service is used.

### Reference review
The supplied Streamlit reference links stayed on their loading screens during review, and the Mobbin page could not be opened in this session. Reference-specific pages and controls could not be independently inventoried; this app follows the feature and style guidance included in the project brief.
""")
footer()
