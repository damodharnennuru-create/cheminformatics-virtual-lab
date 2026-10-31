import streamlit as st

def shell(section):
 st.markdown("""<style>
 :root{--blue:#536DFE;--violet:#7357FF;--ink:#202124;--muted:#70757A}
 html,body,[class*=css]{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:var(--ink)}
 .stApp,[data-testid=stAppViewContainer]{background:linear-gradient(180deg,#F8FAFF 0%,#FFFFFF 440px)}
 [data-testid=stHeader]{background:rgba(248,250,255,.84);backdrop-filter:blur(18px)}
 [data-testid=stSidebar]{display:none}
 .block-container{max-width:1160px;padding-top:1rem;padding-bottom:2.5rem}
 h1,h2,h3{color:#202124;letter-spacing:-.045em}
 .eyebrow{font-size:.72rem;text-transform:uppercase;letter-spacing:.13em;color:#536DFE;font-weight:700;margin-bottom:.6rem}
 .hero-title{font-size:clamp(3rem,7vw,5.7rem);line-height:.98;font-weight:700;margin:.5rem 0 1rem}
 .hero-title span{background:linear-gradient(95deg,#3978FF,#8B5CF6);background-clip:text;-webkit-background-clip:text;color:transparent}.hero-copy,.page-copy{font-size:1.08rem;line-height:1.55;max-width:700px;color:#70757A;margin:0 0 1.5rem}
 .page-title{font-size:clamp(2.4rem,5vw,4rem);line-height:1.03;margin:.4rem 0 .5rem}
 .tool-card,.note-card,.result-card{background:#fff;border:1px solid #E6EAF2;border-radius:20px;padding:22px;box-shadow:0 10px 32px #243b690d;transition:transform .2s ease,box-shadow .2s ease}
 .tool-card:hover{transform:translateY(-3px);box-shadow:0 16px 40px #344b821a}
 .tool-card h3{margin:.15rem 0 .55rem}.tool-card p,.note-card p{color:#6E6E73;line-height:1.55}
 .stButton>button,.stDownloadButton>button{border-radius:999px;font-weight:600;transition:all .18s ease}
 .stButton>button[kind=primary]{background:linear-gradient(100deg,#3478F6,#7657E8);border-color:#536DFE}
 [data-testid=stMetric]{background:#fff;border:1px solid #E8E8ED;border-radius:14px;padding:14px}
 .footer{border-top:1px solid #E2E6EF;margin-top:3rem;padding:18px 8px 4px;text-align:center;color:#6E6E73;font-size:.78rem}
 .topnav{position:sticky;top:0;z-index:999;background:rgba(248,250,255,.9);backdrop-filter:saturate(180%) blur(18px);border-bottom:1px solid rgba(220,226,239,.8);display:flex;align-items:center;gap:25px;padding:13px max(18px,calc((100vw - 1160px)/2));margin:0 calc((1160px - 100vw)/2) 34px;white-space:nowrap}
 .topnav a{color:#4C5057;text-decoration:none;font-size:.78rem;transition:color .18s}.topnav a:hover{color:#536DFE}.topnav .brand{font-weight:700;color:#202124;font-size:.86rem;margin-right:auto}.topnav .active{color:#536DFE;font-weight:600}
 @media(max-width:820px){.topnav{overflow-x:auto;gap:18px;margin-left:-1rem;margin-right:-1rem;padding-left:1rem;padding-right:1rem}.topnav .brand{margin-right:0}.block-container{padding:1rem}}
 @media(max-width:560px){.topnav{gap:14px}.topnav a{font-size:.72rem}.tool-card,.note-card{padding:17px}}
 </style>""",unsafe_allow_html=True)
 links=[("Home","/"),("Molecule Viewer","/Molecule_Viewer"),("Properties","/Property_Calculator"),("Similarity","/Similarity_Search"),("Dataset","/Dataset_Explorer"),("About","/About")]
 items="".join(f'<a class="{"active" if label==section or (section=="Property Calculator" and label=="Properties") or (section=="Similarity Search" and label=="Similarity") or (section=="Dataset Explorer" and label=="Dataset") else ""}" href="{url}">{label}</a>' for label,url in links)
 st.markdown(f'<nav class="topnav"><a class="brand" href="/">◌ &nbsp; Molecular Studio</a>{items}</nav>',unsafe_allow_html=True)

def heading(label,title,copy):
 st.markdown(f'<div class="eyebrow">{label}</div><h1 class="page-title">{title}</h1><p class="page-copy">{copy}</p>',unsafe_allow_html=True)

def footer():
 st.markdown('<div class="footer">Created by Nennuru Damodhar Reddy | RA2611026050176 | Section: AIML C</div>',unsafe_allow_html=True)
