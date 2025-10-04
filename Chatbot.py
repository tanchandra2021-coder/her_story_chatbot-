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
        "color": "#FF6B9D",
        "emoji": "🌸"
    },
    "Angela Merkel": {
        "title": "Economic Policy Expert",
        "description": "Analytical approach to fiscal policy, European economics, and strategic financial planning",
        "style": "analytical and methodical",
        "expertise": ["Fiscal Policy", "European Markets", "Economic Strategy"],
        "image": "Angela_Merkel.png",
        "color": "#C084FC",
        "emoji": "💜"
    },
    "Malala Yousafzai": {
        "title": "Social Finance Advocate",
        "description": "Passionate insights on funding education, microfinance, and investing in social change",
        "style": "passionate and principled",
        "expertise": ["Microfinance", "Social Bonds", "Education Funding"],
        "image": "Malala_Yousafazi.png",
        "color": "#F472B6",
        "emoji": "🦋"
    },
    "Ruth Bader Ginsburg": {
        "title": "Financial Law & Ethics",
        "description": "Precise guidance on financial regulations, investment law, and ethical wealth management",
        "style": "precise and principled",
        "expertise": ["Financial Law", "Securities", "Compliance"],
        "image": "Ruth_Bader_Ginsburg.png",
        "color": "#FCA5A5",
        "emoji": "⚖️"
    },
    "Indra Nooyi": {
        "title": "Corporate Finance Leader",
        "description": "Strategic insights on corporate finance, M&A, sustainable business growth, and CFO excellence",
        "style": "strategic and visionary",
        "expertise": ["Corporate Finance", "M&A", "Business Strategy"],
        "image": "Indra_Nooyi.png",
        "color": "#A78BFA",
        "emoji": "✨"
    },
    "Sheryl Sandberg": {
        "title": "Tech Finance Executive",
        "description": "Data-driven approach to tech valuations, scaling startups, and financial operations",
        "style": "analytical and motivational",
        "expertise": ["Tech Finance", "Scaling", "Operations"],
        "image": "Sheryl_Sandberg.png",
        "color": "#F9A8D4",
        "emoji": "💎"
    },
    "Jacinda Ardern": {
        "title": "Wellbeing Economics",
        "description": "Compassionate approach to budget management, public finance, and wellbeing economics",
        "style": "empathetic and pragmatic",
        "expertise": ["Public Finance", "Budget Policy", "Wellbeing Economy"],
        "image": "Jacinda_Ardern.png",
        "color": "#FDA4AF",
        "emoji": "🌺"
    },
    "Mae Jemison": {
        "title": "STEM Finance Pioneer",
        "description": "Innovative thinking on R&D funding, STEM investment, and technology venture capital",
        "style": "innovative and scientific",
        "expertise": ["Venture Capital", "R&D Finance", "Tech Investment"],
        "image": "Mae_Jemison.png",
        "color": "#DDA0DD",
        "emoji": "🚀"
    },
    "Reshma Saujani": {
        "title": "Startup Finance Advocate",
        "description": "Bold approach to fundraising, startup equity, and building financial resilience in tech",
        "style": "bold and resourceful",
        "expertise": ["Fundraising", "Startup Equity", "Angel Investing"],
        "image": "Reshman_Saujani.png",
        "color": "#E879F9",
        "emoji": "💖"
    },
    "Sara Blakely": {
        "title": "Bootstrap Finance Expert",
        "description": "Self-made approach to bootstrapping businesses, cash flow management, and building wealth",
        "style": "creative and determined",
        "expertise": ["Bootstrapping", "Cash Flow", "Wealth Building"],
        "image": "Sara_Blakely.png",
        "color": "#FBCFE8",
        "emoji": "👑"
    }
}

