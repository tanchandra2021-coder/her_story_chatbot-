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
# 👩‍💼 Finance Leaders Dictionary with Pastel Gradients
# -------------------
leaders = {
    "Michelle Obama": {
        "title": "Education & Social Impact",
        "description": "Learn about financial literacy through education reform and community investment strategies",
        "style": "inspiring and empowering",
        "expertise": ["Impact Investing", "Education Finance", "Nonprofit Strategy"],
        "image": "michelle_obama.png",
        "gradient": "linear-gradient(135deg, #FFD3E1 0%, #C9A0DC 100%)",
        "emoji": "🌸"
    },
    "Angela Merkel": {
        "title": "Economic Policy Expert",
        "description": "Analytical approach to fiscal policy, European economics, and strategic financial planning",
        "style": "analytical and methodical",
        "expertise": ["Fiscal Policy", "European Markets", "Economic Strategy"],
        "image": "Angela_Merkel.png",
        "gradient": "linear-gradient(135deg, #FFE5E5 0%, #D4B5FF 100%)",
        "emoji": "📊"
    },
    "Malala Yousafzai": {
        "title": "Social Finance Advocate",
        "description": "Passionate insights on funding education, microfinance, and investing in social change",
        "style": "passionate and principled",
        "expertise": ["Microfinance", "Social Bonds", "Education Funding"],
        "image": "Malala_Yousafazi.png",
        "gradient": "linear-gradient(135deg, #B8E8FC 0%, #D4F1F4 100%)",
        "emoji": "💙"
    },
    "Ruth Bader Ginsburg": {
        "title": "Financial Law & Ethics",
        "description": "Precise guidance on financial regulations, investment law, and ethical wealth management",
        "style": "precise and principled",
        "expertise": ["Financial Law", "Securities", "Compliance"],
        "image": "Ruth_Bader_Ginsburg.png",
        "gradient": "linear-gradient(135deg, #D4F4DD 0%, #BFECFF 100%)",
        "emoji": "⚖️"
    },
    "Indra Nooyi": {
        "title": "Corporate Finance Leader",
        "description": "Strategic insights on corporate finance, M&A, sustainable business growth, and CFO excellence",
        "style": "strategic and visionary",
        "expertise": ["Corporate Finance", "M&A", "Business Strategy"],
        "image": "Indra_Nooyi.png",
        "gradient": "linear-gradient(135deg, #FFE8D1 0%, #FFD1DC 100%)",
        "emoji": "💼"
    },
    "Sheryl Sandberg": {
        "title": "Tech Finance Executive",
        "description": "Data-driven approach to tech valuations, scaling startups, and financial operations",
        "style": "analytical and motivational",
        "expertise": ["Tech Finance", "Scaling", "Operations"],
        "image": "Sheryl_Sandberg.png",
        "gradient": "linear-gradient(135deg, #E0BBE4 0%, #D4F1F9 100%)",
        "emoji": "💻"
    },
    "Jacinda Ardern": {
        "title": "Wellbeing Economics",
        "description": "Compassionate approach to budget management, public finance, and wellbeing economics",
        "style": "empathetic and pragmatic",
        "expertise": ["Public Finance", "Budget Policy", "Wellbeing Economy"],
        "image": "Jacinda_Ardern.png",
        "gradient": "linear-gradient(135deg, #FFE5F1 0%, #D4EFDF 100%)",
        "emoji": "🌿"
    },
    "Mae Jemison": {
        "title": "STEM Finance Pioneer",
        "description": "Innovative thinking on R&D funding, STEM investment, and technology venture capital",
        "style": "innovative and scientific",
        "expertise": ["Venture Capital", "R&D Finance", "Tech Investment"],
        "image": "Mae_Jemison.png",
        "gradient": "linear-gradient(135deg, #FFD6E8 0%, #E8D4F2 100%)",
        "emoji": "🚀"
    },
    "Reshma Saujani": {
        "title": "Startup Finance Advocate",
        "description": "Bold approach to fundraising, startup equity, and building financial resilience in tech",
        "style": "bold and resourceful",
        "expertise": ["Fundraising", "Startup Equity", "Angel Investing"],
        "image": "Reshman_Saujani.png",
        "gradient": "linear-gradient(135deg, #FFF0E5 0%, #E5E5FF 100%)",
        "emoji": "🎯"
    },
    "Sara Blakely": {
        "title": "Bootstrap Finance Expert",
        "description": "Self-made approach to bootstrapping businesses, cash flow management, and building wealth",
        "style": "creative and determined",
        "expertise": ["Bootstrapping", "Cash Flow", "Wealth Building"],
        "image": "Sara_Blakely.png",
        "gradient": "linear-gradient(135deg, #FFEEF8 0%, #FFEAA7 100%)",
        "emoji": "✨"
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
# 💅 Custom CSS Styling with Enhanced Animations & Pastel Design
# -------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Poppins:wght@300;400;500;600;700;800&display=swap');
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    * {
        font-family: 'Plus Jakarta Sans', 'Poppins', sans-serif;
    }
    
    /* Animated pastel gradient background */
    .stApp {
        background: linear-gradient(-45deg, #FFE5F1, #E8F5E9, #E3F2FD, #FFF3E0, #F3E5F5, #E0F2F7);
        background-size: 400% 400%;
        animation: gradientFlow 25s ease infinite;
    }
    
    @keyframes gradientFlow {
        0% { background-position: 0% 50%; }
        25% { background-position: 100% 50%; }
        50% { background-position: 100% 100%; }
        75% { background-position: 0% 100%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Smooth fade in animation */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(40px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    @keyframes shimmer {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }
    
    /* Enhanced card styling with pastel theme */
    .leader-card {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(20px);
        border-radius: 28px;
        border: 2px solid rgba(255, 255, 255, 0.5);
        overflow: hidden;
        transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
        cursor: pointer;
        height: 100%;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
        animation: fadeInUp 0.8s ease-out backwards;
        position: relative;
    }
    
    .leader-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
        transition: left 0.5s;
    }
    
    .leader-card:hover::before {
        left: 100%;
    }
    
    .leader-card:hover {
        transform: translateY(-16px) scale(1.02);
        box-shadow: 0 24px 48px rgba(0, 0, 0, 0.15);
        border-color: rgba(255, 255, 255, 0.8);
    }
    
    .leader-image-container {
        width: 100%;
        height: 240px;
        overflow: hidden;
        position: relative;
    }
    
    .leader-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.7s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    .leader-card:hover .leader-image {
        transform: scale(1.12) rotate(2deg);
    }
    
    /* Gradient overlay with animation */
    .gradient-overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        opacity: 0;
        transition: opacity 0.5s ease;
    }
    
    .leader-card:hover .gradient-overlay {
        opacity: 0.25;
    }
    
    /* Emoji badge */
    .emoji-badge {
        position: absolute;
        top: 16px;
        right: 16px;
        width: 56px;
        height: 56px;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        z-index: 10;
        animation: float 3s ease-in-out infinite;
        border: 3px solid rgba(255, 255, 255, 0.6);
        transition: all 0.4s ease;
    }
    
    .leader-card:hover .emoji-badge {
        transform: scale(1.15) rotate(10deg);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
    }
    
    /* Chat message animations */
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(40px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-40px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .user-message {
        background: linear-gradient(135deg, #C9A0DC 0%, #B19CD9 100%);
        color: white;
        padding: 18px 24px;
        border-radius: 24px 24px 6px 24px;
        margin: 14px 0;
        margin-left: auto;
        max-width: 70%;
        box-shadow: 0 6px 24px rgba(201, 160, 220, 0.35);
        animation: slideInRight 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
        font-weight: 500;
        line-height: 1.6;
    }
    
    .assistant-message {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(248, 250, 252, 0.98));
        backdrop-filter: blur(20px);
        color: #2C3E50;
        padding: 18px 24px;
        border-radius: 24px 24px 24px 6px;
        margin: 14px 0;
        max-width: 70%;
        border: 2px solid rgba(255, 255, 255, 0.6);
        box-shadow: 0 6px 24px rgba(0, 0, 0, 0.1);
        animation: slideInLeft 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
        font-weight: 500;
        line-height: 1.7;
    }
    
    /* Enhanced title styling */
    .main-title {
        text-align: center;
        font-size: 5.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #C9A0DC 0%, #B8E8FC 30%, #D4F4DD 60%, #FFD6E8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 24px;
        letter-spacing: -3px;
        animation: fadeInUp 1s ease-out, shimmer 3s infinite;
        background-size: 200% auto;
        font-family: 'Poppins', sans-serif;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.05);
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.6rem;
        background: linear-gradient(135deg, #B19CD9 0%, #7FA9E5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 16px;
        font-weight: 700;
        animation: fadeInUp 1.2s ease-out;
        letter-spacing: -0.5px;
    }
    
    /* Enhanced button styling */
    .stButton>button {
        background: linear-gradient(135deg, #C9A0DC 0%, #B19CD9 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 14px 32px;
        font-weight: 700;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        box-shadow: 0 6px 24px rgba(201, 160, 220, 0.35);
        font-size: 15px;
        text-transform: uppercase;
        letter-spacing: 1px;
        border: 2px solid rgba(255, 255, 255, 0.3);
    }
    
    .stButton>button:hover {
        transform: translateY(-4px) scale(1.05);
        box-shadow: 0 12px 36px rgba(201, 160, 220, 0.5);
        background: linear-gradient(135deg, #D4B5FF 0%, #C9A0DC 100%);
    }
    
    .stButton>button:active {
        transform: translateY(-2px) scale(1.02);
    }
    
    /* Enhanced input styling */
    .stTextInput>div>div>input {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(20px);
        border: 2px solid rgba(201, 160, 220, 0.3);
        border-radius: 20px;
        color: #2C3E50;
        padding: 16px 24px;
        font-size: 16px;
        transition: all 0.4s ease;
        font-weight: 600;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #C9A0DC;
        box-shadow: 0 0 0 4px rgba(201, 160, 220, 0.15);
        transform: translateY(-2px);
    }
    
    .stTextInput>div>div>input::placeholder {
        color: #A0AEC0;
        font-weight: 500;
    }
    
    /* Enhanced expertise tags */
    .expertise-tag {
        display: inline-block;
        background: linear-gradient(135deg, rgba(201, 160, 220, 0.15), rgba(184, 232, 252, 0.15));
        padding: 8px 16px;
        border-radius: 24px;
        font-size: 12px;
        color: #7B68A8;
        margin: 5px 4px;
        border: 2px solid rgba(201, 160, 220, 0.3);
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    .expertise-tag:hover {
        transform: scale(1.1) translateY(-2px);
        border-color: rgba(201, 160, 220, 0.6);
        box-shadow: 0 4px 16px rgba(201, 160, 220, 0.3);
        background: linear-gradient(135deg, rgba(201, 160, 220, 0.25), rgba(184, 232, 252, 0.25));
    }
    
    /* Enhanced header styling */
    .chat-header {
        background: linear-gradient(135deg, #C9A0DC 0%, #B8E8FC 100%);
        padding: 32px;
        border-radius: 28px;
        margin-bottom: 28px;
        box-shadow: 0 12px 40px rgba(201, 160, 220, 0.4);
        animation: fadeInUp 0.6s ease-out;
        border: 3px solid rgba(255, 255, 255, 0.4);
    }
    
    /* Card content padding */
    .card-content {
        padding: 24px;
    }
    
    /* Enhanced typing indicator */
    .typing-indicator {
        display: flex;
        gap: 8px;
        padding: 14px;
    }
    
    .typing-dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: linear-gradient(135deg, #C9A0DC 0%, #B8E8FC 100%);
        animation: typingPulse 1.4s infinite ease-in-out;
        box-shadow: 0 2px 8px rgba(201, 160, 220, 0.4);
    }
    
    .typing-dot:nth-child(2) {
        animation-delay: 0.2s;
    }
    
    .typing-dot:nth-child(3) {
        animation-delay: 0.4s;
    }
    
    @keyframes typingPulse {
        0%, 80%, 100% {
            opacity: 0.3;
            transform: scale(0.8);
        }
        40% {
            opacity: 1;
            transform: scale(1.2);
        }
    }
    
    /* Smooth hover transitions */
    a, button, input, .leader-card, .expertise-tag {
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    /* Decorative elements */
    .decorative-circle {
        position: fixed;
        border-radius: 50%;
        opacity: 0.1;
        pointer-events: none;
        animation: float 6s ease-in-out infinite;
    }
    
    /* Card number badge */
    .card-number {
        position: absolute;
        top: 16px;
        left: 16px;
        width: 36px;
        height: 36px;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
        font-weight: 800;
        color: #7B68A8;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
        z-index: 10;
        border: 2px solid rgba(201, 160, 220, 0.3);
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

# -------------------
# 🏠 Leader Selection Page
# -------------------
if st.session_state.selected_leader is None:
    # Hero Section
    st.markdown('<h1 class="main-title">Finance Leaders</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Learn from Visionaries Who Changed the World</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #7B68A8; margin-bottom: 60px; font-size: 1.2rem; font-weight: 600; letter-spacing: 0.5px;">Select a leader to explore their financial expertise and insights</p>', unsafe_allow_html=True)
    
    # First Row - 5 Leaders
    cols1 = st.columns(5, gap="large")
    leader_names = list(leaders.keys())
    
    for idx, col in enumerate(cols1):
        if idx < len(leader_names):
            leader_name = leader_names[idx]
            leader = leaders[leader_name]
            
            with col:
                # Card container
                st.markdown(f'<div class="leader-card" style="animation-delay: {idx * 0.15}s;">', unsafe_allow_html=True)
                
                # Card number badge
                st.markdown(f'<div class="card-number">{idx + 1}</div>', unsafe_allow_html=True)
                
                # Image container with gradient overlay
                st.markdown('<div class="leader-image-container">', unsafe_allow_html=True)
                
                # Emoji badge
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
                
                # Gradient overlay
                st.markdown(f'<div class="gradient-overlay" style="background: {leader["gradient"]};"></div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Card content
                st.markdown(f"""
                <div class="card-content">
                    <h3 style="color: #2D3748; font-size: 20px; font-weight: 800; margin-bottom: 10px; letter-spacing: -0.5px;">
                        {leader_name}
                    </h3>
                    <p style="color: #7B68A8; font-size: 14px; margin-bottom: 14px; font-weight: 700;">{leader['title']}</p>
                    <p style="color: #4A5568; font-size: 13px; line-height: 1.7; margin-bottom: 18px; font-weight: 500;">{leader['description']}</p>
                    <div style="margin-bottom: 18px;">
                        {''.join([f'<span class="expertise-tag">{skill}</span>' for skill in leader['expertise'][:2]])}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                if st.button(f"Start Chat", key=f"btn_{idx}", use_container_width=True):
                    st.session_state.selected_leader = leader_name
                    st.rerun()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Second Row - 5 Leaders
    cols2 = st.columns(5, gap="large")
    
    for idx, col in enumerate(cols2):
        actual_idx = idx + 5
        if actual_idx < len(leader_names):
            leader_name = leader_names[actual_idx]
            leader = leaders[leader_name]
            
            with col:
                # Card container
                st.markdown(f'<div class="leader-card" style="animation-delay: {(idx + 5) * 0.15}s;">', unsafe_allow_html=True)
                
                # Card number badge
                st.markdown(f'<div class="card-number">{actual_idx + 1}</div>', unsafe_allow_html=True)
                
                # Image container with gradient overlay
                st.markdown('<div class="leader-image-container">', unsafe_allow_html=True)
                
                # Emoji badge
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
                
                # Gradient overlay
                st.markdown(f'<div class="gradient-overlay" style="background: {leader["gradient"]};"></div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Card content
                st.markdown(f"""
                <div class="card-content">
                    <h3 style="color: #2D3748; font-size: 20px; font-weight: 800; margin-bottom: 10px; letter-spacing: -0.5px;">
                        {leader_name}
                    </h3>
                    <p style="color: #7B68A8; font-size: 14px; margin-bottom: 14px; font-weight: 700;">{leader['title']}</p>
                    <p style="color: #4A5568; font-size: 13px; line-height: 1.7; margin-bottom: 18px; font-weight: 500;">{leader['description']}</p>
                    <div style="margin-bottom: 18px;">
                        {''.join([f'<span class="expertise-tag">{skill}</span>' for skill in leader['expertise'][:2]])}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                if st.button(f"Start Chat", key=f"btn_{actual_idx}", use_container_width=True):
                    st.session_state.selected_leader = leader_name
                    st.rerun()
    
    # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; padding: 50px;">
        <div style="display: inline-flex; align-items: center; gap: 20px; background: rgba(255, 255, 255, 0.98
