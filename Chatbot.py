import streamlit as st
from openai import OpenAI
import os

OPENAI_API_KEY = "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"
client = OpenAI(api_key=OPENAI_API_KEY)

leaders = {
    "Michelle Obama": {"title": "Education & Social Impact", "specialty": "Passionate about financial literacy through education reform and community investment strategies", "style": "inspiring", "expertise": ["Impact Investing", "Education Finance"], "image": "michelle_obama.png"},
    "Angela Merkel": {"title": "Economic Policy Expert", "specialty": "Analytical approach to fiscal policy, European economics, and strategic financial planning", "style": "analytical", "expertise": ["Fiscal Policy", "Economic Strategy"], "image": "Angela_Merkel.png"},
    "Malala Yousafzai": {"title": "Social Finance Advocate", "specialty": "Passionate insights on funding education, microfinance, and investing in social change", "style": "passionate", "expertise": ["Microfinance", "Social Bonds"], "image": "Malala_Yousafazi.png"},
    "Ruth Bader Ginsburg": {"title": "Financial Law & Ethics", "specialty": "Precise guidance on financial regulations, investment law, and ethical wealth management", "style": "precise", "expertise": ["Financial Law", "Securities"], "image": "Ruth_Bader_Ginsburg.png"},
    "Indra Nooyi": {"title": "Corporate Finance Leader", "specialty": "Strategic insights on corporate finance, M&A, sustainable business growth, and CFO excellence", "style": "strategic", "expertise": ["Corporate Finance", "M&A"], "image": "Indra_Nooyi.png"},
    "Sheryl Sandberg": {"title": "Tech Finance Executive", "specialty": "Data-driven approach to tech valuations, scaling startups, and financial operations", "style": "analytical", "expertise": ["Tech Finance", "Scaling"], "image": "Sheryl_Sandberg.png"},
    "Jacinda Ardern": {"title": "Wellbeing Economics", "specialty": "Compassionate approach to budget management, public finance, and wellbeing economics", "style": "empathetic", "expertise": ["Public Finance", "Budget Policy"], "image": "Jacinda_Ardern.png"},
    "Mae Jemison": {"title": "STEM Finance Pioneer", "specialty": "Innovative thinking on R&D funding, STEM investment, and technology venture capital", "style": "innovative", "expertise": ["Venture Capital", "R&D Finance"], "image": "Mae_Jemison.png"},
    "Reshma Saujani": {"title": "Startup Finance Advocate", "specialty": "Bold approach to fundraising, startup equity, and building financial resilience in tech", "style": "bold", "expertise": ["Fundraising", "Startup Equity"], "image": "Reshman_Saujani.png"},
    "Sara Blakely": {"title": "Bootstrap Finance Expert", "specialty": "Self-made approach to bootstrapping businesses, cash flow management, and building wealth", "style": "creative", "expertise": ["Bootstrapping", "Cash Flow"], "image": "Sara_Blakely.png"}
}

