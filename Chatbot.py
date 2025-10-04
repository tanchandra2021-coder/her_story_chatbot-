import streamlit as st
import openai
from openai import OpenAI
import os
import time

# -------------------
# 🔑 OpenAI API Key
# -------------------
OPENAI_API_KEY = "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"
client = OpenAI(api_key=OPENAI_API_KEY)

# -------------------
# 👩‍💼 Finance Leaders Dictionary
# -------------------
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
        "fun_fact": "Did you know you can learn about personal finance with Michelle Obama?"
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
        "fun_fact": "Explore fiscal policy and European economics with Angela Merkel!"
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
        "fun_fact": "Discover microfinance and social investing with Malala!"
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
        "fun_fact": "Navigate financial regulations with Ruth Bader Ginsburg's wisdom!"
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
        "fun_fact": "Learn corporate finance excellence from Indra Nooyi!"
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
        "fun_fact": "Scale your startup with insights from Sheryl Sandberg!"
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
        "fun_fact": "Explore wellbeing economics with Jacinda Ardern!"
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
        "fun_fact": "Invest in the future with Mae Jemison's STEM insights!"
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
        "fun_fact": "Master fundraising strategies with Reshma Saujani!"
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
        "fun_fact": "Build your empire from scratch with Sara Blakely!"
    }
}

