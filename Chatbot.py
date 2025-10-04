import streamlit as st
from openai import OpenAI
import os

# SECURITY WARNING: Remove this API key and use environment variables instead!
OPENAI_API_KEY = "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"
client = OpenAI(api_key=OPENAI_API_KEY)

leaders = {
    "Michelle Obama": {
        "title": "Education & Social Impact 📚",
        "specialty": "Passionate about financial literacy through education reform and community investment strategies. Empowering communities through strategic financial planning.",
        "style": "inspiring",
        "expertise": ["Impact Investing", "Education Finance"],
        "image": "michelle_obama.png"
    },
    "Angela Merkel": {
        "title": "Economic Policy Expert 📊",
        "specialty": "Analytical approach to fiscal policy, European economics, and strategic financial planning. Bringing decades of economic leadership experience.",
        "style": "analytical",
        "expertise": ["Fiscal Policy", "Economic Strategy"],
        "image": "Angela_Merkel.png"
    },
    "Malala Yousafzai": {
        "title": "Social Finance Advocate 🌍",
        "specialty": "Passionate insights on funding education, microfinance, and investing in social change. Championing financial empowerment for all.",
        "style": "passionate",
        "expertise": ["Microfinance", "Social Bonds"],
        "image": "Malala_Yousafazi.png"
    },
    "Ruth Bader Ginsburg": {
        "title": "Financial Law & Ethics ⚖️",
        "specialty": "Precise guidance on financial regulations, investment law, and ethical wealth management. Justice in every financial decision.",
        "style": "precise",
        "expertise": ["Financial Law", "Securities"],
        "image": "Ruth_Bader_Ginsburg.png"
    },
    "Indra Nooyi": {
        "title": "Corporate Finance Leader 💼",
        "specialty": "Strategic insights on corporate finance, M&A, sustainable business growth, and CFO excellence. Transforming businesses through financial innovation.",
        "style": "strategic",
        "expertise": ["Corporate Finance", "M&A"],
        "image": "Indra_Nooyi.png"
    },
    "Sheryl Sandberg": {
        "title": "Tech Finance Executive 💻",
        "specialty": "Data-driven approach to tech valuations, scaling startups, and financial operations. Building the future of tech finance.",
        "style": "analytical",
        "expertise": ["Tech Finance", "Scaling"],
        "image": "Sheryl_Sandberg.png"
    },
    "Jacinda Ardern": {
        "title": "Wellbeing Economics 🌱",
        "specialty": "Compassionate approach to budget management, public finance, and wellbeing economics. Putting people at the center of financial policy.",
        "style": "empathetic",
        "expertise": ["Public Finance", "Budget Policy"],
        "image": "Jacinda_Ardern.png"
    },
    "Mae Jemison": {
        "title": "STEM Finance Pioneer 🚀",
        "specialty": "Innovative thinking on R&D funding, STEM investment, and technology venture capital. Pioneering the frontier of innovation finance.",
        "style": "innovative",
        "expertise": ["Venture Capital", "R&D Finance"],
        "image": "Mae_Jemison.png"
    },
    "Reshma Saujani": {
        "title": "Startup Finance Advocate 🚀",
        "specialty": "Bold approach to fundraising, startup equity, and building financial resilience in tech. Breaking barriers in venture capital.",
        "style": "bold",
        "expertise": ["Fundraising", "Startup Equity"],
        "image": "Reshman_Saujani.png"
    },
    "Sara Blakely": {
        "title": "Bootstrap Finance Expert 💪",
        "specialty": "Self-made approach to bootstrapping businesses, cash flow management, and building wealth. Turning ideas into billion-dollar businesses.",
        "style": "creative",
        "expertise": ["Bootstrapping", "Cash Flow"],
        "image": "Sara_Blakely.png"
    }
}

