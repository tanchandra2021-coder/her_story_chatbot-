import streamlit as st
from openai import OpenAI
import os

# OpenAI API Key
OPENAI_API_KEY = "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"
client = OpenAI(api_key=OPENAI_API_KEY)

# Leaders Dictionary
leaders = {
    "Michelle Obama": {
        "title": "Education & Social Impact",
        "description": "Learn about financial literacy through education reform and community investment strategies",
        "style": "inspiring and empowering",
        "expertise": ["Impact Investing", "Education Finance", "Nonprofit Strategy"],
        "image": "michelle_obama.png",
        "gradient": "linear-gradient(135deg, #FFD3E1 0%, #C9A0DC 100%)",
        "emoji": "🌸",
        "topics": ["Personal Finance", "Education", "Social Impact"],
        "fun_fact": "Learn about personal finance with Michelle Obama!"
    },
    "Angela Merkel": {
        "title": "Economic Policy Expert",
        "description": "Analytical approach to fiscal policy, European economics, and strategic financial planning",
        "style": "analytical and methodical",
        "expertise": ["Fiscal Policy", "European Markets", "Economic Strategy"],
        "image": "Angela_Merkel.png",
        "gradient": "linear-gradient(135deg, #FFE5E5 0%, #D4B5FF 100%)",
        "emoji": "📊",
        "topics": ["Economic Policy", "Government Finance", "Strategic Planning"],
        "fun_fact": "Explore fiscal policy with Angela Merkel!"
    },
    "Malala Yousafzai": {
        "title": "Social Finance Advocate",
        "description": "Passionate insights on funding education, microfinance, and investing in social change",
        "style": "passionate and principled",
        "expertise": ["Microfinance", "Social Bonds", "Education Funding"],
        "image": "Malala_Yousafazi.png",
        "gradient": "linear-gradient(135deg, #B8E8FC 0%, #D4F1F4 100%)",
        "emoji": "💙",
        "topics": ["Microfinance", "Education", "Social Change"],
        "fun_fact": "Discover microfinance with Malala!"
    },
    "Ruth Bader Ginsburg": {
        "title": "Financial Law & Ethics",
        "description": "Precise guidance on financial regulations, investment law, and ethical wealth management",
        "style": "precise and principled",
        "expertise": ["Financial Law", "Securities", "Compliance"],
        "image": "Ruth_Bader_Ginsburg.png",
        "gradient": "linear-gradient(135deg, #D4F4DD 0%, #BFECFF 100%)",
        "emoji": "⚖️",
        "topics": ["Financial Law", "Ethics", "Compliance"],
        "fun_fact": "Navigate financial regulations with RBG!"
    },
    "Indra Nooyi": {
        "title": "Corporate Finance Leader",
        "description": "Strategic insights on corporate finance, M&A, sustainable business growth, and CFO excellence",
        "style": "strategic and visionary",
        "expertise": ["Corporate Finance", "M&A", "Business Strategy"],
        "image": "Indra_Nooyi.png",
        "gradient": "linear-gradient(135deg, #FFE8D1 0%, #FFD1DC 100%)",
        "emoji": "💼",
        "topics": ["Finance Careers", "Corporate Strategy", "Leadership"],
        "fun_fact": "Learn corporate finance from Indra Nooyi!"
    },
    "Sheryl Sandberg": {
        "title": "Tech Finance Executive",
        "description": "Data-driven approach to tech valuations, scaling startups, and financial operations",
        "style": "analytical and motivational",
        "expertise": ["Tech Finance", "Scaling", "Operations"],
        "image": "Sheryl_Sandberg.png",
        "gradient": "linear-gradient(135deg, #E0BBE4 0%, #D4F1F9 100%)",
        "emoji": "💻",
        "topics": ["Tech Finance", "Startups", "Scaling"],
        "fun_fact": "Scale your startup with Sheryl Sandberg!"
    },
    "Jacinda Ardern": {
        "title": "Wellbeing Economics",
        "description": "Compassionate approach to budget management, public finance, and wellbeing economics",
        "style": "empathetic and pragmatic",
        "expertise": ["Public Finance", "Budget Policy", "Wellbeing Economy"],
        "image": "Jacinda_Ardern.png",
        "gradient": "linear-gradient(135deg, #FFE5F1 0%, #D4EFDF 100%)",
        "emoji": "🌿",
        "topics": ["Public Finance", "Wellbeing", "Budget Management"],
        "fun_fact": "Explore wellbeing economics with Jacinda!"
    },
    "Mae Jemison": {
        "title": "STEM Finance Pioneer",
        "description": "Innovative thinking on R&D funding, STEM investment, and technology venture capital",
        "style": "innovative and scientific",
        "expertise": ["Venture Capital", "R&D Finance", "Tech Investment"],
        "image": "Mae_Jemison.png",
        "gradient": "linear-gradient(135deg, #FFD6E8 0%, #E8D4F2 100%)",
        "emoji": "🚀",
        "topics": ["Venture Capital", "STEM", "Innovation"],
        "fun_fact": "Invest in the future with Mae Jemison!"
    },
    "Reshma Saujani": {
        "title": "Startup Finance Advocate",
        "description": "Bold approach to fundraising, startup equity, and building financial resilience in tech",
        "style": "bold and resourceful",
        "expertise": ["Fundraising", "Startup Equity", "Angel Investing"],
        "image": "Reshman_Saujani.png",
        "gradient": "linear-gradient(135deg, #FFF0E5 0%, #E5E5FF 100%)",
        "emoji": "🎯",
        "topics": ["Fundraising", "Startups", "Tech"],
        "fun_fact": "Master fundraising with Reshma Saujani!"
    },
    "Sara Blakely": {
        "title": "Bootstrap Finance Expert",
        "description": "Self-made approach to bootstrapping businesses, cash flow management, and building wealth",
        "style": "creative and determined",
        "expertise": ["Bootstrapping", "Cash Flow", "Wealth Building"],
        "image": "Sara_Blakely.png",
        "gradient": "linear-gradient(135deg, #FFEEF8 0%, #FFEAA7 100%)",
        "emoji": "✨",
        "topics": ["Entrepreneurship", "Wealth Building", "Bootstrapping"],
        "fun_fact": "Build your empire with Sara Blakely!"
    }
}

