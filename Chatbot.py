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
        "gradient": "linear-gradient(135deg, #FFD6E8 0%, #C9A0DC 100%)",
        "emoji": "🌸",
        "topics": ["Personal Finance", "Education", "Social Impact"]
    },
    "Angela Merkel": {
        "title": "Economic Policy Expert",
        "description": "Analytical approach to fiscal policy, European economics, and strategic financial planning",
        "style": "analytical and methodical",
        "expertise": ["Fiscal Policy", "European Markets", "Economic Strategy"],
        "image": "Angela_Merkel.png",
        "gradient": "linear-gradient(135deg, #FFC2D4 0%, #E8BFFF 100%)",
        "emoji": "📊",
        "topics": ["Economic Policy", "Government Finance", "Strategic Planning"]
    },
    "Malala Yousafzai": {
        "title": "Social Finance Advocate",
        "description": "Passionate insights on funding education, microfinance, and investing in social change",
        "style": "passionate and principled",
        "expertise": ["Microfinance", "Social Bonds", "Education Funding"],
        "image": "Malala_Yousafazi.png",
        "gradient": "linear-gradient(135deg, #A8E6FF 0%, #C8E6C9 100%)",
        "emoji": "💙",
        "topics": ["Microfinance", "Education", "Social Change"]
    },
    "Ruth Bader Ginsburg": {
        "title": "Financial Law & Ethics",
        "description": "Precise guidance on financial regulations, investment law, and ethical wealth management",
        "style": "precise and principled",
        "expertise": ["Financial Law", "Securities", "Compliance"],
        "image": "Ruth_Bader_Ginsburg.png",
        "gradient": "linear-gradient(135deg, #C8E6C9 0%, #B3E5FC 100%)",
        "emoji": "⚖️",
        "topics": ["Financial Law", "Ethics", "Compliance"]
    },
    "Indra Nooyi": {
        "title": "Corporate Finance Leader",
        "description": "Strategic insights on corporate finance, M&A, sustainable business growth, and CFO excellence",
        "style": "strategic and visionary",
        "expertise": ["Corporate Finance", "M&A", "Business Strategy"],
        "image": "Indra_Nooyi.png",
        "gradient": "linear-gradient(135deg, #FFE8C5 0%, #FFD6E8 100%)",
        "emoji": "💼",
        "topics": ["Finance Careers", "Corporate Strategy", "Leadership"]
    },
    "Sheryl Sandberg": {
        "title": "Tech Finance Executive",
        "description": "Data-driven approach to tech valuations, scaling startups, and financial operations",
        "style": "analytical and motivational",
        "expertise": ["Tech Finance", "Scaling", "Operations"],
        "image": "Sheryl_Sandberg.png",
        "gradient": "linear-gradient(135deg, #E1BEE7 0%, #B3E5FC 100%)",
        "emoji": "💻",
        "topics": ["Tech Finance", "Startups", "Scaling"]
    },
    "Jacinda Ardern": {
        "title": "Wellbeing Economics",
        "description": "Compassionate approach to budget management, public finance, and wellbeing economics",
        "style": "empathetic and pragmatic",
        "expertise": ["Public Finance", "Budget Policy", "Wellbeing Economy"],
        "image": "Jacinda_Ardern.png",
        "gradient": "linear-gradient(135deg, #FFF9C4 0%, #C8E6C9 100%)",
        "emoji": "🌿",
        "topics": ["Public Finance", "Wellbeing", "Budget Management"]
    },
    "Mae Jemison": {
        "title": "STEM Finance Pioneer",
        "description": "Innovative thinking on R&D funding, STEM investment, and technology venture capital",
        "style": "innovative and scientific",
        "expertise": ["Venture Capital", "R&D Finance", "Tech Investment"],
        "image": "Mae_Jemison.png",
        "gradient": "linear-gradient(135deg, #FFD6E8 0%, #E1BEE7 100%)",
        "emoji": "🚀",
        "topics": ["Venture Capital", "STEM", "Innovation"]
    },
    "Reshma Saujani": {
        "title": "Startup Finance Advocate",
        "description": "Bold approach to fundraising, startup equity, and building financial resilience in tech",
        "style": "bold and resourceful",
        "expertise": ["Fundraising", "Startup Equity", "Angel Investing"],
        "image": "Reshman_Saujani.png",
        "gradient": "linear-gradient(135deg, #FFE8C5 0%, #E1BEE7 100%)",
        "emoji": "🎯",
        "topics": ["Fundraising", "Startups", "Tech"]
    },
    "Sara Blakely": {
        "title": "Bootstrap Finance Expert",
        "description": "Self-made approach to bootstrapping businesses, cash flow management, and building wealth",
        "style": "creative and determined",
        "expertise": ["Bootstrapping", "Cash Flow", "Wealth Building"],
        "image": "Sara_Blakely.png",
        "gradient": "linear-gradient(135deg, #FFF9C4 0%, #FFECB3 100%)",
        "emoji": "✨",
        "topics": ["Entrepreneurship", "Wealth Building", "Bootstrapping"]
    }
}

