import streamlit as st
from openai import OpenAI
import os

OPENAI_API_KEY = "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"
client = OpenAI(api_key=OPENAI_API_KEY)

leaders = {
    "Michelle Obama": {"title": "Education & Social Impact", "description": "Financial literacy through education reform", "style": "inspiring", "expertise": ["Impact Investing", "Education Finance"], "image": "michelle_obama.png", "emoji": "🌸", "topics": ["Personal Finance", "Education"]},
    "Angela Merkel": {"title": "Economic Policy Expert", "description": "Fiscal policy and strategic planning", "style": "analytical", "expertise": ["Fiscal Policy", "Economic Strategy"], "image": "Angela_Merkel.png", "emoji": "📊", "topics": ["Economic Policy", "Government Finance"]},
    "Malala Yousafzai": {"title": "Social Finance Advocate", "description": "Microfinance and social change", "style": "passionate", "expertise": ["Microfinance", "Social Bonds"], "image": "Malala_Yousafazi.png", "emoji": "💙", "topics": ["Microfinance", "Education"]},
    "Ruth Bader Ginsburg": {"title": "Financial Law & Ethics", "description": "Financial regulations and law", "style": "precise", "expertise": ["Financial Law", "Securities"], "image": "Ruth_Bader_Ginsburg.png", "emoji": "⚖️", "topics": ["Financial Law", "Ethics"]},
    "Indra Nooyi": {"title": "Corporate Finance Leader", "description": "Corporate finance and M&A", "style": "strategic", "expertise": ["Corporate Finance", "M&A"], "image": "Indra_Nooyi.png", "emoji": "💼", "topics": ["Finance Careers", "Corporate Strategy"]},
    "Sheryl Sandberg": {"title": "Tech Finance Executive", "description": "Tech valuations and scaling", "style": "analytical", "expertise": ["Tech Finance", "Scaling"], "image": "Sheryl_Sandberg.png", "emoji": "💻", "topics": ["Tech Finance", "Startups"]},
    "Jacinda Ardern": {"title": "Wellbeing Economics", "description": "Budget and wellbeing economics", "style": "empathetic", "expertise": ["Public Finance", "Budget Policy"], "image": "Jacinda_Ardern.png", "emoji": "🌿", "topics": ["Public Finance", "Wellbeing"]},
    "Mae Jemison": {"title": "STEM Finance Pioneer", "description": "R&D funding and venture capital", "style": "innovative", "expertise": ["Venture Capital", "R&D Finance"], "image": "Mae_Jemison.png", "emoji": "🚀", "topics": ["Venture Capital", "STEM"]},
    "Reshma Saujani": {"title": "Startup Finance Advocate", "description": "Fundraising and startup equity", "style": "bold", "expertise": ["Fundraising", "Startup Equity"], "image": "Reshman_Saujani.png", "emoji": "🎯", "topics": ["Fundraising", "Startups"]},
    "Sara Blakely": {"title": "Bootstrap Finance Expert", "description": "Bootstrapping and wealth building", "style": "creative", "expertise": ["Bootstrapping", "Cash Flow"], "image": "Sara_Blakely.png", "emoji": "✨", "topics": ["Entrepreneurship", "Wealth Building"]}
}