# Page Configuration
st.set_page_config(
    page_title="Finance Leaders AI Chat",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background: linear-gradient(-45deg, #0a0e27, #16213e, #0f3460, #1a1a2e);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .main-title {
        text-align: center;
        font-size: 5rem;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 20px;
        letter-spacing: 8px;
        font-family: 'Orbitron', sans-serif;
        text-transform: uppercase;
        animation: titleGlow 3s ease-in-out infinite;
        text-shadow: 0 0 20px rgba(100, 200, 255, 0.8), 0 0 40px rgba(100, 200, 255, 0.4);
    }
    
    @keyframes titleGlow {
        0%, 100% { text-shadow: 0 0 20px rgba(100, 200, 255, 0.8); }
        50% { text-shadow: 0 0 40px rgba(100, 200, 255, 1); }
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.5rem;
        color: #64c8ff;
        margin-bottom: 20px;
        font-weight: 600;
        letter-spacing: 3px;
        text-transform: uppercase;
        font-family: 'Rajdhani', sans-serif;
    }
    
    .greeting-box {
        text-align: center;
        background: rgba(100, 200, 255, 0.1);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(100, 200, 255, 0.3);
        padding: 20px 40px;
        border-radius: 50px;
        margin: 30px auto 50px;
        max-width: 600px;
        animation: pulseGlow 2s ease-in-out infinite;
    }
    
    @keyframes pulseGlow {
        0%, 100% { box-shadow: 0 0 20px rgba(100, 200, 255, 0.3); }
        50% { box-shadow: 0 0 30px rgba(100, 200, 255, 0.6); }
    }
    
    .leader-card {
        background: rgba(20, 30, 60, 0.8);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 2px solid rgba(100, 200, 255, 0.3);
        overflow: hidden;
        transition: all 0.5s ease;
        cursor: pointer;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        animation: fadeInUp 0.8s ease-out backwards;
    }
    
    .leader-card:hover {
        transform: translateY(-15px) scale(1.05);
        box-shadow: 0 20px 60px rgba(100, 200, 255, 0.4);
        border-color: rgba(100, 200, 255, 0.8);
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .emoji-badge {
        position: absolute;
        top: 15px;
        right: 15px;
        width: 60px;
        height: 60px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 32px;
        z-index: 10;
        border: 2px solid rgba(100, 200, 255, 0.4);
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #64c8ff 0%, #9696ff 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 14px 35px;
        font-weight: 700;
        transition: all 0.4s ease;
        box-shadow: 0 8px 25px rgba(100, 200, 255, 0.4);
        text-transform: uppercase;
        letter-spacing: 2px;
        font-family: 'Rajdhani', sans-serif;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 12px 40px rgba(100, 200, 255, 0.6);
    }
    
    .chat-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        padding: 35px;
        border-radius: 25px;
        margin-bottom: 30px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        border: 2px solid rgba(100, 200, 255, 0.3);
        animation: zoomIn 0.8s ease-out;
    }
    
    @keyframes zoomIn {
        from { opacity: 0; transform: scale(0.3); }
        to { opacity: 1; transform: scale(1); }
    }
    
    .user-message {
        background: linear-gradient(135deg, #64c8ff 0%, #9696ff 100%);
        color: white;
        padding: 18px 25px;
        border-radius: 25px 25px 5px 25px;
        margin: 14px 0;
        margin-left: auto;
        max-width: 70%;
        box-shadow: 0 8px 25px rgba(100, 200, 255, 0.4);
        animation: slideInRight 0.5s ease-out;
    }
    
    .assistant-message {
        background: rgba(30, 40, 70, 0.8);
        backdrop-filter: blur(20px);
        color: #ffffff;
        padding: 18px 25px;
        border-radius: 25px 25px 25px 5px;
        margin: 14px 0;
        max-width: 70%;
        border: 2px solid rgba(100, 200, 255, 0.3);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
        animation: slideInLeft 0.5s ease-out;
    }
    
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(50px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-50px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .stTextInput>div>div>input {
        background: rgba(30, 40, 70, 0.8);
        backdrop-filter: blur(20px);
        border: 2px solid rgba(100, 200, 255, 0.3);
        border-radius: 25px;
        color: #ffffff;
        padding: 16px 25px;
        font-size: 16px;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #64c8ff;
        box-shadow: 0 0 20px rgba(100, 200, 255, 0.5);
    }
    
    .section-title {
        color: #ffffff;
        font-size: 2rem;
        font-weight: 800;
        text-align: center;
        margin: 40px 0;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 3px;
        text-shadow: 0 0 20px rgba(100, 200, 255, 0.6);
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = {
        name: [{"role": "system", "content": f"You are {name}, a financial expert with expertise in {leaders[name]['expertise'][0]}. You speak in a {leaders[name]['style']} style. Provide insightful financial advice related to {leaders[name]['title']}."}]
        for name in leaders
    }

if "selected_leader" not in st.session_state:
    st.session_state.selected_leader = None

if "typing" not in st.session_state:
    st.session_state.typing = False

if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = None

# Leader Selection Page
if st.session_state.selected_leader is None:
    st.markdown('<h1 class="main-title">FINANCE LEADERS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Visionaries Who Changed the World</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="greeting-box">
        <p style="color: #ffffff; font-size: 1.3rem; font-weight: 600; margin: 0; font-family: 'Rajdhani', sans-serif; letter-spacing: 2px;">
            👋 Hello, ready to chat with these inspiring leaders?
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Topic selection
    st.markdown('<h2 class="section-title">RECOMMENDED FOR YOU</h2>', unsafe_allow_html=True)
    
    topic_cols = st.columns(5)
    topics = ["Finance Careers", "Personal Finance", "Startups", "Social Impact", "Tech Finance"]
    
    for idx, topic in enumerate(topics):
        with topic_cols[idx]:
            if st.button(topic, key=f"topic_{idx}", width='stretch'):
                st.session_state.selected_topic = topic
                st.rerun()
    
    if st.session_state.selected_topic:
        recommended = [name for name, info in leaders.items() if st.session_state.selected_topic in info['topics']]
        
        if recommended:
            st.markdown(f"""
            <div style="text-align: center; margin: 30px 0;">
                <p style="color: #64c8ff; font-size: 1.2rem; font-weight: 600;">
                    Top leaders for {st.session_state.selected_topic}
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="section-title">ALL LEADERS</h2>', unsafe_allow_html=True)
    
    # First Row - 5 Leaders
    cols1 = st.columns(5, gap="large")
    leader_names = list(leaders.keys())
    
    for idx, col in enumerate(cols1):
        if idx < len(leader_names):
            leader_name = leader_names[idx]
            leader = leaders[leader_name]
            
            with col:
                st.markdown(f'<div class="leader-card" style="animation-delay: {idx * 0.1}s; position: relative;">', unsafe_allow_html=True)
                st.markdown(f'<div class="emoji-badge">{leader["emoji"]}</div>', unsafe_allow_html=True)
                
                if os.path.exists(leader['image']):
                    st.image(leader['image'], width='stretch')
                else:
                    st.markdown(f"""
                    <div style="width: 100%; height: 220px; background: {leader['gradient']}; display: flex; align-items: center; justify-content: center; font-size: 80px;">
                        {leader['emoji']}
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div style="padding: 20px;">
                    <h3 style="color: #ffffff; font-size: 20px; font-weight: 800; margin-bottom: 8px; font-family: 'Orbitron', sans-serif;">
                        {leader_name}
                    </h3>
                    <p style="color: #64c8ff; font-size: 14px; margin-bottom: 12px; font-weight: 700;">{leader['title']}</p>
                    <p style="color: #a0aec0; font-size: 12px; line-height: 1.6; margin-bottom: 15px;">{leader['description']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                if st.button("Start Chat", key=f"btn_{idx}", width='stretch'):
                    st.session_state.selected_leader = leader_name
                    st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Second Row - 5 Leaders
    cols2 = st.columns(5, gap="large")
    
    for idx, col in enumerate(cols2):
        actual_idx = idx + 5
        if actual_idx < len(leader_names):
            leader_name = leader_names[actual_idx]
            leader = leaders[leader_name]
            
            with col:
                st.markdown(f'<div class="leader-card" style="animation-delay: {(idx + 5) * 0.1}s; position: relative;">', unsafe_allow_html=True)
                st.markdown(f'<div class="emoji-badge">{leader["emoji"]}</div>', unsafe_allow_html=True)
                
                if os.path.exists(leader['image']):
                    st.image(leader['image'], width='stretch')
                else:
                    st.markdown(f"""
                    <div style="width: 100%; height: 220px; background: {leader['gradient']}; display: flex; align-items: center; justify-content: center; font-size: 80px;">
                        {leader['emoji']}
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div style="padding: 20px;">
                    <h3 style="color: #ffffff; font-size: 20px; font-weight: 800; margin-bottom: 8px; font-family: 'Orbitron', sans-serif;">
                        {leader_name}
                    </h3>
                    <p style="color: #64c8ff; font-size: 14px; margin-bottom: 12px; font-weight: 700;">{leader['title']}</p>
                    <p style="color: #a0aec0; font-size: 12px; line-height: 1.6; margin-bottom: 15px;">{leader['description']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                if st.button("Start Chat", key=f"btn_{actual_idx}", width='stretch'):
                    st.session_state.selected_leader = leader_name
                    st.rerun()

# Chat Page
else:
    leader_name = st.session_state.selected_leader
    leader = leaders[leader_name]
    
    col1, col2 = st.columns([1, 8])
    
    with col1:
        if st.button("← Back", key="back_button"):
            st.session_state.selected_leader = None
            st.session_state.selected_topic = None
            st.rerun()
    
    with col2:
        st.markdown(f"""
        <div class="chat-header">
            <div style="display: flex; align-items: center; gap: 30px;">
                <div style="width: 90px; height: 90px; background: rgba(100, 200, 255, 0.2); border-radius: 25px; display: flex; align-items: center; justify-content: center; font-size: 48px; border: 3px solid rgba(100, 200, 255, 0.5); animation: float 3s ease-in-out infinite;">
                    {leader['emoji']}
                </div>
                <div>
                    <h2 style="color: #ffffff; margin: 0; font-size: 38px; font-weight: 900; font-family: 'Orbitron', sans-serif; text-shadow: 0 0 20px rgba(100, 200, 255, 0.6);">{leader_name}</h2>
                    <p style="color: #64c8ff; margin: 10px 0; font-size: 18px; font-weight: 700;">{leader['title']}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Chat messages
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.messages[leader_name][1:]:
            if msg["role"] == "user":
                st.markdown(f'<div style="display: flex; justify-content: flex-end;"><div class="user-message">{msg["content"]}</div></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="assistant-message">{msg["content"]}</div>', unsafe_allow_html=True)
        
        if st.session_state.typing:
            st.markdown('<div class="assistant-message"><p style="margin: 0;">Thinking...</p></div>', unsafe_allow_html=True)
    
    # Chat input
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([6, 1])
    
    with col1:
        user_input = st.text_input(
            "Message",
            placeholder=f"Ask {leader_name.split()[0]} about {leader['expertise'][0].lower()}...",
            key="user_input",
            label_visibility="collapsed"
        )
    
    with col2:
        send_button = st.button("Send", width='stretch')
    
    if send_button and user_input:
        st.session_state.messages[leader_name].append({"role": "user", "content": user_input})
        st.session_state.typing = True
        st.rerun()
    
    if st.session_state.typing:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages[leader_name],
                temperature=0.7,
                max_tokens=400
            )
            reply = response.choices[0].message.content
            
            st.session_state.messages[leader_name].append({"role": "assistant", "content": reply})
            st.session_state.typing = False
            st.rerun()
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.session_state.typing = False