st.set_page_config(page_title="Finance Leaders AI Chat", page_icon="💼", layout="wide", initial_sidebar_state="collapsed")

# Enhanced CSS with clean light background and WOW animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Montserrat:wght@400;600;700;800;900&display=swap');
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Clean, light, colorful animated background */
    .stApp {
        background: 
            linear-gradient(135deg, rgba(255,214,232,0.3) 0%, transparent 50%),
            linear-gradient(225deg, rgba(200,230,201,0.3) 0%, transparent 50%),
            linear-gradient(315deg, rgba(179,229,252,0.3) 0%, transparent 50%),
            linear-gradient(45deg, rgba(255,249,196,0.3) 0%, transparent 50%),
            linear-gradient(to bottom, #FFFFFF 0%, #F8F9FA 100%);
        animation: backgroundPulse 20s ease infinite;
        position: relative;
        overflow-x: hidden;
    }
    
    @keyframes backgroundPulse {
        0%, 100% { filter: brightness(1); }
        50% { filter: brightness(1.05); }
    }
    
    /* Floating particles */
    .stApp::before {
        content: '';
        position: fixed;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle, rgba(102,126,234,0.1) 1px, transparent 1px),
            radial-gradient(circle, rgba(243,129,129,0.1) 1px, transparent 1px),
            radial-gradient(circle, rgba(100,181,246,0.1) 1px, transparent 1px);
        background-size: 50px 50px, 80px 80px, 100px 100px;
        background-position: 0 0, 20px 20px, 40px 40px;
        animation: particleFloat 60s linear infinite;
        opacity: 0.6;
        pointer-events: none;
    }
    
    @keyframes particleFloat {
        0% { transform: translateY(0px); }
        100% { transform: translateY(-100px); }
    }
    
    /* Epic title with gradient and animation */
    .main-title {
        text-align: center;
        font-size: 5.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea 0%, #f093fb 25%, #764ba2 50%, #667eea 75%, #f093fb 100%);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 15px;
        letter-spacing: 6px;
        font-family: 'Montserrat', sans-serif;
        text-transform: uppercase;
        animation: gradientFlow 8s ease infinite, titleBounce 2s ease-in-out infinite;
        filter: drop-shadow(0 8px 16px rgba(102,126,234,0.3));
        position: relative;
    }
    
    @keyframes gradientFlow {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    @keyframes titleBounce {
        0%, 100% { transform: translateY(0px) scale(1); }
        50% { transform: translateY(-8px) scale(1.02); }
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.6rem;
        color: #667eea;
        margin-bottom: 25px;
        font-weight: 700;
        letter-spacing: 4px;
        text-transform: uppercase;
        font-family: 'Montserrat', sans-serif;
        animation: fadeInUp 1s ease-out 0.3s backwards;
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Greeting box with pulse */
    .greeting-box {
        text-align: center;
        background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(255,255,255,0.85));
        backdrop-filter: blur(20px);
        border: 3px solid transparent;
        background-clip: padding-box;
        padding: 25px 50px;
        border-radius: 60px;
        margin: 35px auto 60px;
        max-width: 700px;
        box-shadow: 
            0 15px 50px rgba(102,126,234,0.2),
            0 0 0 1px rgba(255,255,255,0.8) inset;
        animation: floatBox 4s ease-in-out infinite, pulseGlow 3s ease-in-out infinite;
        position: relative;
    }
    
    .greeting-box::before {
        content: '';
        position: absolute;
        inset: -3px;
        border-radius: 60px;
        padding: 3px;
        background: linear-gradient(135deg, #667eea, #f093fb, #764ba2);
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        animation: borderRotate 4s linear infinite;
    }
    
    @keyframes floatBox {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-12px); }
    }
    
    @keyframes pulseGlow {
        0%, 100% { box-shadow: 0 15px 50px rgba(102,126,234,0.2), 0 0 0 1px rgba(255,255,255,0.8) inset; }
        50% { box-shadow: 0 20px 60px rgba(102,126,234,0.35), 0 0 0 1px rgba(255,255,255,0.9) inset; }
    }
    
    @keyframes borderRotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* EXTREME 3D POP CARD EFFECT */
    .leader-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.98), rgba(255,255,255,0.92));
        backdrop-filter: blur(30px);
        border-radius: 35px;
        border: 2px solid rgba(255,255,255,0.8);
        overflow: visible;
        cursor: pointer;
        box-shadow: 
            0 15px 35px rgba(0,0,0,0.08),
            0 5px 15px rgba(0,0,0,0.05),
            0 0 0 1px rgba(255,255,255,0.9) inset;
        animation: cardEntrance 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) backwards;
        position: relative;
        transform-style: preserve-3d;
        perspective: 1000px;
        transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    @keyframes cardEntrance {
        from {
            opacity: 0;
            transform: translateY(80px) rotateX(-30deg) scale(0.7);
        }
        to {
            opacity: 1;
            transform: translateY(0) rotateX(0) scale(1);
        }
    }
    
    /* MASSIVE POP EFFECT ON HOVER */
    .leader-card:hover {
        transform: translateY(-40px) translateZ(100px) scale(1.15) rotateY(-8deg) rotateX(8deg);
        box-shadow: 
            0 50px 100px rgba(102,126,234,0.35),
            0 25px 50px rgba(102,126,234,0.2),
            0 0 0 3px rgba(102,126,234,0.4) inset,
            0 0 80px rgba(102,126,234,0.2);
        border-color: rgba(102,126,234,0.6);
        z-index: 100;
    }
    
    /* Shine effect on hover */
    .leader-card::after {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(
            45deg,
            transparent 30%,
            rgba(255,255,255,0.8) 50%,
            transparent 70%
        );
        transform: rotate(45deg) translateX(-100%);
        transition: transform 0.8s;
    }
    
    .leader-card:hover::after {
        transform: rotate(45deg) translateX(100%);
    }
    
    /* Profile image with extreme 3D lift */
    .profile-wrapper {
        padding: 35px;
        display: flex;
        justify-content: center;
        position: relative;
    }
    
    .profile-image-container {
        width: 220px;
        height: 220px;
        border-radius: 50%;
        position: relative;
        transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
        transform-style: preserve-3d;
    }
    
    .leader-card:hover .profile-image-container {
        transform: translateZ(60px) scale(1.15) rotateZ(-5deg);
    }
    
    .profile-image-container img {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        object-fit: cover;
        border: 6px solid white;
        box-shadow: 
            0 20px 50px rgba(0,0,0,0.15),
            0 0 0 12px rgba(102,126,234,0.1),
            0 0 60px rgba(102,126,234,0.2) inset;
        transition: all 0.6s ease;
    }
    
    .leader-card:hover .profile-image-container img {
        box-shadow: 
            0 35px 80px rgba(0,0,0,0.25),
            0 0 0 16px rgba(102,126,234,0.3),
            0 0 100px rgba(102,126,234,0.4) inset;
        border-width: 8px;
    }
    
    /* Animated emoji badge */
    .emoji-badge {
        position: absolute;
        top: 25px;
        right: 25px;
        width: 75px;
        height: 75px;
        background: linear-gradient(135deg, rgba(255,255,255,0.98), rgba(255,255,255,0.9));
        backdrop-filter: blur(15px);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 40px;
        box-shadow: 0 12px 35px rgba(0,0,0,0.15);
        z-index: 20;
        border: 4px solid rgba(102,126,234,0.2);
        animation: floatEmoji 5s ease-in-out infinite;
        transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    @keyframes floatEmoji {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        25% { transform: translateY(-12px) rotate(-8deg); }
        75% { transform: translateY(-12px) rotate(8deg); }
    }
    
    .leader-card:hover .emoji-badge {
        transform: translateZ(80px) scale(1.4) rotate(360deg);
        box-shadow: 0 20px 50px rgba(102,126,234,0.4);
        border-color: rgba(102,126,234,0.5);
    }
    
    /* Card content */
    .card-content {
        padding: 0 35px 35px 35px;
        text-align: center;
        position: relative;
        z-index: 10;
        transition: all 0.4s ease;
    }
    
    .leader-card:hover .card-content {
        transform: translateZ(40px);
    }
    
    .card-content h3 {
        color: #2D3748;
        font-size: 26px;
        font-weight: 900;
        margin-bottom: 10px;
        font-family: 'Montserrat', sans-serif;
        letter-spacing: 0.5px;
    }
    
    .card-content .title {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 16px;
        font-weight: 700;
        margin-bottom: 14px;
        letter-spacing: 0.5px;
    }
    
    .card-content .description {
        color: #4A5568;
        font-size: 13.5px;
        line-height: 1.7;
        margin-bottom: 20px;
        font-weight: 500;
    }
    
    /* Glowing expertise tags */
    .expertise-tag {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 25px;
        font-size: 11.5px;
        margin: 5px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        box-shadow: 0 6px 20px rgba(102,126,234,0.3);
    }
    
    .expertise-tag:hover {
        transform: translateY(-5px) scale(1.15);
        box-shadow: 0 12px 35px rgba(102,126,234,0.5);
        background: linear-gradient(135deg, #764ba2 0%, #f093fb 100%);
    }
    
    /* Premium buttons */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 18px 45px;
        font-weight: 800;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        box-shadow: 0 12px 35px rgba(102,126,234,0.35);
        text-transform: uppercase;
        letter-spacing: 2px;
        font-family: 'Montserrat', sans-serif;
        font-size: 15px;
        border: 2px solid transparent;
    }
    
    .stButton>button:hover {
        transform: translateY(-6px) scale(1.08);
        box-shadow: 0 18px 50px rgba(102,126,234,0.5);
        background: linear-gradient(135deg, #764ba2 0%, #f093fb 100%);
        border-color: rgba(255,255,255,0.5);
    }
    
    /* Chat interface */
    .chat-header {
        background: linear-gradient(135deg, rgba(255,255,255,0.98), rgba(255,255,255,0.92));
        backdrop-filter: blur(30px);
        padding: 40px;
        border-radius: 35px;
        margin-bottom: 35px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.1);
        border: 2px solid rgba(102,126,234,0.2);
        animation: zoomIn 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    @keyframes zoomIn {
        from { opacity: 0; transform: scale(0.5) rotate(-5deg); }
        to { opacity: 1; transform: scale(1) rotate(0deg); }
    }
    
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px 28px;
        border-radius: 28px 28px 8px 28px;
        margin: 16px 0;
        margin-left: auto;
        max-width: 70%;
        box-shadow: 0 10px 30px rgba(102,126,234,0.35);
        animation: slideInRight 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
        font-weight: 500;
        line-height: 1.6;
    }
    
    .assistant-message {
        background: linear-gradient(135deg, rgba(255,255,255,0.98), rgba(255,255,255,0.92));
        backdrop-filter: blur(20px);
        color: #2D3748;
        padding: 20px 28px;
        border-radius: 28px 28px 28px 8px;
        margin: 16px 0;
        max-width: 70%;
        border: 2px solid rgba(102,126,234,0.2);
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        animation: slideInLeft 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
        font-weight: 500;
        line-height: 1.7;
    }
    
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(60px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-60px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .stTextInput>div>div>input {
        background: rgba(255,255,255,0.95);
        backdrop-filter: blur(20px);
        border: 2px solid rgba(102,126,234,0.25);
        border-radius: 30px;
        color: #2D3748;
        padding: 18px 28px;
        font-size: 16px;
        transition: all 0.3s ease;
        font-weight: 500;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #667eea;
        box-shadow: 0 0 40px rgba(102,126,234,0.25);
        transform: translateY(-3px);
    }
    
    .section-title {
        color: #2D3748;
        font-size: 2.8rem;
        font-weight: 900;
        text-align: center;
        margin: 60px 0 45px 0;
        font-family: 'Montserrat', sans-serif;
        letter-spacing: 3px;
        text-transform: uppercase;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        filter: drop-shadow(0 6px 12px rgba(102,126,234,0.2));
        animation: titlePulse 3s ease-in-out infinite;
    }
    
    @keyframes titlePulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.03); }
    }