st.set_page_config(page_title="HerStory", page_icon="👩", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Poppins:wght@400;500;600;700&display=swap');
    #MainMenu, footer, header {visibility: hidden;}
    * {font-family: 'Poppins', sans-serif;}
    
    .stApp {
        background: linear-gradient(135deg, #FFF5F7 0%, #FFF0F5 25%, #F0F8FF 50%, #FFF8F0 75%, #F5F0FF 100%);
        background-size: 400% 400%;
        animation: bgFlow 25s ease infinite;
    }
    @keyframes bgFlow {
        0%, 100% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
    }
    
    .hero-title {
        text-align: center;
        font-size: 5rem;
        font-weight: 900;
        font-family: 'Playfair Display', serif;
        background: linear-gradient(135deg, #C9A0DC 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 50px 0 80px;
        letter-spacing: 3px;
        animation: titleFloat 4s ease-in-out infinite;
    }
    @keyframes titleFloat {
        0%, 100% {transform: translateY(0);}
        50% {transform: translateY(-10px);}
    }
    
    .carousel-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 40px;
        margin: 60px auto;
        max-width: 1400px;
        perspective: 1500px;
    }
    
    .arrow-btn {
        background: linear-gradient(135deg, #C9A0DC, #764ba2);
        border: none;
        border-radius: 50%;
        width: 70px;
        height: 70px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: 0 10px 40px rgba(201, 160, 220, 0.4);
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        font-size: 28px;
        color: white;
    }
    
    .arrow-btn:hover {
        transform: scale(1.15);
        box-shadow: 0 15px 50px rgba(201, 160, 220, 0.6);
    }
    
    .leader-card {
        background: white;
        border-radius: 50px;
        padding: 60px 80px;
        box-shadow: 0 30px 80px rgba(0, 0, 0, 0.15);
        text-align: center;
        max-width: 700px;
        border: 3px solid rgba(201, 160, 220, 0.3);
        animation: cardPop 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
        transition: all 0.6s ease;
        position: relative;
    }
    
    @keyframes cardPop {
        0% {
            opacity: 0;
            transform: scale(0.5) translateY(50px);
        }
        100% {
            opacity: 1;
            transform: scale(1) translateY(0);
        }
    }
    
    .leader-card:hover {
        transform: scale(1.05) translateY(-15px);
        box-shadow: 0 40px 100px rgba(201, 160, 220, 0.35);
    }
    
    .curved-text {
        font-size: 2rem;
        font-weight: 700;
        color: #764ba2;
        margin-bottom: 30px;
        font-family: 'Playfair Display', serif;
        letter-spacing: 1px;
    }
    
    .profile-container {
        position: relative;
        width: 280px;
        height: 280px;
        margin: 30px auto 40px;
        transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    .leader-card:hover .profile-container {
        transform: scale(1.12) translateZ(50px);
    }
    
    .profile-img {
        width: 280px;
        height: 280px;
        border-radius: 50%;
        object-fit: cover;
        border: 8px solid white;
        box-shadow: 
            0 25px 60px rgba(0, 0, 0, 0.2),
            0 0 0 15px rgba(201, 160, 220, 0.15),
            inset 0 0 50px rgba(201, 160, 220, 0.1);
        transition: all 0.6s ease;
    }
    
    .leader-card:hover .profile-img {
        box-shadow: 
            0 35px 80px rgba(201, 160, 220, 0.4),
            0 0 0 20px rgba(201, 160, 220, 0.3),
            inset 0 0 80px rgba(201, 160, 220, 0.2);
    }
    
    .leader-name {
        font-size: 2.5rem;
        font-weight: 800;
        color: #2D3748;
        margin: 20px 0 10px;
        font-family: 'Playfair Display', serif;
    }
    
    .leader-title {
        font-size: 1.3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #C9A0DC, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 25px;
    }
    
    .leader-specialty {
        font-size: 1.05rem;
        color: #4A5568;
        line-height: 1.8;
        margin-bottom: 30px;
        font-weight: 500;
    }
    
    .expertise-tags {
        display: flex;
        justify-content: center;
        gap: 12px;
        flex-wrap: wrap;
        margin-bottom: 35px;
    }
    
    .tag {
        background: linear-gradient(135deg, #C9A0DC, #764ba2);
        color: white;
        padding: 10px 24px;
        border-radius: 25px;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 6px 20px rgba(201, 160, 220, 0.35);
        transition: all 0.3s ease;
    }
    
    .tag:hover {
        transform: translateY(-3px) scale(1.08);
        box-shadow: 0 10px 30px rgba(201, 160, 220, 0.5);
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #C9A0DC, #764ba2);
        color: white;
        border: none;
        border-radius: 35px;
        padding: 18px 50px;
        font-weight: 700;
        font-size: 16px;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        box-shadow: 0 12px 40px rgba(201, 160, 220, 0.4);
        border: 2px solid transparent;
    }
    
    .stButton>button:hover {
        transform: translateY(-5px) scale(1.08);
        box-shadow: 0 18px 50px rgba(201, 160, 220, 0.6);
        border-color: rgba(255, 255, 255, 0.5);
    }
    
    .chat-header {
        background: white;
        padding: 35px;
        border-radius: 35px;
        margin-bottom: 30px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.12);
        border: 2px solid rgba(201, 160, 220, 0.3);
    }
    
    .user-msg {
        background: linear-gradient(135deg, #C9A0DC, #764ba2);
        color: white;
        padding: 18px 26px;
        border-radius: 28px 28px 8px 28px;
        margin: 14px 0;
        margin-left: auto;
        max-width: 70%;
        box-shadow: 0 10px 30px rgba(201, 160, 220, 0.4);
        font-weight: 500;
    }
    
    .assistant-msg {
        background: white;
        color: #2D3748;
        padding: 18px 26px;
        border-radius: 28px 28px 28px 8px;
        margin: 14px 0;
        max-width: 70%;
        border: 2px solid rgba(201, 160, 220, 0.2);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        font-weight: 500;
    }
    
    .stTextInput>div>div>input {
        background: white;
        border: 2px solid rgba(201, 160, 220, 0.3);
        border-radius: 28px;
        padding: 18px 26px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #C9A0DC;
        box-shadow: 0 0 40px rgba(201, 160, 220, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Session State
for key, default in [("messages", {name: [{"role": "system", "content": f"You are {name}, a {leaders[name]['style']} financial expert specializing in {leaders[name]['title']}."}] for name in leaders}), ("selected_leader", None), ("typing", False), ("current_index", 0)]:
    if key not in st.session_state:
        st.session_state[key] = default

leaders_list = list(leaders.keys())

# Main Page
if not st.session_state.selected_leader:
    st.markdown('<h1 class="hero-title">Welcome to HerStory!</h1>', unsafe_allow_html=True)
    
    # Carousel
    col1, col2, col3 = st.columns([1, 6, 1])
    
    with col1:
        if st.button("←", key="prev"):
            st.session_state.current_index = (st.session_state.current_index - 1) % len(leaders_list)
            st.rerun()
    
    with col2:
        current_name = leaders_list[st.session_state.current_index]
        leader = leaders[current_name]
        
        st.markdown(f"""
        <div class="leader-card">
            <p class="curved-text">Hi, I'm {current_name.split()[0]}. Let's Chat!</p>
            
            <div class="profile-container">
                {"<img src='" + leader['image'] + "' class='profile-img' />" if os.path.exists(leader['image']) else f"<div class='profile-img' style='background: linear-gradient(135deg, #FFD6E8, #C9A0DC); display: flex; align-items: center; justify-content: center; font-size: 100px;'>👩</div>"}
            </div>
            
            <h2 class="leader-name">{current_name}</h2>
            <p class="leader-title">{leader['title']}</p>
            <p class="leader-specialty">{leader['specialty']}</p>
            
            <div class="expertise-tags">
                {"".join([f"<span class='tag'>{exp}</span>" for exp in leader['expertise']])}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.button("Start Chatting", key="start", width='stretch', type="primary", on_click=lambda: setattr(st.session_state, 'selected_leader', current_name))
    
    with col3:
        if st.button("→", key="next"):
            st.session_state.current_index = (st.session_state.current_index + 1) % len(leaders_list)
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
        st.markdown(f"""
        <div class="chat-header">
            <div style="display: flex; align-items: center; gap: 30px;">
                <div style="width: 90px; height: 90px; background: linear-gradient(135deg, #FFD6E8, #C9A0DC); border-radius: 30px; display: flex; align-items: center; justify-content: center; font-size: 48px; border: 4px solid rgba(201, 160, 220, 0.3); box-shadow: 0 10px 30px rgba(0,0,0,0.15);">
                    👩
                </div>
                <div>
                    <h2 style="color: #2D3748; margin: 0; font-size: 38px; font-weight: 900; font-family: 'Playfair Display', serif;">{name}</h2>
                    <p style="background: linear-gradient(135deg, #C9A0DC, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 8px 0; font-size: 18px; font-weight: 700;">{leader['title']}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
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
