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
        "gradient": "linear-gradient(135deg, #FFE5F1 0%, #E8D4F2 100%)",
        "emoji": "🌸",
        "topics": ["Personal Finance", "Education", "Social Impact"]
    },
    "Angela Merkel": {
        "title": "Economic Policy Expert",
        "description": "Analytical approach to fiscal policy, European economics, and strategic financial planning",
        "style": "analytical and methodical",
        "expertise": ["Fiscal Policy", "European Markets", "Economic Strategy"],
        "image": "Angela_Merkel.png",
        "gradient": "linear-gradient(135deg, #FFE5E5 0%, #E8D4FF 100%)",
        "emoji": "📊",
        "topics": ["Economic Policy", "Government Finance", "Strategic Planning"]
    },
    "Malala Yousafzai": {
        "title": "Social Finance Advocate",
        "description": "Passionate insights on funding education, microfinance, and investing in social change",
        "style": "passionate and principled",
        "expertise": ["Microfinance", "Social Bonds", "Education Funding"],
        "image": "Malala_Yousafazi.png",
        "gradient": "linear-gradient(135deg, #D4F1F4 0%, #B8E8FC 100%)",
        "emoji": "💙",
        "topics": ["Microfinance", "Education", "Social Change"]
    },
    "Ruth Bader Ginsburg": {
        "title": "Financial Law & Ethics",
        "description": "Precise guidance on financial regulations, investment law, and ethical wealth management",
        "style": "precise and principled",
        "expertise": ["Financial Law", "Securities", "Compliance"],
        "image": "Ruth_Bader_Ginsburg.png",
        "gradient": "linear-gradient(135deg, #E8F5E9 0%, #BFECFF 100%)",
        "emoji": "⚖️",
        "topics": ["Financial Law", "Ethics", "Compliance"]
    },
    "Indra Nooyi": {
        "title": "Corporate Finance Leader",
        "description": "Strategic insights on corporate finance, M&A, sustainable business growth, and CFO excellence",
        "style": "strategic and visionary",
        "expertise": ["Corporate Finance", "M&A", "Business Strategy"],
        "image": "Indra_Nooyi.png",
        "gradient": "linear-gradient(135deg, #FFF0E5 0%, #FFE8F0 100%)",
        "emoji": "💼",
        "topics": ["Finance Careers", "Corporate Strategy", "Leadership"]
    },
    "Sheryl Sandberg": {
        "title": "Tech Finance Executive",
        "description": "Data-driven approach to tech valuations, scaling startups, and financial operations",
        "style": "analytical and motivational",
        "expertise": ["Tech Finance", "Scaling", "Operations"],
        "image": "Sheryl_Sandberg.png",
        "gradient": "linear-gradient(135deg, #F3E5F5 0%, #E1F5FE 100%)",
        "emoji": "💻",
        "topics": ["Tech Finance", "Startups", "Scaling"]
    },
    "Jacinda Ardern": {
        "title": "Wellbeing Economics",
        "description": "Compassionate approach to budget management, public finance, and wellbeing economics",
        "style": "empathetic and pragmatic",
        "expertise": ["Public Finance", "Budget Policy", "Wellbeing Economy"],
        "image": "Jacinda_Ardern.png",
        "gradient": "linear-gradient(135deg, #FFF8E1 0%, #E8F5E9 100%)",
        "emoji": "🌿",
        "topics": ["Public Finance", "Wellbeing", "Budget Management"]
    },
    "Mae Jemison": {
        "title": "STEM Finance Pioneer",
        "description": "Innovative thinking on R&D funding, STEM investment, and technology venture capital",
        "style": "innovative and scientific",
        "expertise": ["Venture Capital", "R&D Finance", "Tech Investment"],
        "image": "Mae_Jemison.png",
        "gradient": "linear-gradient(135deg, #FFE5F1 0%, #F3E5F5 100%)",
        "emoji": "🚀",
        "topics": ["Venture Capital", "STEM", "Innovation"]
    },
    "Reshma Saujani": {
        "title": "Startup Finance Advocate",
        "description": "Bold approach to fundraising, startup equity, and building financial resilience in tech",
        "style": "bold and resourceful",
        "expertise": ["Fundraising", "Startup Equity", "Angel Investing"],
        "image": "Reshman_Saujani.png",
        "gradient": "linear-gradient(135deg, #FFF3E0 0%, #F3E5F5 100%)",
        "emoji": "🎯",
        "topics": ["Fundraising", "Startups", "Tech"]
    },
    "Sara Blakely": {
        "title": "Bootstrap Finance Expert",
        "description": "Self-made approach to bootstrapping businesses, cash flow management, and building wealth",
        "style": "creative and determined",
        "expertise": ["Bootstrapping", "Cash Flow", "Wealth Building"],
        "image": "Sara_Blakely.png",
        "gradient": "linear-gradient(135deg, #FFF9C4 0%, #FFEBEE 100%)",
        "emoji": "✨",
        "topics": ["Entrepreneurship", "Wealth Building", "Bootstrapping"]
    }
}