</style>
""", unsafe_allow_html=True)

# Session State
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

if "carousel_page" not in st.session_state:
    st.session_state.carousel_page = 0

# Main Page
if st.session_state.selected_leader is None:
    st.markdown('<h1 class="main-title">FINANCE LEADERS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Visionaries Who Changed the World</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="greeting-box">
        <p style="color: #2D3748; font-size: 1.4rem; font-weight: 700; margin: 0; font-family: 'Montserrat', sans-serif; letter-spacing: 1.5px;">
            👋 Hello, ready to chat with these inspiring leaders?
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="section-title">RECOMMENDED FOR YOU</h2>', unsafe_allow_html=True)
    
    topic_cols = st.columns(5)
    topics = ["Finance Careers", "Personal Finance", "Startups", "Social Impact", "Tech Finance"]
    
    for idx, topic in enumerate(topics):
        with topic_cols[idx]:
            if st.button(topic, key=f"topic_{idx}", width='stretch'):
                st.session_state.selected_topic = topic
                st.rerun()
    
    st.markdown('<h2 class="section-title">ALL LEADERS</h2>', unsafe_allow_html=True)
    
    # Carousel navigation
    nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
    with nav_col1:
        if st.button("← Previous", key="prev", width='stretch'):
            if st.session_state.carousel_page > 0:
                st.session_state.carousel_page -= 1
                st.rerun()
    
    with nav_col3:
        if st.button("Next →", key="next", width='stretch'):
            if st.session_state.carousel_page < 1:
                st.session_state.carousel_page += 1
                st.rerun()
    
    # Display leaders
    leader_names = list(leaders.keys())
    start_idx = st.session_state.carousel_page * 5
    end_idx = start_idx + 5
    
    cols = st.columns(5, gap="large")
    
    for idx, col in enumerate(cols):
        leader_idx = start_idx + idx
        if leader_idx < len(leader_names):
            leader_name = leader_names[leader_idx]
            leader = leaders[leader_name]
            
            with col:
                st.markdown(f'<div class="leader-card" style="animation-delay: {idx * 0.12}s;">', unsafe_allow_html=True)
                st.markdown(f'<div class="emoji-badge">{leader["emoji"]}</div>', unsafe_allow_html=True)
                
                st.markdown('<div class="profile-wrapper">', unsafe_allow_html=True)
                st.markdown('<div class="profile-image-container">', unsafe_allow_html=True)
                
                if os.path.exists(leader['image']):
                    st.image(leader['image'], width=220)
                else:
                    st.markdown(f"""
                    <div style="width: 220px; height: 220px; background: {leader['gradient']}; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 90px; border: 6px solid white; box-shadow: 0 20px 50px rgba(0,0,0,0.15);">
                        {leader['emoji']}
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class="card-content">
                    <h3>{leader_name}</h3>
                    <p class="title">{leader['title']}</p>
                    <p class="description">{leader['description']}</p>
                    <div style="margin-bottom: 22px;">
                        {''.join([f'<span class="expertise-tag">{skill}</span>' for skill in leader['expertise'][:2]])}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                if st.button("Start Chat", key=f"btn_{leader_idx}", width='stretch'):
                    st.session_state.selected_leader = leader_name
                    st.rerun()
    
    st.markdown("<br><br>", unsafe_allow_html=True)

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
            <div style="display: flex; align-items: center; gap: 35px;">
                <div style="width: 95px; height: 95px; background: {leader['gradient']}; border-radius: 30px; display: flex; align-items: center; justify-content: center; font-size: 52px; border: 4px solid rgba(102,126,234,0.3); box-shadow: 0 15px 40px rgba(0,0,0,0.15); animation: float 3s ease-in-out infinite;">
                    {leader['emoji']}
                </div>
                <div>
                    <h2 style="color: #2D3748; margin: 0; font-size: 42px; font-weight: 900; font-family: 'Montserrat', sans-serif; letter-spacing: 0.5px;">{leader_name}</h2>
                    <p style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 12px 0; font-size: 20px; font-weight: 700; letter-spacing: 0.5px;">{leader['title']}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.messages[leader_name][1:]:
            if msg["role"] == "user":
                st.markdown(f'<div style="display: flex; justify-content: flex-end;"><div class="user-message">{msg["content"]}</div></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="assistant-message">{msg["content"]}</div>', unsafe_allow_html=True)
        
        if st.session_state.typing:
            st.markdown('<div class="assistant-message"><p style="margin: 0;">Thinking...</p></div>', unsafe_allow_html=True)
    
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

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 35px;">
        <div style="font-size: 85px; margin-bottom: 28px; animation: float 3s ease-in-out infinite;">💼</div>
        <h2 style="background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 900; font-size: 36px; letter-spacing: 2px; font-family: 'Montserrat', sans-serif;">FINANCE<br>LEADERS</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(255,255,255,0.85)); backdrop-filter: blur(20px); padding: 28px; border-radius: 25px; border: 2px solid rgba(102,126,234,0.2); margin-bottom: 28px; box-shadow: 0 8px 30px rgba(0,0,0,0.1);">
        <h3 style="color: #2D3748; font-weight: 800; margin-bottom: 20px; font-size: 24px; font-family: 'Montserrat', sans-serif;">About</h3>
        <p style="color: #4A5568; line-height: 1.9; font-weight: 500; font-size: 14.5px;">
            Connect with 10 inspiring women leaders and learn from their unique perspectives on finance, business, and leadership through AI-powered conversations.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(255,255,255,0.85)); backdrop-filter: blur(20px); padding: 28px; border-radius: 25px; border: 2px solid rgba(102,126,234,0.2); box-shadow: 0 8px 30px rgba(0,0,0,0.1);">
        <h3 style="color: #2D3748; font-weight: 800; margin-bottom: 20px; font-size: 24px; font-family: 'Montserrat', sans-serif;">Features</h3>
        <ul style="color: #4A5568; line-height: 2.4; font-weight: 500; font-size: 14.5px; padding-left: 22px;">
            <li>Personalized financial advice</li>
            <li>Expert insights from diverse fields</li>
            <li>Real-time AI conversations</li>
            <li>Empowering guidance</li>
            <li>Interactive 3D cards</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; padding: 25px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 25px; border: 2px solid rgba(255,255,255,0.3); box-shadow: 0 10px 35px rgba(102,126,234,0.4);">
        <p style="color: white; font-weight: 800; margin: 0; font-size: 17px; letter-spacing: 1.5px; font-family: 'Montserrat', sans-serif;">
            POWERED BY OPENAI GPT-3.5
        </p>
    </div>
    """, unsafe_allow_html=True)