# -------------------
# 🎨 Page Configuration
# -------------------
st.set_page_config(
    page_title="Finance Leaders AI Chat",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------
# 💅 Futuristic CSS with Animations
# -------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Exo+2:wght@300;400;500;600;700;800&family=Rajdhani:wght@300;400;500;600;700&display=swap');
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    * {
        font-family: 'Exo 2', 'Rajdhani', sans-serif;
    }
    
    /* Futuristic animated background */
    .stApp {
        background: linear-gradient(-45deg, #0a0e27, #16213e, #0f3460, #1a1a2e);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        position: relative;
        overflow-x: hidden;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Parallax stars background */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(2px 2px at 20% 30%, white, transparent),
            radial-gradient(2px 2px at 60% 70%, white, transparent),
            radial-gradient(1px 1px at 50% 50%, white, transparent),
            radial-gradient(1px 1px at 80% 10%, white, transparent),
            radial-gradient(2px 2px at 90% 60%, white, transparent),
            radial-gradient(1px 1px at 33% 80%, white, transparent);
        background-size: 200% 200%;
        background-position: 0% 0%;
        animation: stars 60s linear infinite;
        opacity: 0.3;
        pointer-events: none;
        z-index: 0;
    }
    
    @keyframes stars {
        from { transform: translateY(0); }
        to { transform: translateY(-100px); }
    }
    
    /* Futuristic title */
    .main-title {
        text-align: center;
        font-size: 6rem;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 20px;
        letter-spacing: 8px;
        font-family: 'Orbitron', sans-serif;
        text-transform: uppercase;
        animation: titleGlow 3s ease-in-out infinite, fadeInDown 1s ease-out;
        text-shadow: 
            0 0 10px rgba(100, 200, 255, 0.8),
            0 0 20px rgba(100, 200, 255, 0.6),
            0 0 30px rgba(100, 200, 255, 0.4),
            0 0 40px rgba(100, 200, 255, 0.2);
        position: relative;
        z-index: 10;
    }
    
    @keyframes titleGlow {
        0%, 100% { 
            text-shadow: 
                0 0 10px rgba(100, 200, 255, 0.8),
                0 0 20px rgba(100, 200, 255, 0.6),
                0 0 30px rgba(100, 200, 255, 0.4);
        }
        50% { 
            text-shadow: 
                0 0 20px rgba(100, 200, 255, 1),
                0 0 30px rgba(100, 200, 255, 0.8),
                0 0 40px rgba(100, 200, 255, 0.6),
                0 0 50px rgba(100, 200, 255, 0.4);
        }
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-50px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.8rem;
        color: #64c8ff;
        margin-bottom: 15px;
        font-weight: 600;
        animation: fadeInUp 1.2s ease-out;
        letter-spacing: 3px;
        text-transform: uppercase;
        font-family: 'Rajdhani', sans-serif;
    }
    
    /* Personalized greeting */
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
    
    /* Floating notification */
    .floating-notification {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background: linear-gradient(135deg, rgba(100, 200, 255, 0.95), rgba(150, 150, 255, 0.95));
        backdrop-filter: blur(20px);
        padding: 20px 30px;
        border-radius: 20px;
        border: 2px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        z-index: 1000;
        animation: slideInRight 0.5s ease-out, float 3s ease-in-out infinite;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .floating-notification:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 15px 50px rgba(100, 200, 255, 0.6);
    }
    
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(100px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* Leader card with zoom animation */
    .leader-card {
        background: rgba(20, 30, 60, 0.8);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 2px solid rgba(100, 200, 255, 0.3);
        overflow: hidden;
        transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        cursor: pointer;
        height: 100%;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        position: relative;
        animation: fadeInUp 0.8s ease-out backwards;
    }
    
    .leader-card::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, #64c8ff, #9696ff, #64c8ff);
        border-radius: 20px;
        opacity: 0;
        transition: opacity 0.5s;
        z-index: -1;
        animation: borderRotate 3s linear infinite;
    }
    
    @keyframes borderRotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .leader-card:hover::before {
        opacity: 1;
    }
    
    .leader-card:hover {
        transform: translateY(-15px) scale(1.05);
        box-shadow: 0 20px 60px rgba(100, 200, 255, 0.4);
        border-color: rgba(100, 200, 255, 0.8);
    }
    
    /* Rotating portrait effect */
    .leader-image-container {
        width: 100%;
        height: 240px;
        overflow: hidden;
        position: relative;
        perspective: 1000px;
    }
    
    .leader-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        transform-style: preserve-3d;
    }
    
    .leader-card:hover .leader-image {
        transform: scale(1.2) rotateY(5deg) rotateX(5deg);
    }
    
    /* Sparkle effect */
    .sparkle {
        position: absolute;
        width: 4px;
        height: 4px;
        background: white;
        border-radius: 50%;
        animation: sparkleFloat 3s ease-in-out infinite;
        opacity: 0;
    }
    
    @keyframes sparkleFloat {
        0%, 100% { opacity: 0; transform: translateY(0) scale(0); }
        50% { opacity: 1; transform: translateY(-30px) scale(1); }
    }
    
    /* Emoji with rotation */
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
        box-shadow: 0 5px 25px rgba(0, 0, 0, 0.3);
        z-index: 10;
        border: 2px solid rgba(100, 200, 255, 0.4);
        transition: all 0.5s ease;
        animation: rotateEmoji 10s linear infinite;
    }
    
    @keyframes rotateEmoji {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .leader-card:hover .emoji-badge {
        transform: scale(1.3) rotate(360deg);
        box-shadow: 0 10px 40px rgba(100, 200, 255, 0.6);
    }
    
    /* Card content */
    .card-content {
        padding: 25px;
        position: relative;
        z-index: 5;
    }
    
    .card-content h3 {
        color: #ffffff;
        font-size: 22px;
        font-weight: 800;
        margin-bottom: 10px;
        letter-spacing: 1px;
        font-family: 'Orbitron', sans-serif;
    }
    
    .card-content p {
        color: #64c8ff;
        font-size: 14px;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    
    /* Expertise tags */
    .expertise-tag {
        display: inline-block;
        background: rgba(100, 200, 255, 0.2);
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 11px;
        color: #64c8ff;
        margin: 4px;
        border: 1px solid rgba(100, 200, 255, 0.5);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }
    
    .expertise-tag:hover {
        background: rgba(100, 200, 255, 0.4);
        transform: scale(1.1);
        box-shadow: 0 5px 15px rgba(100, 200, 255, 0.4);
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #64c8ff 0%, #9696ff 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 14px 35px;
        font-weight: 700;
        transition: all 0.4s ease;
        box-shadow: 0 8px 25px rgba(100, 200, 255, 0.4);
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-family: 'Rajdhani', sans-serif;
        border: 2px solid rgba(255, 255, 255, 0.2);
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 12px 40px rgba(100, 200, 255, 0.6);
        background: linear-gradient(135deg, #9696ff 0%, #64c8ff 100%);
    }
    
    /* Floating action button */
    .fab {
        position: fixed;
        bottom: 40px;
        right: 40px;
        width: 70px;
        height: 70px;
        background: linear-gradient(135deg, #64c8ff, #9696ff);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 32px;
        box-shadow: 0 10px 40px rgba(100, 200, 255, 0.6);
        cursor: pointer;
        transition: all 0.4s ease;
        z-index: 1000;
        animation: float 3s ease-in-out infinite;
        border: 3px solid rgba(255, 255, 255, 0.3);
    }
    
    .fab:hover {
        transform: scale(1.2) rotate(90deg);
        box-shadow: 0 15px 50px rgba(100, 200, 255, 0.8);
    }
    
    /* Topic suggestions */
    .topic-card {
        background: rgba(100, 200, 255, 0.1);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(100, 200, 255, 0.3);
        padding: 15px 25px;
        border-radius: 15px;
        margin: 10px;
        display: inline-block;
        cursor: pointer;
        transition: all 0.3s ease;
        color: #64c8ff;
        font-weight: 600;
    }
    
    .topic-card:hover {
        background: rgba(100, 200, 255, 0.3);
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(100, 200, 255, 0.4);
    }
    
    /* Chat interface */
    .chat-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        padding: 35px;
        border-radius: 25px;
        margin-bottom: 30px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        border: 2px solid rgba(100, 200, 255, 0.3);
        animation: fadeInDown 0.6s ease-out;
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
        font-weight: 500;
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
        font-weight: 500;
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Input styling */
    .stTextInput>div>div>input {
        background: rgba(30, 40, 70, 0.8);
        backdrop-filter: blur(20px);
        border: 2px solid rgba(100, 200, 255, 0.3);
        border-radius: 25px;
        color: #ffffff;
        padding: 16px 25px;
        font-size: 16px;
        transition: all 0.3s ease;
        font-weight: 500;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #64c8ff;
        box-shadow: 0 0 20px rgba(100, 200, 255, 0.5);
    }
    
    .stTextInput>div>div>input::placeholder {
        color: #64c8ff;
        opacity: 0.7;
    }
    
    /* Typing indicator */
    .typing-indicator {
        display: flex;
        gap: 8px;
        padding: 15px;
    }
    
    .typing-dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #64c8ff;
        animation: typingPulse 1.4s infinite ease-in-out;
        box-shadow: 0 0 10px rgba(100, 200, 255, 0.6);
    }
    
    .typing-dot:nth-child(2) { animation-delay: 0.2s; }
    .typing-dot:nth-child(3) { animation-delay: 0.4s; }
    
    @keyframes typingPulse {
        0%, 80%, 100% {
            opacity: 0.3;
            transform: scale(0.8);
        }
        40% {
            opacity: 1;
            transform: scale(1.3);
        }
    }
    
    /* Recommended section */
    .recommended-section {
        background: rgba(20, 30, 60, 0.6);
        backdrop-filter: blur(20px);
        padding: 40px;
        border-radius: 25px;
        margin: 50px 0;
        border: 2px solid rgba(100, 200, 255, 0.3);
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
    }
    
    .section-title {
        color: #ffffff;
        font-size: 2.5rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 30px;
        font-family: 'Orbitron', sans-serif;
        text-transform: uppercase;
        letter-spacing: 3px;
        text-shadow: 0 0 20px rgba(100, 200, 255, 0.6);
    }
</style>
""", unsafe_allow_html=True)

# -------------------
# 💬 Initialize Session State
# -------------------
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

if "show_notification" not in st.session_state:
    st.session_state.show_notification = True

# -------------------
# 🏠 Leader Selection Page
# -------------------
if st.session_state.selected_leader is None:
    # Hero Section with parallax effect
    st.markdown('<h1 class="main-title">FINANCE LEADERS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Visionaries Who Changed the World</p>', unsafe_allow_html=True)
    
    # Personalized greeting
    st.markdown("""
    <div class="greeting-box">
        <p style="color: #ffffff; font-size: 1.3rem; font-weight: 600; margin: 0; font-family: 'Rajdhani', sans-serif; letter-spacing: 2px;">
            👋 Hello, ready to chat with these inspiring leaders?
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Topic-based suggestions section
    st.markdown("""
    <div class="recommended-section">
        <h2 class="section-title">Recommended For You</h2>
        <div style="text-align: center; margin-bottom: 30px;">
            <p style="color: #64c8ff; font-size: 1.1rem; font-weight: 500;">Select a topic to find the perfect leader</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Topic selection
    topic_cols = st.columns(5)
    topics = ["Finance Careers", "Personal Finance", "Startups", "Social Impact", "Tech Finance"]
    
    for idx, topic in enumerate(topics):
        with topic_cols[idx]:
            if st.button(topic, key=f"topic_{idx}", use_container_width=True):
                st.session_state.selected_topic = topic
                st.rerun()
    
    # Show recommended leaders based on selected topic
    if st.session_state.selected_topic:
        st.markdown(f"""
        <div style="text-align: center; margin: 30px 0;">
            <p style="color: #ffffff; font-size: 1.2rem; font-weight: 600;">
                Top leaders for <span style="color: #64c8ff;">{st.session_state.selected_topic}</span>:
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Filter leaders by topic
        recommended = [name for name, info in leaders.items() if st.session_state.selected_topic in info['topics']]
        
        rec_cols = st.columns(len(recommended) if len(recommended) <= 4 else 4)
        for idx, leader_name in enumerate(recommended[:4]):
            leader = leaders[leader_name]
            with rec_cols[idx]:
                st.markdown(f"""
                <div style="text-align: center; padding: 20px; background: rgba(100, 200, 255, 0.1); border-radius: 15px; border: 2px solid rgba(100, 200, 255, 0.3); cursor: pointer; transition: all 0.3s ease;" 
                     onmouseover="this.style.background='rgba(100, 200, 255, 0.2)'; this.style.transform='translateY(-5px)'"
                     onmouseout="this.style.background='rgba(100, 200, 255, 0.1)'; this.style.transform='translateY(0)'">
                    <div style="font-size: 48px; margin-bottom: 10px;">{leader['emoji']}</div>
                    <h4 style="color: #ffffff; font-weight: 700; margin-bottom: 5px;">{leader_name}</h4>
                    <p style="color: #64c8ff; font-size: 0.9rem;">{leader['title']}</p>
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Floating action button (FAB)
    st.markdown("""
    <div class="fab" title="Quick Actions">
        ⚡
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Dynamic leader carousel - First Row
    st.markdown("""
    <div style="margin: 60px 0 40px 0;">
        <h2 style="color: #ffffff; font-size: 2rem; font-weight: 800; text-align: center; margin-bottom: 40px; font-family: 'Orbitron', sans-serif; letter-spacing: 3px; text-shadow: 0 0 20px rgba(100, 200, 255, 0.6);">
            ALL LEADERS
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    cols1 = st.columns(5, gap="large")
    leader_names = list(leaders.keys())
    
    for idx, col in enumerate(cols1):
        if idx < len(leader_names):
            leader_name = leader_names[idx]
            leader = leaders[leader_name]
            
            with col:
                # Sparkle effects
                st.markdown(f"""
                <div class="sparkle" style="top: {20 + idx * 10}px; left: {30 + idx * 15}px; animation-delay: {idx * 0.3}s;"></div>
                <div class="sparkle" style="top: {40 + idx * 8}px; right: {25 + idx * 12}px; animation-delay: {idx * 0.4}s;"></div>
                """, unsafe_allow_html=True)
                
                # Card container with animation delay
                st.markdown(f'<div class="leader-card" style="animation-delay: {idx * 0.15}s;">', unsafe_allow_html=True)
                
                # Image container
                st.markdown('<div class="leader-image-container">', unsafe_allow_html=True)
                
                # Emoji badge with rotation
                st.markdown(f'<div class="emoji-badge">{leader["emoji"]}</div>', unsafe_allow_html=True)
                
                # Try to load image
                try:
                    if os.path.exists(leader['image']):
                        st.image(leader['image'], use_container_width=True)
                    else:
                        st.markdown(f"""
                        <div style="width: 100%; height: 240px; background: {leader['gradient']}; display: flex; align-items: center; justify-content: center; font-size: 90px;">
                            {leader['emoji']}
                        </div>
                        """, unsafe_allow_html=True)
                except:
                    st.markdown(f"""
                    <div style="width: 100%; height: 240px; background: {leader['gradient']}; display: flex; align-items: center; justify-content: center; font-size: 90px;">
                        {leader['emoji']}
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Card content
                st.markdown(f"""
                <div class="card-content">
                    <h3>{leader_name}</h3>
                    <p style="font-weight: 700; margin-bottom: 10px;">{leader['title']}</p>
                    <p style="font-size: 12px; opacity: 0.9; margin-bottom: 15px;">{leader['description']}</p>
                    <div style="margin-bottom: 18px;">
                        {''.join([f'<span class="expertise-tag">{skill}</span>' for skill in leader['expertise'][:2]])}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                if st.button("Start Chat", key=f"btn_{idx}", use_container_width=True):
                    st.session_state.selected_leader = leader_name
                    st.rerun()
                
                # Fun fact notification
                st.markdown(f"""
                <div style="margin-top: 10px; padding: 10px; background: rgba(100, 200, 255, 0.1); border-radius: 10px; border: 1px solid rgba(100, 200, 255, 0.3); font-size: 11px; color: #64c8ff; text-align: center;">
                    💡 {leader['fun_fact']}
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Second Row
    cols2 = st.columns(5, gap="large")
    
    for idx, col in enumerate(cols2):
        actual_idx = idx + 5
        if actual_idx < len(leader_names):
            leader_name = leader_names[actual_idx]
            leader = leaders[leader_name]
            
            with col:
                # Sparkle effects
                st.markdown(f"""
                <div class="sparkle" style="top: {25 + idx * 12}px; left: {35 + idx * 10}px; animation-delay: {idx * 0.35}s;"></div>
                <div class="sparkle" style="top: {45 + idx * 9}px; right: {30 + idx * 14}px; animation-delay: {idx * 0.45}s;"></div>
                """, unsafe_allow_html=True)
                
                st.markdown(f'<div class="leader-card" style="animation-delay: {(idx + 5) * 0.15}s;">', unsafe_allow_html=True)
                
                st.markdown('<div class="leader-image-container">', unsafe_allow_html=True)
                
                st.markdown(f'<div class="emoji-badge">{leader["emoji"]}</div>', unsafe_allow_html=True)
                
                try:
                    if os.path.exists(leader['image']):
                        st.image(leader['image'], use_container_width=True)
                    else:
                        st.markdown(f"""
                        <div style="width: 100%; height: 240px; background: {leader['gradient']}; display: flex; align-items: center; justify-content: center; font-size: 90px;">
                            {leader['emoji']}
                        </div>
                        """, unsafe_allow_html=True)
                except:
                    st.markdown(f"""
                    <div style="width: 100%; height: 240px; background: {leader['gradient']}; display: flex; align-items: center; justify-content: center; font-size: 90px;">
                        {leader['emoji']}
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class="card-content">
                    <h3>{leader_name}</h3>
                    <p style="font-weight: 700; margin-bottom: 10px;">{leader['title']}</p>
                    <p style="font-size: 12px; opacity: 0.9; margin-bottom: 15px;">{leader['description']}</p>
                    <div style="margin-bottom: 18px;">
                        {''.join([f'<span class="expertise-tag">{skill}</span>' for skill in leader['expertise'][:2]])}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                if st.button("Start Chat", key=f"btn_{actual_idx}", use_container_width=True):
                    st.session_state.selected_leader = leader_name
                    st.rerun()
                
                st.markdown(f"""
                <div style="margin-top: 10px; padding: 10px; background: rgba(100, 200, 255, 0.1); border-radius: 10px; border: 1px solid rgba(100, 200, 255, 0.3); font-size: 11px; color: #64c8ff; text-align: center;">
                    💡 {leader['fun_fact']}
                </div>
                """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; padding: 60px 20px;">
        <div style="display: inline-flex; align-items: center; gap: 20px; background: rgba(20, 30, 60, 0.8); backdrop-filter: blur(20px); padding: 25px 50px; border-radius: 50px; border: 2px solid rgba(100, 200, 255, 0.3); box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);">
            <span style="font-size: 32px; animation: float 3s ease-in-out infinite;">✨</span>
            <span style="color: #64c8ff; font-weight: 700; font-size: 1.1rem; letter-spacing: 1px;">Powered by Wisdom & Financial Excellence</span>
            <span style="font-size: 32px; animation: float 3s ease-in-out infinite; animation-delay: 1.5s;">💼</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------
# 💬 Chat Page with Zoom Animation
# -------------------
else:
    leader_name = st.session_state.selected_leader
    leader = leaders[leader_name]
    
    # Zoom in animation for selected leader
    st.markdown(f"""
    <style>
        @keyframes zoomIn {{
            from {{
                opacity: 0;
                transform: scale(0.3);
            }}
            to {{
                opacity: 1;
                transform: scale(1);
            }}
        }}
        
        .zoom-container {{
            animation: zoomIn 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        }}
    </style>
    """, unsafe_allow_html=True)
    
    # Chat Header with zoom effect
    col1, col2 = st.columns([1, 8])
    
    with col1:
        if st.button("← Back", key="back_button"):
            st.session_state.selected_leader = None
            st.session_state.selected_topic = None
            st.rerun()
    
    with col2:
        st.markdown(f"""
        <div class="chat-header zoom-container">
            <div style="display: flex; align-items: center; gap: 30px;">
                <div style="width: 100px; height: 100px; background: rgba(100, 200, 255, 0.2); backdrop-filter: blur(10px); border-radius: 25px; display: flex; align-items: center; justify-content: center; font-size: 55px; border: 3px solid rgba(100, 200, 255, 0.5); box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3); animation: float 3s ease-in-out infinite;">
                    {leader['emoji']}
                </div>
                <div>
                    <h2 style="color: #ffffff; margin: 0; font-size: 42px; font-weight: 900; letter-spacing: 2px; font-family: 'Orbitron', sans-serif; text-shadow: 0 0 20px rgba(100, 200, 255, 0.6);">{leader_name}</h2>
                    <p style="color: #64c8ff; margin: 10px 0; font-size: 20px; font-weight: 700; letter-spacing: 1px;">{leader['title']}</p>
                    <div style="margin-top: 15px;">
                        {''.join([f'<span style="background: rgba(100, 200, 255, 0.2); padding: 8px 20px; border-radius: 25px; font-size: 13px; color: #ffffff; margin-right: 10px; border: 2px solid rgba(100, 200, 255, 0.4); font-weight: 700; display: inline-block;">{skill}</span>' for skill in leader['expertise']])}
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Display Chat Messages
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.messages[leader_name][1:]:
            if msg["role"] == "user":
                st.markdown(f'<div style="display: flex; justify-content: flex-end;"><div class="user-message">{msg["content"]}</div></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="assistant-message">{msg["content"]}</div>', unsafe_allow_html=True)
        
        if st.session_state.typing:
            st.markdown("""
            <div class="assistant-message" style="padding: 12px 25px;">
                <div class="typing-indicator">
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Chat Input
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
        send_button = st.button("Send", use_container_width=True)
    
    # Process Message
    if send_button and user_input:
        st.session_state.messages[leader_name].append({"role": "user", "content": user_input})
        st.session_state.typing = True
        st.rerun()
    
    # Get AI response
    if st.session_state.typing:
        with st.spinner(f"{leader_name.split()[0]} is thinking..."):
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
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.session_state.typing = False
        
        st.rerun()

# -------------------
# 📊 Futuristic Sidebar
# -------------------
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 30px;">
        <div style="font-size: 80px; margin-bottom: 25px; animation: rotateEmoji 10s linear infinite;">💼</div>
        <h2 style="color: #64c8ff; font-weight: 900; font-size: 32px; letter-spacing: 3px; font-family: 'Orbitron', sans-serif; text-shadow: 0 0 15px rgba(100, 200, 255, 0.6);">FINANCE<br>LEADERS</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="background: rgba(20, 30, 60, 0.8); padding: 25px; border-radius: 20px; border: 2px solid rgba(100, 200, 255, 0.3); margin-bottom: 25px; box-shadow: 0 5px 25px rgba(0, 0, 0, 0.3);">
        <h3 style="color: #ffffff; font-weight: 800; margin-bottom: 18px; font-size: 22px; font-family: 'Orbitron', sans-serif;">About</h3>
        <p style="color: #64c8ff; line-height: 1.9; font-weight: 500; font-size: 14px;">
            Connect with 10 inspiring women leaders and learn from their unique perspectives on finance, business, and leadership through AI-powered conversations.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="background: rgba(20, 30, 60, 0.8); padding: 25px; border-radius: 20px; border: 2px solid rgba(100, 200, 255, 0.3); box-shadow: 0 5px 25px rgba(0, 0, 0, 0.3);">
        <h3 style="color: #ffffff; font-weight: 800; margin-bottom: 18px; font-size: 22px; font-family: 'Orbitron', sans-serif;">Features</h3>
        <ul style="color: #64c8ff; line-height: 2.3; font-weight: 500; font-size: 14px; padding-left: 20px;">
            <li>🎯 Personalized financial advice</li>
            <li>🌟 Expert insights from diverse fields</li>
            <li>⚡ Real-time AI conversations</li>
            <li>💡 Empowering guidance</li>
            <li>🚀 Futuristic experience</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; padding: 22px; background: linear-gradient(135deg, #64c8ff 0%, #9696ff 100%); border-radius: 20px; border: 2px solid rgba(255, 255, 255, 0.3); box-shadow: 0 8px 30px rgba(100, 200, 255, 0.4);">
        <p style="color: white; font-weight: 800; margin: 0; font-size: 16px; letter-spacing: 1px; font-family: 'Rajdhani', sans-serif;">
            ⚡ POWERED BY OPENAI GPT-3.5
        </p>
    </div>
    """, unsafe_allow_html=True)