# Page Configuration
st.set_page_config(
    page_title="Finance Leaders AI Chat",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with lighter background and 3D carousel
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Lighter animated background */
    .stApp {
        background: linear-gradient(-45deg, #E3F2FD, #F3E5F5, #FFF8E1, #E8F5E9, #FFE5F1);
        background-size: 400% 400%;
        animation: gradientShift 20s ease infinite;
    }
    
    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .main-title {
        text-align: center;
        font-size: 5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 20px;
        letter-spacing: 8px;
        font-family: 'Orbitron', sans-serif;
        text-transform: uppercase;
        animation: titlePulse 3s ease-in-out infinite;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1));
    }
    
    @keyframes titlePulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.5rem;
        color: #667eea;
        margin-bottom: 20px;
        font-weight: 600;
        letter-spacing: 3px;
        text-transform: uppercase;
        font-family: 'Rajdhani', sans-serif;
    }
    
    .greeting-box {
        text-align: center;
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(102, 126, 234, 0.3);
        padding: 20px 40px;
        border-radius: 50px;
        margin: 30px auto 50px;
        max-width: 600px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        animation: floatBox 3s ease-in-out infinite;
    }
    
    @keyframes floatBox {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* 3D Carousel Card with POP effect */
    .leader-card {
        background: white;
        border-radius: 30px;
        border: 3px solid rgba(102, 126, 234, 0.2);
        overflow: hidden;
        transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: pointer;
        box-shadow: 
            0 20px 60px rgba(0,0,0,0.15),
            0 0 0 1px rgba(255,255,255,0.8) inset;
        animation: cardEntrance 0.8s ease-out backwards;
        position: relative;
        transform-style: preserve-3d;
        perspective: 1000px;
    }
    
    @keyframes cardEntrance {
        from {
            opacity: 0;
            transform: translateY(60px) rotateX(-20deg) scale(0.8);
        }
        to {
            opacity: 1;
            transform: translateY(0) rotateX(0) scale(1);
        }
    }
    
    .leader-card:hover {
        transform: translateY(-30px) scale(1.08) rotateY(5deg);
        box-shadow: 
            0 40px 80px rgba(102, 126, 234, 0.4),
            0 0 0 2px rgba(102, 126, 234, 0.5) inset,
            0 0 60px rgba(102, 126, 234, 0.3);
        border-color: rgba(102, 126, 234, 0.5);
    }
    
    .leader-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(
            45deg,
            transparent,
            rgba(255, 255, 255, 0.5),
            transparent
        );
        transform: rotate(45deg);
        transition: all 0.6s;
        opacity: 0;
    }
    
    .leader-card:hover::before {
        opacity: 1;
        top: 50%;
        left: 50%;
    }
    
    /* Circular image with 3D effect */
    .profile-image-wrapper {
        width: 100%;
        padding: 30px;
        display: flex;
        justify-content: center;
        position: relative;
    }
    
    .profile-image {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        border: 5px solid white;
        box-shadow: 
            0 20px 40px rgba(0,0,0,0.2),
            0 0 0 10px rgba(102, 126, 234, 0.1),
            0 0 60px rgba(102, 126, 234, 0.3) inset;
        transition: all 0.6s ease;
        object-fit: cover;
        transform: translateZ(50px);
    }
    
    .leader-card:hover .profile-image {
        transform: translateZ(80px) scale(1.1) rotateZ(5deg);
        box-shadow: 
            0 30px 60px rgba(0,0,0,0.3),
            0 0 0 15px rgba(102, 126, 234, 0.2),
            0 0 80px rgba(102, 126, 234, 0.5) inset;
    }
    
    .emoji-badge {
        position: absolute;
        top: 20px;
        right: 20px;
        width: 70px;
        height: 70px;
        background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(255,255,255,0.8));
        backdrop-filter: blur(10px);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 36px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        z-index: 10;
        border: 3px solid rgba(102, 126, 234, 0.3);
        animation: floatEmoji 4s ease-in-out infinite;
        transition: all 0.4s ease;
    }
    
    @keyframes floatEmoji {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-15px) rotate(10deg); }
    }
    
    .leader-card:hover .emoji-badge {
        transform: scale(1.3) rotate(360deg);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5);
    }
    
    .card-content {
        padding: 0 30px 30px 30px;
        text-align: center;
        position: relative;
        z-index: 5;
    }
    
    .card-content h3 {
        color: #2D3748;
        font-size: 24px;
        font-weight: 900;
        margin-bottom: 10px;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 1px;
    }
    
    .card-content .title {
        color: #667eea;
        font-size: 16px;
        font-weight: 700;
        margin-bottom: 12px;
    }
    
    .card-content .description {
        color: #4A5568;
        font-size: 13px;
        line-height: 1.6;
        margin-bottom: 20px;
    }
    
    /* Expertise tags with animation */
    .expertise-tag {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 11px;
        margin: 4px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .expertise-tag:hover {
        transform: translateY(-3px) scale(1.1);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 16px 40px;
        font-weight: 700;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        text-transform: uppercase;
        letter-spacing: 2px;
        font-family: 'Rajdhani', sans-serif;
        font-size: 15px;
    }
    
    .stButton>button:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.6);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    .chat-header {
        background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(255,255,255,0.85));
        backdrop-filter: blur(20px);
        padding: 35px;
        border-radius: 30px;
        margin-bottom: 30px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.15);
        border: 2px solid rgba(102, 126, 234, 0.2);
        animation: zoomIn 0.8s ease-out;
    }
    
    @keyframes zoomIn {
        from { opacity: 0; transform: scale(0.5); }
        to { opacity: 1; transform: scale(1); }
    }
    
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 18px 25px;
        border-radius: 25px 25px 5px 25px;
        margin: 14px 0;
        margin-left: auto;
        max-width: 70%;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        animation: slideInRight 0.5s ease-out;
    }
    
    .assistant-message {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        color: #2D3748;
        padding: 18px 25px;
        border-radius: 25px 25px 25px 5px;
        margin: 14px 0;
        max-width: 70%;
        border: 2px solid rgba(102, 126, 234, 0.2);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
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
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 25px;
        color: #2D3748;
        padding: 16px 25px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #667eea;
        box-shadow: 0 0 30px rgba(102, 126, 234, 0.3);
        transform: translateY(-2px);
    }
    
    .section-title {
        color: #2D3748;
        font-size: 2.5rem;
        font-weight: 900;
        text-align: center;
        margin: 50px 0 40px 0;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 3px;
        text-transform: uppercase;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1));
    }
    
    /* Carousel navigation */
    .carousel-nav {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin: 40px 0;
    }
    
    .carousel-dot {
        width: 15px;
        height: 15px;
        border-radius: 50%;
        background: rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .carousel-dot:hover, .carousel-dot.active {
        background: #667eea;
        transform: scale(1.3);
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.5);
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

if "carousel_page" not in st.session_state:
    st.session_state.carousel_page = 0

# Leader Selection Page
if st.session_state.selected_leader is None:
    st.markdown('<h1 class="main-title">FINANCE LEADERS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Visionaries Who Changed the World</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="greeting-box">
        <p style="color: #2D3748; font-size: 1.3rem; font-weight: 700; margin: 0; font-family: 'Rajdhani', sans-serif; letter-spacing: 2px;">
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
    
    # Display 5 leaders per page with 3D cards
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
                st.markdown(f'<div class="leader-card" style="animation-delay: {idx * 0.1}s;">', unsafe_allow_html=True)
                st.markdown(f'<div class="emoji-badge">{leader["emoji"]}</div>', unsafe_allow_html=True)
                
                st.markdown('<div class="profile-image-wrapper">', unsafe_allow_html=True)
                if os.path.exists(leader['image']):
                    st.image(leader['image'], width=200)
                else:
                    st.markdown(f"""
                    <div style="width: 200px; height: 200px; background: {leader['gradient']}; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 80px; border: 5px solid white; box-shadow: 0 20px 40px rgba(0,0,0,0.2);">
                        {leader['emoji']}
                    </div>
                    """, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class="card-content">
                    <h3>{leader_name}</h3>
                    <p class="title">{leader['title']}</p>
                    <p class="description">{leader['description']}</p>
                    <div style="margin-bottom: 20px;">
                        {''.join([f'<span class="expertise-tag">{skill}</span>' for skill in leader['expertise'][:2]])}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                if st.button("Start Chat", key=f"btn_{leader_idx}", width='stretch'):
                    st.session_state.selected_leader = leader_name
                    st.rerun()
    
    # Carousel dots
    st.markdown("""
    <div class="carousel-nav">
        <div class="carousel-dot {}"></div>
        <div class="carousel-dot {}"></div>
    </div>
    """.format("active" if st.session_state.carousel_page == 0 else "", 
               "active" if st.session_state.carousel_page == 1 else ""), 
    unsafe_allow_html=True)

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
                <div style="width: 90px; height: 90px; background: {leader['gradient']}; border-radius: 25px; display: flex; align-items: center; justify-content: center; font-size: 48px; border: 3px solid rgba(102, 126, 234, 0.3); box-shadow: 0 10px 30px rgba(0,0,0,0.2); animation: float 3s ease-in-out infinite;">
                    {leader['emoji']}
                </div>
                <div>
                    <h2 style="color: #2D3748; margin: 0; font-size: 38px; font-weight: 900; font-family: 'Orbitron', sans-serif;">{leader_name}</h2>
                    <p style="color: #667eea; margin: 10px 0; font-size: 18px; font-weight: 700;">{leader['title']}</p>
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

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 30px;">
        <div style="font-size: 80px; margin-bottom: 25px; animation: float 3s ease-in-out infinite;">💼</div>
        <h2 style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 900; font-size: 32px; letter-spacing: 3px; font-family: 'Orbitron', sans-serif;">FINANCE<br>LEADERS</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="background: rgba(255, 255, 255, 0.8); padding: 25px; border-radius: 20px; border: 2px solid rgba(102, 126, 234, 0.2); margin-bottom: 25px; box-shadow: 0 5px 25px rgba(0, 0, 0, 0.1);">
        <h3 style="color: #2D3748; font-weight: 800; margin-bottom: 18px; font-size: 22px; font-family: 'Orbitron', sans-serif;">About</h3>
        <p style="color: #4A5568; line-height: 1.9; font-weight: 500; font-size: 14px;">
            Connect with 10 inspiring women leaders and learn from their unique perspectives on finance, business, and leadership through AI-powered conversations.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="background: rgba(255, 255, 255, 0.8); padding: 25px; border-radius: 20px; border: 2px solid rgba(102, 126, 234, 0.2); box-shadow: 0 5px 25px rgba(0, 0, 0, 0.1);">
        <h3 style="color: #2D3748; font-weight: 800; margin-bottom: 18px; font-size: 22px; font-family: 'Orbitron', sans-serif;">Features</h3>
        <ul style="color: #4A5568; line-height: 2.3; font-weight: 500; font-size: 14px; padding-left: 20px;">
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
    <div style="text-align: center; padding: 22px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; border: 2px solid rgba(255, 255, 255, 0.3); box-shadow: 0 8px 30px rgba(102, 126, 234, 0.4);">
        <p style="color: white; font-weight: 800; margin: 0; font-size: 16px; letter-spacing: 1px; font-family: 'Rajdhani', sans-serif;">
            POWERED BY OPENAI GPT-3.5
        </p>
    </div>
    """, unsafe_allow_html=True)