# -------------------
# 🎨 Page Configuration
# -------------------
st.set_page_config(
    page_title="Finance Leaders AI Chat",
    page_icon="💕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------
# 💅 Custom CSS Styling with Animations
# -------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Animated gradient background */
    .stApp {
        background: linear-gradient(-45deg, #FFF5F7, #FFF0F5, #FCE7F3, #FAE8FF, #FEF3C7);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Floating hearts animation */
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(5deg); }
    }
    
    /* Sparkle animation */
    @keyframes sparkle {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(1.2); }
    }
    
    /* Card pop-in animation */
    @keyframes popIn {
        0% {
            opacity: 0;
            transform: scale(0.8) translateY(30px);
        }
        60% {
            transform: scale(1.05) translateY(-5px);
        }
        100% {
            opacity: 1;
            transform: scale(1) translateY(0);
        }
    }
    
    /* Pulse animation for buttons */
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    /* Shimmer effect */
    @keyframes shimmer {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }
    
    /* Card styling with animations */
    .leader-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(20px);
        border-radius: 30px;
        border: 3px solid rgba(255, 182, 193, 0.3);
        padding: 0;
        transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        cursor: pointer;
        height: 100%;
        overflow: hidden;
        box-shadow: 0 10px 40px rgba(255, 105, 180, 0.15);
        animation: popIn 0.6s ease-out;
        position: relative;
    }
    
    .leader-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.5), transparent);
        animation: shimmer 3s infinite;
    }
    
    .leader-card:hover {
        transform: translateY(-15px) scale(1.03) rotate(-1deg);
        border-color: rgba(255, 105, 180, 0.6);
        box-shadow: 0 20px 60px rgba(255, 105, 180, 0.3), 0 0 30px rgba(255, 182, 193, 0.5);
    }
    
    .leader-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 24px 24px 0 0;
        transition: transform 0.4s ease;
    }
    
    .leader-card:hover .leader-image {
        transform: scale(1.1);
    }
    
    /* Chat message styling with animations */
    .user-message {
        background: linear-gradient(135deg, #FF6B9D 0%, #F472B6 50%, #EC4899 100%);
        color: white;
        padding: 18px 24px;
        border-radius: 25px 25px 5px 25px;
        margin: 10px 0;
        margin-left: auto;
        max-width: 70%;
        box-shadow: 0 8px 25px rgba(255, 105, 180, 0.3);
        animation: slideInRight 0.4s ease-out;
        position: relative;
        overflow: hidden;
    }
    
    .user-message::before {
        content: '✨';
        position: absolute;
        right: 10px;
        top: 10px;
        animation: sparkle 2s infinite;
    }
    
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .assistant-message {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(252, 231, 243, 0.95));
        backdrop-filter: blur(20px);
        color: #831843;
        padding: 18px 24px;
        border-radius: 25px 25px 25px 5px;
        margin: 10px 0;
        max-width: 70%;
        border: 2px solid rgba(255, 182, 193, 0.4);
        box-shadow: 0 8px 25px rgba(219, 39, 119, 0.15);
        animation: slideInLeft 0.4s ease-out;
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
    
    /* Title styling with animation */
    .main-title {
        text-align: center;
        font-size: 5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #FF6B9D, #F472B6, #EC4899, #DB2777);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 10px;
        animation: float 3s ease-in-out infinite;
        text-shadow: 0 0 30px rgba(255, 105, 180, 0.3);
        letter-spacing: -2px;
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.8rem;
        color: #DB2777;
        margin-bottom: 20px;
        animation: fadeIn 1s ease-in;
        font-weight: 600;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Button styling with animations */
    .stButton>button {
        background: linear-gradient(135deg, #FF6B9D, #F472B6, #EC4899);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 14px 32px;
        font-weight: 700;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(255, 105, 180, 0.4);
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 14px;
    }
    
    .stButton>button:hover {
        transform: scale(1.08) translateY(-3px);
        box-shadow: 0 12px 35px rgba(255, 105, 180, 0.6);
        animation: pulse 0.5s ease;
    }
    
    .stButton>button:active {
        transform: scale(0.98);
    }
    
    /* Input styling */
    .stTextInput>div>div>input {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(20px);
        border: 3px solid rgba(255, 182, 193, 0.4);
        border-radius: 20px;
        color: #831843;
        padding: 14px 24px;
        font-size: 16px;
        transition: all 0.3s ease;
        font-weight: 500;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #FF6B9D;
        box-shadow: 0 0 25px rgba(255, 105, 180, 0.4);
        transform: scale(1.02);
    }
    
    .stTextInput>div>div>input::placeholder {
        color: #F472B6;
        opacity: 0.7;
    }
    
    /* Expertise tags with animation */
    .expertise-tag {
        display: inline-block;
        background: linear-gradient(135deg, rgba(255, 182, 193, 0.6), rgba(252, 231, 243, 0.8));
        padding: 8px 16px;
        border-radius: 25px;
        font-size: 11px;
        color: #BE185D;
        margin: 4px;
        border: 2px solid rgba(255, 182, 193, 0.5);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
    }
    
    .expertise-tag:hover {
        transform: scale(1.1);
        background: linear-gradient(135deg, #FF6B9D, #F472B6);
        color: white;
    }
    
    /* Header styling */
    .chat-header {
        background: linear-gradient(135deg, #FF6B9D, #F472B6, #EC4899);
        padding: 28px;
        border-radius: 25px;
        margin-bottom: 20px;
        box-shadow: 0 12px 40px rgba(255, 105, 180, 0.4);
        animation: slideDown 0.5s ease-out;
        position: relative;
        overflow: hidden;
    }
    
    .chat-header::before {
        content: '✨';
        position: absolute;
        font-size: 50px;
        opacity: 0.2;
        right: 20px;
        top: 50%;
        transform: translateY(-50%);
        animation: sparkle 3s infinite;
    }
    
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Decorative elements */
    .floating-hearts {
        position: fixed;
        font-size: 30px;
        opacity: 0.3;
        animation: float 4s ease-in-out infinite;
        z-index: -1;
    }
    
    /* Card content padding */
    .card-content {
        padding: 20px;
    }
    
    /* Typing indicator */
    .typing-indicator {
        display: flex;
        gap: 5px;
        padding: 15px;
    }
    
    .typing-dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #FF6B9D;
        animation: typingAnimation 1.4s infinite;
    }
    
    .typing-dot:nth-child(2) {
        animation-delay: 0.2s;
    }
    
    .typing-dot:nth-child(3) {
        animation-delay: 0.4s;
    }
    
    @keyframes typingAnimation {
        0%, 60%, 100% {
            transform: translateY(0);
            opacity: 0.7;
        }
        30% {
            transform: translateY(-15px);
            opacity: 1;
        }
    }
    
    /* Sparkle decoration */
    .sparkle-decoration {
        display: inline-block;
        animation: sparkle 2s infinite;
    }
</style>
""", unsafe_allow_html=True)

# Add floating hearts decoration
st.markdown("""
    <div class="floating-hearts" style="left: 10%; top: 20%;">💕</div>
    <div class="floating-hearts" style="right: 15%; top: 30%; animation-delay: 1s;">✨</div>
    <div class="floating-hearts" style="left: 20%; bottom: 25%; animation-delay: 2s;">🌸</div>
    <div class="floating-hearts" style="right: 10%; bottom: 35%; animation-delay: 1.5s;">💖</div>
    <div class="floating-hearts" style="left: 50%; top: 15%; animation-delay: 0.5s;">🦋</div>
""", unsafe_allow_html=True)

# -------------------
# 💬 Initialize Session State
# -------------------
if "messages" not in st.session_state:
    st.session_state.messages = {
        name: [{"role": "system", "content": f"You are {name}, a financial expert with expertise in {leaders[name]['expertise'][0]}. You speak in a {leaders[name]['style']} style. Provide insightful, warm, and encouraging financial advice related to {leaders[name]['title']}."}]
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
    st.markdown('<h1 class="main-title">💕 Finance Queens 💕</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle"><span class="sparkle-decoration">✨</span> Learn from Visionaries Who Changed the World <span class="sparkle-decoration">✨</span></p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #DB2777; margin-bottom: 50px; font-size: 1.2rem; font-weight: 600;">💖 Select your finance mentor and start your journey 💖</p>', unsafe_allow_html=True)
    
    # Add a decorative divider
    st.markdown('<div style="width: 200px; height: 4px; background: linear-gradient(90deg, #FF6B9D, #F472B6, #EC4899); margin: 30px auto; border-radius: 10px;"></div>', unsafe_allow_html=True)
    
    # First Row - 5 Leaders
    cols1 = st.columns(5, gap="large")
    leader_names = list(leaders.keys())
    
    for idx, col in enumerate(cols1):
        if idx < len(leader_names):
            leader_name = leader_names[idx]
            leader = leaders[leader_name]
            
            with col:
                # Card container
                st.markdown(f'<div class="leader-card" style="animation-delay: {idx * 0.1}s;">', unsafe_allow_html=True)
                
                # Try to load image
                try:
                    if os.path.exists(leader['image']):
                        st.markdown('<div style="overflow: hidden; border-radius: 24px 24px 0 0;">', unsafe_allow_html=True)
                        st.image(leader['image'], use_container_width=True)
                        st.markdown('</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div style="height: 200px; background: linear-gradient(135deg, {leader['color']}, #FECACA); border-radius: 24px 24px 0 0; display: flex; align-items: center; justify-content: center; font-size: 80px; position: relative; overflow: hidden;">
                            <div style="position: absolute; font-size: 120px; opacity: 0.2;">{leader['emoji']}</div>
                            <div style="position: relative;">{leader['emoji']}</div>
                        </div>
                        """, unsafe_allow_html=True)
                except:
                    st.markdown(f"""
                    <div style="height: 200px; background: linear-gradient(135deg, {leader['color']}, #FECACA); border-radius: 24px 24px 0 0; display: flex; align-items: center; justify-content: center; font-size: 80px; position: relative; overflow: hidden;">
                        <div style="position: absolute; font-size: 120px; opacity: 0.2;">{leader['emoji']}</div>
                        <div style="position: relative;">{leader['emoji']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Card content
                st.markdown(f"""
                <div class="card-content">
                    <h3 style="color: #831843; font-size: 19px; font-weight: 800; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
                        <span>{leader['emoji']}</span> {leader_name}
                    </h3>
                    <p style="color: {leader['color']}; font-size: 13px; margin-bottom: 12px; font-weight: 600;">💼 {leader['title']}</p>
                    <p style="color: #BE185D; font-size: 12px; line-height: 1.6; margin-bottom: 16px; font-weight: 500;">{leader['description'][:75]}...</p>
                    <div style="margin-bottom: 16px;">
                        {''.join([f'<span class="expertise-tag">{skill}</span>' for skill in leader['expertise'][:2]])}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                if st.button(f"✨ Chat with {leader_name.split()[0]}", key=f"btn_{idx}", use_container_width=True):
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
                st.markdown(f'<div class="leader-card" style="animation-delay: {(idx + 5) * 0.1}s;">', unsafe_allow_html=True)
                
                # Try to load image
                try:
                    if os.path.exists(leader['image']):
                        st.markdown('<div style="overflow: hidden; border-radius: 24px 24px 0 0;">', unsafe_allow_html=True)
                        st.image(leader['image'], use_container_width=True)
                        st.markdown('</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div style="height: 200px; background: linear-gradient(135deg, {leader['color']}, #FECACA); border-radius: 24px 24px 0 0; display: flex; align-items: center; justify-content: center; font-size: 80px; position: relative; overflow: hidden;">
                            <div style="position: absolute; font-size: 120px; opacity: 0.2;">{leader['emoji']}</div>
                            <div style="position: relative;">{leader['emoji']}</div>
                        </div>
                        """, unsafe_allow_html=True)
                except:
                    st.markdown(f"""
                    <div style="height: 200px; background: linear-gradient(135deg, {leader['color']}, #FECACA); border-radius: 24px 24px 0 0; display: flex; align-items: center; justify-content: center; font-size: 80px; position: relative; overflow: hidden;">
                        <div style="position: absolute; font-size: 120px; opacity: 0.2;">{leader['emoji']}</div>
                        <div style="position: relative;">{leader['emoji']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Card content
                st.markdown(f"""
                <div class="card-content">
                    <h3 style="color: #831843; font-size: 19px; font-weight: 800; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
                        <span>{leader['emoji']}</span> {leader_name}
                    </h3>
                    <p style="color: {leader['color']}; font-size: 13px; margin-bottom: 12px; font-weight: 600;">💼 {leader['title']}</p>
                    <p style="color: #BE185D; font-size: 12px; line-height: 1.6; margin-bottom: 16px; font-weight: 500;">{leader['description'][:75]}...</p>
                    <div style="margin-bottom: 16px;">
                        {''.join([f'<span class="expertise-tag">{skill}</span>' for skill in leader['expertise'][:2]])}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                if st.button(f"✨ Chat with {leader_name.split()[0]}", key=f"btn_{actual_idx}", use_container_width=True):
                    st.session_state.selected_leader = leader_name
                    st.rerun()
    
    # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; padding: 40px;">
        <div style="display: inline-flex; align-items: center; gap: 15px; background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(20px); padding: 20px 40px; border-radius: 50px; border: 3px solid rgba(255, 182, 193, 0.5); box-shadow: 0 10px 40px rgba(255, 105, 180, 0.2);">
            <span style="font-size: 24px;" class="sparkle-decoration">✨</span>
            <span style="color: #DB2777; font-weight: 700; font-size: 1.1rem;">Powered by wisdom, grace & financial excellence</span>
            <span style="font-size: 24px;" class="sparkle-decoration">💕</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------
# 💬 Chat Page
# -------------------
else:
    leader_name = st.session_state.selected_leader
    leader = leaders[leader_name]
    
    # Chat Header
    col1, col2 = st.columns([1, 8])
    
    with col1:
        if st.button("← Back", key="back_button"):
            st.session_state.selected_leader = None
            st.rerun()
    
    with col2:
        st.markdown(f"""
        <div class="chat-header">
            <div style="display: flex; align-items: center; gap: 24px;">
                <div style="width: 80px; height: 80px; background: rgba(255, 255, 255, 0.3); backdrop-filter: blur(10px); border-radius: 20px; display: flex; align-items: center; justify-content: center; font-size: 42px; border: 4px solid rgba(255, 255, 255, 0.5); box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);">
                    {leader['emoji']}
                </div>
                <div>
                    <h2 style="color: white; margin: 0; font-size: 32px; font-weight: 900; text-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);">{leader_name}</h2>
                    <p style="color: rgba(255, 255, 255, 0.95); margin: 6px 0; font-size: 17px; font-weight: 600;">{leader['title']}</p>
                    <div style="margin-top: 10px;">
                        {''.join([f'<span style="background: rgba(255, 255, 255, 0.3); padding: 6px 14px; border-radius: 25px; font-size: 13px; color: white; margin-right: 8px; border: 2px solid rgba(255, 255, 255, 0.4); font-weight: 600; display: inline-block;">{skill}</span>' for skill in leader['expertise']])}
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Display Chat Messages
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.messages[leader_name][1:]:  # Skip system message
            if msg["role"] == "user":
                st.markdown(f'<div style="display: flex; justify-content: flex-end;"><div class="user-message">{msg["content"]}</div></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="assistant-message">💕 {msg["content"]}</div>', unsafe_allow_html=True)
        
        # Typing indicator
        if st.session_state.typing:
            st.markdown("""
            <div class="assistant-message" style="padding: 10px 20px;">
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
            placeholder=f"✨ Ask {leader_name.split()[0]} about {leader['expertise'][0].lower()}...",
            key="user_input",
            label_visibility="collapsed"
        )
    
    with col2:
        send_button = st.button("Send 💖", use_container_width=True)
    
    # Process Message
    if send_button and user_input:
        # Add user message
        st.session_state.messages[leader_name].append({"role": "user", "content": user_input})
        st.session_state.typing = True
        st.rerun()
    
    # Get AI response if typing
    if st.session_state.typing:
        with st.spinner(f"💕 {leader_name.split()[0]} is thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=st.session_state.messages[leader_name],
                    temperature=0.7,
                    max_tokens=400
                )
                reply = response.choices[0].message.content
                
                # Add assistant message
                st.session_state.messages[leader_name].append({"role": "assistant", "content": reply})
                st.session_state.typing = False
                
            except Exception as e:
                st.error(f"💔 Oops! Something went wrong: {str(e)}")
                st.session_state.typing = False
        
        st.rerun()

# -------------------
# 📊 Sidebar Info
# -------------------
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <div style="font-size: 60px; margin-bottom: 20px;">💕</div>
        <h2 style="color: #DB2777; font-weight: 800;">Finance Queens</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(255, 182, 193, 0.3), rgba(252, 231, 243, 0.5)); 
                padding: 20px; border-radius: 20px; border: 2px solid rgba(255, 182, 193, 0.5); margin-bottom: 20px;">
        <h3 style="color: #BE185D; font-weight: 700; margin-bottom: 15px;">✨ About</h3>
        <p style="color: #831843; line-height: 1.6; font-weight: 500;">
            Connect with 10 inspiring women leaders and learn from their unique perspectives on finance, business, and leadership. 
            Each mentor brings her own expertise to guide you! 💖
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(255, 182, 193, 0.3), rgba(252, 231, 243, 0.5)); 
                padding: 20px; border-radius: 20px; border: 2px solid rgba(255, 182, 193, 0.5);">
        <h3 style="color: #BE185D; font-weight: 700; margin-bottom: 15px;">🎯 Features</h3>
        <ul style="color: #831843; line-height: 2; font-weight: 500; list-style: none; padding-left: 0;">
            <li>💕 Personalized financial advice</li>
            <li>✨ Expert insights from diverse fields</li>
            <li>🦋 Real-time AI conversations</li>
            <li>👑 Empowering guidance</li>
            <li>💖 Supportive community</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; padding: 15px; background: rgba(255, 182, 193, 0.2); 
                border-radius: 15px; border: 2px solid rgba(255, 182, 193, 0.4);">
        <p style="color: #DB2777; font-weight: 700; margin: 0;">
            ✨ Powered by OpenAI GPT-3.5 ✨
        </p>
    </div>
    """, unsafe_allow_html=True)
