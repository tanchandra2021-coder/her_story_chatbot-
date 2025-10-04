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
        "gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
    },
    "Angela Merkel": {
        "title": "Economic Policy Expert",
        "description": "Analytical approach to fiscal policy, European economics, and strategic financial planning",
        "style": "analytical and methodical",
        "expertise": ["Fiscal Policy", "European Markets", "Economic Strategy"],
        "image": "Angela_Merkel.png",
        "gradient": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)"
    },
    "Malala Yousafzai": {
        "title": "Social Finance Advocate",
        "description": "Passionate insights on funding education, microfinance, and investing in social change",
        "style": "passionate and principled",
        "expertise": ["Microfinance", "Social Bonds", "Education Funding"],
        "image": "Malala_Yousafazi.png",
        "gradient": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)"
    },
    "Ruth Bader Ginsburg": {
        "title": "Financial Law & Ethics",
        "description": "Precise guidance on financial regulations, investment law, and ethical wealth management",
        "style": "precise and principled",
        "expertise": ["Financial Law", "Securities", "Compliance"],
        "image": "Ruth_Bader_Ginsburg.png",
        "gradient": "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)"
    },
    "Indra Nooyi": {
        "title": "Corporate Finance Leader",
        "description": "Strategic insights on corporate finance, M&A, sustainable business growth, and CFO excellence",
        "style": "strategic and visionary",
        "expertise": ["Corporate Finance", "M&A", "Business Strategy"],
        "image": "Indra_Nooyi.png",
        "gradient": "linear-gradient(135deg, #fa709a 0%, #fee140 100%)"
    },
    "Sheryl Sandberg": {
        "title": "Tech Finance Executive",
        "description": "Data-driven approach to tech valuations, scaling startups, and financial operations",
        "style": "analytical and motivational",
        "expertise": ["Tech Finance", "Scaling", "Operations"],
        "image": "Sheryl_Sandberg.png",
        "gradient": "linear-gradient(135deg, #30cfd0 0%, #330867 100%)"
    },
    "Jacinda Ardern": {
        "title": "Wellbeing Economics",
        "description": "Compassionate approach to budget management, public finance, and wellbeing economics",
        "style": "empathetic and pragmatic",
        "expertise": ["Public Finance", "Budget Policy", "Wellbeing Economy"],
        "image": "Jacinda_Ardern.png",
        "gradient": "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)"
    },
    "Mae Jemison": {
        "title": "STEM Finance Pioneer",
        "description": "Innovative thinking on R&D funding, STEM investment, and technology venture capital",
        "style": "innovative and scientific",
        "expertise": ["Venture Capital", "R&D Finance", "Tech Investment"],
        "image": "Mae_Jemison.png",
        "gradient": "linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)"
    },
    "Reshma Saujani": {
        "title": "Startup Finance Advocate",
        "description": "Bold approach to fundraising, startup equity, and building financial resilience in tech",
        "style": "bold and resourceful",
        "expertise": ["Fundraising", "Startup Equity", "Angel Investing"],
        "image": "Reshman_Saujani.png",
        "gradient": "linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%)"
    },
    "Sara Blakely": {
        "title": "Bootstrap Finance Expert",
        "description": "Self-made approach to bootstrapping businesses, cash flow management, and building wealth",
        "style": "creative and determined",
        "expertise": ["Bootstrapping", "Cash Flow", "Wealth Building"],
        "image": "Sara_Blakely.png",
        "gradient": "linear-gradient(135deg, #fdcbf1 0%, #e6dee9 100%)"
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
# 💅 Custom CSS Styling with Smooth Animations
# -------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Smooth animated gradient background */
    .stApp {
        background: linear-gradient(-45deg, #E0F2F7, #F0F4F8, #E8F5E9, #FFF3E0, #F3E5F5);
        background-size: 400% 400%;
        animation: gradientFlow 20s ease infinite;
    }
    
    @keyframes gradientFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Smooth fade in animation */
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
    
    /* Card styling with smooth animations */
    .leader-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 24px;
        border: 2px solid rgba(200, 200, 200, 0.2);
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        height: 100%;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        animation: fadeInUp 0.6s ease-out;
    }
    
    .leader-card:hover {
        transform: translateY(-12px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        border-color: rgba(150, 150, 150, 0.3);
    }
    
    .leader-image-container {
        width: 100%;
        height: 220px;
        overflow: hidden;
        position: relative;
    }
    
    .leader-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .leader-card:hover .leader-image {
        transform: scale(1.08);
    }
    
    /* Gradient overlay on images */
    .gradient-overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        opacity: 0;
        transition: opacity 0.4s ease;
    }
    
    .leader-card:hover .gradient-overlay {
        opacity: 0.3;
    }
    
    /* Chat message animations */
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 16px 22px;
        border-radius: 20px 20px 4px 20px;
        margin: 12px 0;
        margin-left: auto;
        max-width: 70%;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        animation: slideInRight 0.4s ease-out;
    }
    
    .assistant-message {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(240, 244, 248, 0.95));
        backdrop-filter: blur(10px);
        color: #2C3E50;
        padding: 16px 22px;
        border-radius: 20px 20px 20px 4px;
        margin: 12px 0;
        max-width: 70%;
        border: 2px solid rgba(200, 200, 200, 0.2);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        animation: slideInLeft 0.4s ease-out;
    }
    
    /* Title styling */
    .main-title {
        text-align: center;
        font-size: 4.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #43e97b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 20px;
        letter-spacing: -2px;
        animation: fadeInUp 0.8s ease-out;
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.4rem;
        color: #5A67D8;
        margin-bottom: 30px;
        font-weight: 600;
        animation: fadeInUp 1s ease-out;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 16px;
        padding: 12px 28px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    .stButton>button:active {
        transform: translateY(0);
    }
    
    /* Input styling */
    .stTextInput>div>div>input {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(200, 200, 200, 0.3);
        border-radius: 16px;
        color: #2C3E50;
        padding: 14px 20px;
        font-size: 15px;
        transition: all 0.3s ease;
        font-weight: 500;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    .stTextInput>div>div>input::placeholder {
        color: #A0AEC0;
    }
    
    /* Expertise tags */
    .expertise-tag {
        display: inline-block;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(67, 233, 123, 0.1));
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 11px;
        color: #5A67D8;
        margin: 4px;
        border: 1.5px solid rgba(102, 126, 234, 0.3);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
    }
    
    .expertise-tag:hover {
        transform: scale(1.05);
        border-color: rgba(102, 126, 234, 0.6);
    }
    
    /* Header styling */
    .chat-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 28px;
        border-radius: 20px;
        margin-bottom: 24px;
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.3);
        animation: fadeInUp 0.5s ease-out;
    }
    
    /* Card content padding */
    .card-content {
        padding: 20px;
    }
    
    /* Typing indicator */
    .typing-indicator {
        display: flex;
        gap: 6px;
        padding: 12px;
    }
    
    .typing-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #667eea;
        animation: typingPulse 1.4s infinite ease-in-out;
    }
    
    .typing-dot:nth-child(2) {
        animation-delay: 0.2s;
    }
    
    .typing-dot:nth-child(3) {
        animation-delay: 0.4s;
    }
    
    @keyframes typingPulse {
        0%, 80%, 100% {
            opacity: 0.4;
            transform: scale(0.8);
        }
        40% {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    /* Smooth hover transitions for all interactive elements */
    a, button, input, .leader-card, .expertise-tag {
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
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
    st.markdown('<p style="text-align: center; color: #718096; margin-bottom: 50px; font-size: 1.1rem; font-weight: 500;">Select a leader to explore their financial expertise</p>', unsafe_allow_html=True)
    
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
                
                # Image container with gradient overlay
                st.markdown('<div class="leader-image-container">', unsafe_allow_html=True)
                
                # Try to load image
                try:
                    if os.path.exists(leader['image']):
                        st.image(leader['image'], use_container_width=True)
                    else:
                        st.markdown(f"""
                        <div style="width: 100%; height: 220px; background: {leader['gradient']}; display: flex; align-items: center; justify-content: center; font-size: 80px;">
                            💼
                        </div>
                        """, unsafe_allow_html=True)
                except:
                    st.markdown(f"""
                    <div style="width: 100%; height: 220px; background: {leader['gradient']}; display: flex; align-items: center; justify-content: center; font-size: 80px;">
                        💼
                    </div>
                    """, unsafe_allow_html=True)
                
                # Gradient overlay
                st.markdown(f'<div class="gradient-overlay" style="background: {leader["gradient"]};"></div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Card content
                st.markdown(f"""
                <div class="card-content">
                    <h3 style="color: #2D3748; font-size: 18px; font-weight: 700; margin-bottom: 8px;">
                        {leader_name}
                    </h3>
                    <p style="color: #5A67D8; font-size: 13px; margin-bottom: 12px; font-weight: 600;">{leader['title']}</p>
                    <p style="color: #4A5568; font-size: 12px; line-height: 1.6; margin-bottom: 16px; font-weight: 500;">{leader['description']}</p>
                    <div style="margin-bottom: 16px;">
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
                st.markdown(f'<div class="leader-card" style="animation-delay: {(idx + 5) * 0.1}s;">', unsafe_allow_html=True)
                
                # Image container with gradient overlay
                st.markdown('<div class="leader-image-container">', unsafe_allow_html=True)
                
                # Try to load image
                try:
                    if os.path.exists(leader['image']):
                        st.image(leader['image'], use_container_width=True)
                    else:
                        st.markdown(f"""
                        <div style="width: 100%; height: 220px; background: {leader['gradient']}; display: flex; align-items: center; justify-content: center; font-size: 80px;">
                            💼
                        </div>
                        """, unsafe_allow_html=True)
                except:
                    st.markdown(f"""
                    <div style="width: 100%; height: 220px; background: {leader['gradient']}; display: flex; align-items: center; justify-content: center; font-size: 80px;">
                        💼
                    </div>
                    """, unsafe_allow_html=True)
                
                # Gradient overlay
                st.markdown(f'<div class="gradient-overlay" style="background: {leader["gradient"]};"></div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Card content
                st.markdown(f"""
                <div class="card-content">
                    <h3 style="color: #2D3748; font-size: 18px; font-weight: 700; margin-bottom: 8px;">
                        {leader_name}
                    </h3>
                    <p style="color: #5A67D8; font-size: 13px; margin-bottom: 12px; font-weight: 600;">{leader['title']}</p>
                    <p style="color: #4A5568; font-size: 12px; line-height: 1.6; margin-bottom: 16px; font-weight: 500;">{leader['description']}</p>
                    <div style="margin-bottom: 16px;">
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
    <div style="text-align: center; padding: 40px;">
        <div style="display: inline-flex; align-items: center; gap: 15px; background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); padding: 18px 36px; border-radius: 50px; border: 2px solid rgba(200, 200, 200, 0.2); box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);">
            <span style="color: #5A67D8; font-weight: 600; font-size: 1rem;">Powered by wisdom and financial excellence</span>
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
                <div style="width: 80px; height: 80px; background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(10px); border-radius: 20px; display: flex; align-items: center; justify-content: center; font-size: 42px; border: 3px solid rgba(255, 255, 255, 0.4);">
                    💼
                </div>
                <div>
                    <h2 style="color: white; margin: 0; font-size: 32px; font-weight: 800;">{leader_name}</h2>
                    <p style="color: rgba(255, 255, 255, 0.95); margin: 6px 0; font-size: 17px; font-weight: 600;">{leader['title']}</p>
                    <div style="margin-top: 10px;">
                        {''.join([f'<span style="background: rgba(255, 255, 255, 0.2); padding: 6px 14px; border-radius: 20px; font-size: 13px; color: white; margin-right: 8px; border: 2px solid rgba(255, 255, 255, 0.3); font-weight: 600; display: inline-block;">{skill}</span>' for skill in leader['expertise']])}
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
                st.markdown(f'<div class="assistant-message">{msg["content"]}</div>', unsafe_allow_html=True)
        
        # Typing indicator
        if st.session_state.typing:
            st.markdown("""
            <div class="assistant-message" style="padding: 8px 16px;">
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
        # Add user message
        st.session_state.messages[leader_name].append({"role": "user", "content": user_input})
        st.session_state.typing = True
        st.rerun()
    
    # Get AI response if typing
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
                
                # Add assistant message
                st.session_state.messages[leader_name].append({"role": "assistant", "content": reply})
                st.session_state.typing = False
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.session_state.typing = False
        
        st.rerun()

# -------------------
# 📊 Sidebar Info
# -------------------
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <div style="font-size: 60px; margin-bottom: 20px;">💼</div>
        <h2 style="color: #5A67D8; font-weight: 800;">Finance Leaders</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 16px; border: 2px solid rgba(200, 200, 200, 0.2); margin-bottom: 20px;">
        <h3 style="color: #2D3748; font-weight: 700; margin-bottom: 15px;">About</h3>
        <p style="color: #4A5568; line-height: 1.6; font-weight: 500;">
            Connect with 10 inspiring women leaders and learn from their unique perspectives on finance, business, and leadership.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 16px; border: 2px solid rgba(200, 200, 200, 0.2);">
        <h3 style="color: #2D3748; font-weight: 700; margin-bottom: 15px;">Features</h3>
        <ul style="color: #4A5568; line-height: 2; font-weight: 500;">
            <li>Personalize