st.set_page_config(page_title="HerStory", page_icon="👩", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Poppins:wght@400;500;600;700&display=swap');
    
    #MainMenu, footer, header {visibility: hidden;}
    .stApp {
        background: linear-gradient(135deg, #FFF5F7 0%, #FFE5F0 25%, #F0F8FF 50%, #FFF8F0 75%, #F5F0FF 100%);
        background-size: 400% 400%;
        animation: bgFlow 20s ease infinite;
    }
    
    @keyframes bgFlow {
        0%, 100% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
    }
    
    .hero-title {
        text-align: center;
        font-size: 4.5rem;
        font-weight: 900;
        font-family: 'Playfair Display', serif;
        background: linear-gradient(135deg, #E91E63 0%, #9C27B0 50%, #673AB7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 40px 0 60px;
        letter-spacing: 2px;
        animation: titleFloat 3s ease-in-out infinite;
    }
    
    @keyframes titleFloat {
        0%, 100% {transform: translateY(0);}
        50% {transform: translateY(-8px);}
    }
    
    .carousel-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 30px;
        margin: 0 auto;
        max-width: 1200px;
        padding: 20px;
    }
    
    .leader-card {
        background: white;
        border-radius: 40px;
        padding: 50px 60px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
        text-align: center;
        width: 100%;
        max-width: 600px;
        margin: 0 auto;
        animation: cardPop 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
        position: relative;
        border: 3px solid rgba(233, 30, 99, 0.2);
    }
    
    @keyframes cardPop {
        0% {
            opacity: 0;
            transform: scale(0.8) translateY(30px);
        }
        100% {
            opacity: 1;
            transform: scale(1) translateY(0);
        }
    }
    
    .curved-text {
        font-size: 1.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #E91E63, #9C27B0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 30px;
        font-family: 'Playfair Display', serif;
        letter-spacing: 1px;
    }
    
    .profile-container {
        width: 240px;
        height: 240px;
        margin: 0 auto 30px;
        position: relative;
        animation: popIn 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    @keyframes popIn {
        0% {
            transform: scale(0);
            opacity: 0;
        }
        60% {
            transform: scale(1.15);
        }
        100% {
            transform: scale(1);
            opacity: 1;
        }
    }
    
    .profile-img {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        object-fit: cover;
        border: 6px solid white;
        box-shadow: 
            0 20px 50px rgba(0, 0, 0, 0.2),
            0 0 0 12px rgba(233, 30, 99, 0.15);
    }
    
    .leader-name {
        font-size: 2.2rem;
        font-weight: 800;
        color: #2D3748;
        margin: 20px 0 10px;
        font-family: 'Playfair Display', serif;
    }
    
    .leader-title {
        font-size: 1.2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #E91E63, #9C27B0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
    }
    
    .leader-specialty {
        font-size: 1rem;
        color: #4A5568;
        line-height: 1.7;
        margin-bottom: 25px;
        font-weight: 500;
    }
    
    .expertise-tags {
        display: flex;
        justify-content: center;
        gap: 10px;
        flex-wrap: wrap;
        margin-bottom: 30px;
    }
    
    .tag {
        background: linear-gradient(135deg, #E91E63, #9C27B0);
        color: white;
        padding: 8px 20px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(233, 30, 99, 0.3);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #E91E63, #9C27B0) !important;
        color: white !important;
        border: none !important;
        border-radius: 30px !important;
        padding: 15px 40px !important;
        font-weight: 700 !important;
        font-size: 15px !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 30px rgba(233, 30, 99, 0.4) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05) !important;
        box-shadow: 0 15px 40px rgba(233, 30, 99, 0.5) !important;
    }
    
    div[data-testid="column"] > div > div > button {
        background: linear-gradient(135deg, #E91E63, #9C27B0) !important;
        border: none !important;
        border-radius: 50% !important;
        width: 60px !important;
        height: 60px !important;
        font-size: 24px !important;
        color: white !important;
        box-shadow: 0 8px 25px rgba(233, 30, 99, 0.4) !important;
        transition: all 0.3s ease !important;
        cursor: pointer !important;
    }
    
    div[data-testid="column"] > div > div > button:hover {
        transform: scale(1.15) !important;
        box-shadow: 0 12px 35px rgba(233, 30, 99, 0.6) !important;
    }
    
    .chat-header {
        background: white;
        padding: 30px;
        border-radius: 30px;
        margin-bottom: 25px;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.1);
        border: 2px solid rgba(233, 30, 99, 0.2);
    }
    
    .user-msg {
        background: linear-gradient(135deg, #E91E63, #9C27B0);
        color: white;
        padding: 15px 22px;
        border-radius: 25px 25px 5px 25px;
        margin: 12px 0;
        margin-left: auto;
        max-width: 70%;
        box-shadow: 0 8px 25px rgba(233, 30, 99, 0.3);
        font-weight: 500;
    }
    
    .assistant-msg {
        background: white;
        color: #2D3748;
        padding: 15px 22px;
        border-radius: 25px 25px 25px 5px;
        margin: 12px 0;
        max-width: 70%;
        border: 2px solid rgba(233, 30, 99, 0.2);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
        font-weight: 500;
    }
    
    .stTextInput > div > div > input {
        background: white !important;
        border: 2px solid rgba(233, 30, 99, 0.3) !important;
        border-radius: 25px !important;
        padding: 15px 22px !important;
        font-size: 15px !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #E91E63 !important;
        box-shadow: 0 0 30px rgba(233, 30, 99, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = {
        name: [{"role": "system", "content": f"You are {name}, a {leaders[name]['style']} financial expert specializing in {leaders[name]['title']}. Provide helpful, insightful advice in your unique style."}] 
        for name in leaders
    }
if "selected_leader" not in st.session_state:
    st.session_state.selected_leader = None
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "typing" not in st.session_state:
    st.session_state.typing = False

leaders_list = list(leaders.keys())

# Main Page - Carousel
if not st.session_state.selected_leader:
    st.markdown('<h1 class="hero-title">Welcome to HerStory!</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 6, 1])
    
    with col1:
        if st.button("←", key="prev_btn"):
            st.session_state.current_index = (st.session_state.current_index - 1) % len(leaders_list)
            st.rerun()
    
    with col2:
        current_name = leaders_list[st.session_state.current_index]
        leader = leaders[current_name]
        first_name = current_name.split()[0]
        
        st.markdown(f"""
        <div class="leader-card">
            <p class="curved-text">Hi, I'm {first_name}. Let's Chat!</p>
            
            <div class="profile-container">
                <img src="https://via.placeholder.com/240/E91E63/FFFFFF?text={first_name[0]}" class="profile-img" alt="{current_name}">
            </div>
            
            <h2 class="leader-name">{current_name}</h2>
            <p class="leader-title">{leader['title']}</p>
            <p class="leader-specialty">{leader['specialty']}</p>
            
            <div class="expertise-tags">
                {''.join([f'<span class="tag">{exp}</span>' for exp in leader['expertise']])}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Start Chatting", key="start_chat", use_container_width=True):
            st.session_state.selected_leader = current_name
            st.rerun()
    
    with col3:
        if st.button("→", key="next_btn"):
            st.session_state.current_index = (st.session_state.current_index + 1) % len(leaders_list)
            st.rerun()

# Chat Page
else:
    name = st.session_state.selected_leader
    leader = leaders[name]
    first_name = name.split()[0]
    
    col_back, col_header = st.columns([1, 8])
    
    with col_back:
        if st.button("← Back", key="back_btn"):
            st.session_state.selected_leader = None
            st.rerun()
    
    with col_header:
        st.markdown(f"""
        <div class="chat-header">
            <div style="display: flex; align-items: center; gap: 25px;">
                <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #E91E63, #9C27B0); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 40px; border: 4px solid white; box-shadow: 0 8px 25px rgba(233, 30, 99, 0.3);">
                    {first_name[0]}
                </div>
                <div>
                    <h2 style="color: #2D3748; margin: 0; font-size: 32px; font-weight: 900; font-family: 'Playfair Display', serif;">{name}</h2>
                    <p style="background: linear-gradient(135deg, #E91E63, #9C27B0); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 5px 0 0 0; font-size: 16px; font-weight: 700;">{leader['title']}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Display chat messages
    for msg in st.session_state.messages[name][1:]:
        css_class = "user-msg" if msg["role"] == "user" else "assistant-msg"
        align = "flex-end" if msg["role"] == "user" else "flex-start"
        st.markdown(
            f'<div style="display: flex; justify-content: {align};"><div class="{css_class}">{msg["content"]}</div></div>',
            unsafe_allow_html=True
        )
    
    if st.session_state.typing:
        st.markdown('<div style="display: flex; justify-content: flex-start;"><div class="assistant-msg">💭 Thinking...</div></div>', unsafe_allow_html=True)
    
    # Input area
    col_input, col_send = st.columns([6, 1])
    
    with col_input:
        user_input = st.text_input(
            "Message",
            placeholder=f"Ask {first_name} about finance...",
            key="user_input",
            label_visibility="collapsed"
        )
    
    with col_send:
        send_clicked = st.button("Send", key="send_btn", use_container_width=True)
    
    if send_clicked and user_input:
        st.session_state.messages[name].append({"role": "user", "content": user_input})
        st.session_state.typing = True
        st.rerun()
    
    if st.session_state.typing:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages[name],
                temperature=0.7,
                max_tokens=400
            )
            st.session_state.messages[name].append({
                "role": "assistant",
                "content": response.choices[0].message.content
            })
            st.session_state.typing = False
            st.rerun()
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.session_state.typing = False