st.set_page_config(page_title="Finance Leaders", page_icon="💼", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');
    #MainMenu, footer, header {visibility: hidden;}
    * {font-family: 'Poppins', sans-serif;}
    
    .stApp {
        background: linear-gradient(135deg, #E3F2FD 0%, #F3E5F5 25%, #FFF8E1 50%, #E8F5E9 75%, #FFE5F1 100%);
        background-size: 400% 400%;
        animation: bg 20s ease infinite;
    }
    @keyframes bg {0%, 100% {background-position: 0% 50%;} 50% {background-position: 100% 50%;}}
    
    .title {
        text-align: center;
        font-size: 4.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea, #764ba2, #f093fb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 6px;
        margin-bottom: 10px;
        animation: pulse 3s ease infinite;
    }
    @keyframes pulse {0%, 100% {transform: scale(1);} 50% {transform: scale(1.02);}}
    
    .subtitle {
        text-align: center;
        font-size: 1.3rem;
        color: #667eea;
        font-weight: 700;
        letter-spacing: 3px;
        margin-bottom: 20px;
    }
    
    .greeting {
        background: rgba(255,255,255,0.9);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(102,126,234,0.3);
        padding: 20px;
        border-radius: 50px;
        margin: 30px auto;
        max-width: 600px;
        text-align: center;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        animation: float 3s ease infinite;
    }
    @keyframes float {0%, 100% {transform: translateY(0);} 50% {transform: translateY(-10px);}}
    
    .card {
        background: white;
        border-radius: 30px;
        border: 2px solid rgba(102,126,234,0.2);
        padding: 25px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
        cursor: pointer;
        position: relative;
        transform-style: preserve-3d;
    }
    
    .card:hover {
        transform: translateY(-35px) scale(1.12) rotateY(-5deg);
        box-shadow: 0 40px 80px rgba(102,126,234,0.4);
        border-color: rgba(102,126,234,0.6);
        z-index: 100;
    }
    
    .emoji-badge {
        position: absolute;
        top: 20px;
        right: 20px;
        width: 65px;
        height: 65px;
        background: rgba(255,255,255,0.95);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 35px;
        border: 3px solid rgba(102,126,234,0.3);
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        transition: all 0.4s ease;
    }
    
    .card:hover .emoji-badge {
        transform: scale(1.3) rotate(360deg);
    }
    
    .profile-img {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        border: 5px solid white;
        box-shadow: 0 15px 40px rgba(0,0,0,0.2);
        margin: 0 auto 20px;
        display: block;
        transition: all 0.5s ease;
    }
    
    .card:hover .profile-img {
        transform: scale(1.15) translateZ(50px);
        box-shadow: 0 25px 60px rgba(102,126,234,0.4);
    }
    
    .card h3 {
        color: #2D3748;
        font-size: 22px;
        font-weight: 800;
        text-align: center;
        margin: 15px 0 8px;
    }
    
    .card .role {
        color: #667eea;
        font-size: 14px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 10px;
    }
    
    .card .desc {
        color: #4A5568;
        font-size: 12px;
        text-align: center;
        margin-bottom: 15px;
        line-height: 1.6;
    }
    
    .tag {
        display: inline-block;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 10px;
        font-weight: 700;
        margin: 3px;
        text-transform: uppercase;
        box-shadow: 0 5px 15px rgba(102,126,234,0.3);
        transition: all 0.3s ease;
    }
    
    .tag:hover {
        transform: translateY(-3px) scale(1.1);
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 15px 35px;
        font-weight: 700;
        transition: all 0.4s ease;
        box-shadow: 0 10px 30px rgba(102,126,234,0.35);
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-size: 14px;
    }
    
    .stButton>button:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 15px 40px rgba(102,126,234,0.5);
    }
    
    .chat-header {
        background: rgba(255,255,255,0.95);
        backdrop-filter: blur(20px);
        padding: 30px;
        border-radius: 30px;
        margin-bottom: 25px;
        box-shadow: 0 15px 50px rgba(0,0,0,0.1);
        border: 2px solid rgba(102,126,234,0.2);
    }
    
    .user-msg {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 18px 24px;
        border-radius: 25px 25px 5px 25px;
        margin: 12px 0;
        margin-left: auto;
        max-width: 70%;
        box-shadow: 0 8px 25px rgba(102,126,234,0.35);
    }
    
    .assistant-msg {
        background: rgba(255,255,255,0.95);
        color: #2D3748;
        padding: 18px 24px;
        border-radius: 25px 25px 25px 5px;
        margin: 12px 0;
        max-width: 70%;
        border: 2px solid rgba(102,126,234,0.2);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    
    .stTextInput>div>div>input {
        background: rgba(255,255,255,0.95);
        border: 2px solid rgba(102,126,234,0.25);
        border-radius: 25px;
        padding: 16px 24px;
        transition: all 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #667eea;
        box-shadow: 0 0 30px rgba(102,126,234,0.25);
    }
    
    .section-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 50px 0 35px;
        letter-spacing: 2px;
    }
</style>
""", unsafe_allow_html=True)

# Session State
for key, default in [("messages", {name: [{"role": "system", "content": f"You are {name}, a {leaders[name]['style']} financial expert."}] for name in leaders}), ("selected_leader", None), ("typing", False), ("carousel_page", 0)]:
    if key not in st.session_state:
        st.session_state[key] = default

# Main Page
if not st.session_state.selected_leader:
    st.markdown('<h1 class="title">FINANCE LEADERS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">VISIONARIES WHO CHANGED THE WORLD</p>', unsafe_allow_html=True)
    st.markdown('<div class="greeting"><p style="color: #2D3748; font-size: 1.2rem; font-weight: 700; margin: 0;">👋 Ready to chat with inspiring leaders?</p></div>', unsafe_allow_html=True)
    
    st.markdown('<h2 class="section-title">RECOMMENDED FOR YOU</h2>', unsafe_allow_html=True)
    cols = st.columns(5)
    for idx, topic in enumerate(["Finance Careers", "Personal Finance", "Startups", "Social Impact", "Tech Finance"]):
        with cols[idx]:
            st.button(topic, key=f"t{idx}", width='stretch')
    
    st.markdown('<h2 class="section-title">ALL LEADERS</h2>', unsafe_allow_html=True)
    
    nav1, _, nav2 = st.columns([1, 2, 1])
    with nav1:
        if st.button("← Previous", width='stretch') and st.session_state.carousel_page > 0:
            st.session_state.carousel_page -= 1
            st.rerun()
    with nav2:
        if st.button("Next →", width='stretch') and st.session_state.carousel_page < 1:
            st.session_state.carousel_page += 1
            st.rerun()
    
    leaders_list = list(leaders.keys())
    start = st.session_state.carousel_page * 5
    cols = st.columns(5, gap="large")
    
    for idx, col in enumerate(cols):
        leader_idx = start + idx
        if leader_idx < len(leaders_list):
            name = leaders_list[leader_idx]
            leader = leaders[name]
            with col:
                st.markdown(f'<div class="card"><div class="emoji-badge">{leader["emoji"]}</div>', unsafe_allow_html=True)
                if os.path.exists(leader['image']):
                    st.markdown(f'<img src="data:image/png;base64," class="profile-img" />', unsafe_allow_html=True)
                    st.image(leader['image'], width=180)
                else:
                    st.markdown(f'<div class="profile-img" style="background: linear-gradient(135deg, #FFD6E8, #C9A0DC); display: flex; align-items: center; justify-content: center; font-size: 70px;">{leader["emoji"]}</div>', unsafe_allow_html=True)
                
                st.markdown(f'<h3>{name}</h3><p class="role">{leader["title"]}</p><p class="desc">{leader["description"]}</p><div style="text-align: center;">{"".join([f"<span class=\"tag\">{e}</span>" for e in leader["expertise"][:2]])}</div></div>', unsafe_allow_html=True)
                
                if st.button("Start Chat", key=f"b{leader_idx}", width='stretch'):
                    st.session_state.selected_leader = name
                    st.rerun()

# Chat Page
else:
    name = st.session_state.selected_leader
    leader = leaders[name]
    
    c1, c2 = st.columns([1, 8])
    with c1:
        if st.button("← Back"):
            st.session_state.selected_leader = None
            st.rerun()
    
    with c2:
        st.markdown(f'<div class="chat-header"><div style="display: flex; align-items: center; gap: 25px;"><div style="width: 80px; height: 80px; background: linear-gradient(135deg, #FFD6E8, #C9A0DC); border-radius: 25px; display: flex; align-items: center; justify-content: center; font-size: 45px; border: 3px solid rgba(102,126,234,0.3);">{leader["emoji"]}</div><div><h2 style="color: #2D3748; margin: 0; font-size: 36px; font-weight: 900;">{name}</h2><p style="color: #667eea; margin: 8px 0; font-size: 18px; font-weight: 700;">{leader["title"]}</p></div></div></div>', unsafe_allow_html=True)
    
    for msg in st.session_state.messages[name][1:]:
        css = "user-msg" if msg["role"] == "user" else "assistant-msg"
        align = "flex-end" if msg["role"] == "user" else "flex-start"
        st.markdown(f'<div style="display: flex; justify-content: {align};"><div class="{css}">{msg["content"]}</div></div>', unsafe_allow_html=True)
    
    if st.session_state.typing:
        st.markdown('<div class="assistant-msg">Thinking...</div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns([6, 1])
    with c1:
        user_input = st.text_input("Message", placeholder=f"Ask {name.split()[0]} about finance...", key="input", label_visibility="collapsed")
    with c2:
        send = st.button("Send", width='stretch')
    
    if send and user_input:
        st.session_state.messages[name].append({"role": "user", "content": user_input})
        st.session_state.typing = True
        st.rerun()
    
    if st.session_state.typing:
        try:
            response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages[name], temperature=0.7, max_tokens=400)
            st.session_state.messages[name].append({"role": "assistant", "content": response.choices[0].message.content})
            st.session_state.typing = False
            st.rerun()
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.session_state.typing = False
