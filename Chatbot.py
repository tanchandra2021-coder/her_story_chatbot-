import streamlit as st
from openai import OpenAI
import os
from PIL import Image
import base64
from io import BytesIO

# SECURITY WARNING: Remove this API key and use environment variables instead!
OPENAI_API_KEY = "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"
client = OpenAI(api_key=OPENAI_API_KEY)

leaders = {
    "Michelle Obama": {
        "title": "Education & Social Impact",
        "specialty": "Passionate about financial literacy through education reform and community investment strategies. Empowering communities through strategic financial planning.",
        "emoji": "🎓",
        "style": "inspiring",
        "expertise": ["Impact Investing", "Education Finance"],
        "image": "michelle_obama.png"
    },
    "Angela Merkel": {
        "title": "Economic Policy Expert",
        "specialty": "Analytical approach to fiscal policy, European economics, and strategic financial planning. Bringing decades of economic leadership experience.",
        "emoji": "📊",
        "style": "analytical",
        "expertise": ["Fiscal Policy", "Economic Strategy"],
        "image": "Angela_Merkel.png"
    },
    "Malala Yousafzai": {
        "title": "Social Finance Advocate",
        "specialty": "Passionate insights on funding education, microfinance, and investing in social change. Championing financial empowerment for all.",
        "emoji": "🌍",
        "style": "passionate",
        "expertise": ["Microfinance", "Social Bonds"],
        "image": "Malala_Yousafazi.png"
    },
    "Ruth Bader Ginsburg": {
        "title": "Financial Law & Ethics",
        "specialty": "Precise guidance on financial regulations, investment law, and ethical wealth management. Justice in every financial decision.",
        "emoji": "⚖️",
        "style": "precise",
        "expertise": ["Financial Law", "Securities"],
        "image": "Ruth_Bader_Ginsburg.png"
    },
    "Indra Nooyi": {
        "title": "Corporate Finance Leader",
        "specialty": "Strategic insights on corporate finance, M&A, sustainable business growth, and CFO excellence. Transforming businesses through financial innovation.",
        "emoji": "💼",
        "style": "strategic",
        "expertise": ["Corporate Finance", "M&A"],
        "image": "Indra_Nooyi.png"
    },
    "Sheryl Sandberg": {
        "title": "Tech Finance Executive",
        "specialty": "Data-driven approach to tech valuations, scaling startups, and financial operations. Building the future of tech finance.",
        "emoji": "💻",
        "style": "analytical",
        "expertise": ["Tech Finance", "Scaling"],
        "image": "Sheryl_Sandberg.png"
    },
    "Jacinda Ardern": {
        "title": "Wellbeing Economics",
        "specialty": "Compassionate approach to budget management, public finance, and wellbeing economics. Putting people at the center of financial policy.",
        "emoji": "🌱",
        "style": "empathetic",
        "expertise": ["Public Finance", "Budget Policy"],
        "image": "Jacinda_Ardern.png"
    },
    "Mae Jemison": {
        "title": "STEM Finance Pioneer",
        "specialty": "Innovative thinking on R&D funding, STEM investment, and technology venture capital. Pioneering the frontier of innovation finance.",
        "emoji": "🚀",
        "style": "innovative",
        "expertise": ["Venture Capital", "R&D Finance"],
        "image": "Mae_Jemison.png"
    },
    "Reshma Saujani": {
        "title": "Startup Finance Advocate",
        "specialty": "Bold approach to fundraising, startup equity, and building financial resilience in tech. Breaking barriers in venture capital.",
        "emoji": "💪",
        "style": "bold",
        "expertise": ["Fundraising", "Startup Equity"],
        "image": "Reshman_Saujani.png"
    },
    "Sara Blakely": {
        "title": "Bootstrap Finance Expert",
        "specialty": "Self-made approach to bootstrapping businesses, cash flow management, and building wealth. Turning ideas into billion-dollar businesses.",
        "emoji": "✨",
        "style": "creative",
        "expertise": ["Bootstrapping", "Cash Flow"],
        "image": "Sara_Blakely.png"
    }
}

def get_image_base64(image_path):
    """Convert image to base64 for embedding in HTML"""
    try:
        with Image.open(image_path) as img:
            # Convert to RGBA to handle transparency
            img = img.convert("RGBA")
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            return f"data:image/png;base64,{img_str}"
    except:
        return None

st.set_page_config(page_title="HerStory", page_icon="👩", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Poppins:wght@400;500;600;700&display=swap');
    
    #MainMenu, footer, header {visibility: hidden;}
    
    .stApp {
        background: linear-gradient(135deg, #FFF5F7 0%, #FFE5F0 25%, #F0F8FF 50%, #FFF8F0 75%, #F5F0FF 100%);
        background-size: 400% 400%;
        animation: bgFlow 20s ease infinite;
        font-family: 'Poppins', sans-serif;
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
        background-clip: text;
        margin: 40px 0 60px;
        letter-spacing: 2px;
        animation: titleFloat 3s ease-in-out infinite;
    }
    
    @keyframes titleFloat {
        0%, 100% {transform: translateY(0px);}
        50% {transform: translateY(-8px);}
    }
    
    .carousel-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 40px;
        padding: 20px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .arrow-button {
        background: linear-gradient(135deg, #E91E63, #9C27B0);
        border: none;
        border-radius: 50%;
        width: 70px;
        height: 70px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: 0 10px 35px rgba(233, 30, 99, 0.4);
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        color: white;
        font-size: 28px;
        font-weight: bold;
    }
    
    .arrow-button:hover {
        transform: scale(1.15);
        box-shadow: 0 15px 45px rgba(233, 30, 99, 0.6);
    }
    
    .leader-card {
        background: white;
        border-radius: 45px;
        padding: 50px 60px 60px;
        box-shadow: 0 25px 70px rgba(0, 0, 0, 0.15);
        max-width: 650px;
        width: 100%;
        position: relative;
        border: 3px solid rgba(233, 30, 99, 0.2);
        animation: cardSlideIn 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    @keyframes cardSlideIn {
        0% {
            opacity: 0;
            transform: translateX(100px) scale(0.9) rotateY(20deg);
        }
        100% {
            opacity: 1;
            transform: translateX(0) scale(1) rotateY(0deg);
        }
    }
    
    .card-exit {
        animation: cardSlideOut 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55) forwards;
    }
    
    @keyframes cardSlideOut {
        0% {
            opacity: 1;
            transform: translateX(0) scale(1) rotateY(0deg);
        }
        100% {
            opacity: 0;
            transform: translateX(-100px) scale(0.9) rotateY(-20deg);
        }
    }
    
    .curved-text-container {
        position: relative;
        width: 280px;
        height: 60px;
        margin: 0 auto 20px;
    }
    
    .curved-text {
        position: absolute;
        width: 100%;
        text-align: center;
        font-size: 1.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #E91E63, #9C27B0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Playfair Display', serif;
        letter-spacing: 1px;
        transform: translateY(-10px);
    }
    
    .profile-circle-container {
        width: 280px;
        height: 280px;
        margin: 0 auto 40px;
        position: relative;
        animation: imagePopUp 0.9s cubic-bezier(0.34, 1.56, 0.64, 1);
        animation-delay: 0.2s;
        animation-fill-mode: both;
        border-radius: 0;
    }
    
    @keyframes imagePopUp {
        0% {
            opacity: 0;
            transform: scale(0) rotate(-180deg);
        }
        50% {
            transform: scale(1.15) rotate(10deg);
        }
        100% {
            opacity: 1;
            transform: scale(1) rotate(0deg);
        }
    }
    
    div[data-testid="stImage"] {
        display: flex;
        justify-content: center;
        margin: 0 auto;
    }
    
    div[data-testid="stImage"] > img {
        border: 8px solid white !important;
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.25), 0 0 0 15px rgba(233, 30, 99, 0.2) !important;
        animation: imagePopUp 0.9s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
        max-width: 280px !important;
        max-height: 280px !important;
        width: 280px !important;
        height: 280px !important;
        object-fit: cover !important;
    }
    
    .profile-glow {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, rgba(233, 30, 99, 0.3) 0%, transparent 70%);
        animation: pulse 2s ease-in-out infinite;
        z-index: 1;
    }
    
    @keyframes pulse {
        0%, 100% {
            transform: translate(-50%, -50%) scale(1);
            opacity: 0.6;
        }
        50% {
            transform: translate(-50%, -50%) scale(1.1);
            opacity: 0.8;
        }
    }
    
    .leader-name-text {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 900;
        color: #2D3748;
        margin: 0 0 12px 0;
        font-family: 'Playfair Display', serif;
        animation: fadeInUp 0.6s ease-out;
        animation-delay: 0.4s;
        animation-fill-mode: both;
    }
    
    .leader-title-text {
        text-align: center;
        font-size: 1.3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #E91E63, #9C27B0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0 0 25px 0;
        animation: fadeInUp 0.6s ease-out;
        animation-delay: 0.5s;
        animation-fill-mode: both;
    }
    
    .leader-specialty-text {
        text-align: center;
        font-size: 1.05rem;
        color: #4A5568;
        line-height: 1.8;
        margin: 0 auto 30px;
        max-width: 520px;
        font-weight: 500;
        animation: fadeInUp 0.6s ease-out;
        animation-delay: 0.6s;
        animation-fill-mode: both;
    }
    
    @keyframes fadeInUp {
        0% {
            opacity: 0;
            transform: translateY(20px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .expertise-tags-container {
        display: flex;
        justify-content: center;
        gap: 12px;
        flex-wrap: wrap;
        margin-bottom: 35px;
        animation: fadeInUp 0.6s ease-out;
        animation-delay: 0.7s;
        animation-fill-mode: both;
    }
    
    .expertise-tag {
        background: linear-gradient(135deg, #E91E63, #9C27B0);
        color: white;
        padding: 10px 24px;
        border-radius: 25px;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        box-shadow: 0 6px 20px rgba(233, 30, 99, 0.35);
        transition: all 0.3s ease;
    }
    
    .expertise-tag:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 10px 30px rgba(233, 30, 99, 0.5);
    }
    
    .start-button-container {
        animation: fadeInUp 0.6s ease-out;
        animation-delay: 0.8s;
        animation-fill-mode: both;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #E91E63, #9C27B0) !important;
        color: white !important;
        border: none !important;
        border-radius: 35px !important;
        padding: 18px 50px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
        box-shadow: 0 12px 35px rgba(233, 30, 99, 0.4) !important;
        font-family: 'Poppins', sans-serif !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-4px) scale(1.05) !important;
        box-shadow: 0 18px 45px rgba(233, 30, 99, 0.6) !important;
    }
    
    div[data-testid="column"] button[kind="secondary"] {
        background: linear-gradient(135deg, #E91E63, #9C27B0) !important;
        border: none !important;
        border-radius: 50% !important;
        width: 70px !important;
        height: 70px !important;
        min-width: 70px !important;
        min-height: 70px !important;
        font-size: 28px !important;
        color: white !important;
        box-shadow: 0 10px 35px rgba(233, 30, 99, 0.4) !important;
        transition: all 0.3s ease !important;
        padding: 0 !important;
        font-weight: bold !important;
    }
    
    div[data-testid="column"] button[kind="secondary"]:hover {
        transform: scale(1.15) !important;
        box-shadow: 0 15px 45px rgba(233, 30, 99, 0.6) !important;
    }
    
    .chat-header-box {
        background: white;
        padding: 25px 30px;
        border-radius: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
        border: 2px solid rgba(233, 30, 99, 0.2);
        display: flex;
        align-items: center;
        gap: 20px;
    }
    
    .chat-avatar {
        width: 70px;
        height: 70px;
        background: linear-gradient(135deg, #E91E63, #9C27B0);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 36px;
        border: 4px solid white;
        box-shadow: 0 6px 20px rgba(233, 30, 99, 0.3);
        flex-shrink: 0;
    }
    
    .chat-info h2 {
        color: #2D3748;
        margin: 0 0 5px 0;
        font-size: 28px;
        font-weight: 900;
        font-family: 'Playfair Display', serif;
    }
    
    .chat-info p {
        background: linear-gradient(135deg, #E91E63, #9C27B0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
        font-size: 14px;
        font-weight: 700;
    }
    
    .message-container {
        display: flex;
        margin: 12px 0;
    }
    
    .message-container.user {
        justify-content: flex-end;
    }
    
    .message-container.assistant {
        justify-content: flex-start;
    }
    
    .message-bubble {
        padding: 14px 20px;
        border-radius: 20px;
        max-width: 70%;
        font-weight: 500;
        line-height: 1.5;
    }
    
    .message-bubble.user {
        background: linear-gradient(135deg, #E91E63, #9C27B0);
        color: white;
        border-radius: 20px 20px 4px 20px;
        box-shadow: 0 6px 20px rgba(233, 30, 99, 0.3);
    }
    
    .message-bubble.assistant {
        background: white;
        color: #2D3748;
        border-radius: 20px 20px 20px 4px;
        border: 2px solid rgba(233, 30, 99, 0.2);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
    }
    
    .stTextInput > div > div > input {
        background: white !important;
        border: 2px solid rgba(233, 30, 99, 0.3) !important;
        border-radius: 25px !important;
        padding: 14px 20px !important;
        font-size: 15px !important;
        font-family: 'Poppins', sans-serif !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #E91E63 !important;
        box-shadow: 0 0 25px rgba(233, 30, 99, 0.25) !important;
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
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        if st.button("←", key="prev_btn", type="secondary"):
            st.session_state.current_index = (st.session_state.current_index - 1) % len(leaders_list)
            st.rerun()
    
    with col2:
        current_name = leaders_list[st.session_state.current_index]
        leader = leaders[current_name]
        first_name = current_name.split()[0]
        
        # Start card
        st.markdown('<div class="leader-card">', unsafe_allow_html=True)
        
        # Curved text
        st.markdown(f'''
            <div class="curved-text-container">
                <p class="curved-text">Hi, I'm {first_name}. Let's Chat!</p>
            </div>
        ''', unsafe_allow_html=True)
        
        # Profile image container - opening tags
        st.markdown('<div class="profile-circle-container"><div class="profile-glow"></div>', unsafe_allow_html=True)
        
        # Try to load and display the image
        try:
            if os.path.exists(leader['image']):
                img = Image.open(leader['image'])
                # Create a container with custom styling
                st.markdown('<div style="display: flex; justify-content: center;">', unsafe_allow_html=True)
                st.image(img, use_container_width=False, width=280)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'''
                    <div style="width: 280px; height: 280px; margin: 0 auto; background: linear-gradient(135deg, #E91E63, #9C27B0); display: flex; align-items: center; justify-content: center; font-size: 120px; border: 8px solid white; box-shadow: 0 25px 60px rgba(0, 0, 0, 0.25), 0 0 0 15px rgba(233, 30, 99, 0.2);">
                        👩
                    </div>
                ''', unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f'''
                <div style="width: 280px; height: 280px; margin: 0 auto; background: linear-gradient(135deg, #E91E63, #9C27B0); display: flex; align-items: center; justify-content: center; font-size: 120px; border: 8px solid white; box-shadow: 0 25px 60px rgba(0, 0, 0, 0.25), 0 0 0 15px rgba(233, 30, 99, 0.2);">
                    👩
                </div>
            ''', unsafe_allow_html=True)
        
        # Close profile container
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Leader info
        st.markdown(f'<h2 class="leader-name-text">{current_name}</h2>', unsafe_allow_html=True)
        st.markdown(f'<p class="leader-title-text">{leader["title"]} {leader["emoji"]}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="leader-specialty-text">{leader["specialty"]}</p>', unsafe_allow_html=True)
        
        # Expertise tags
        expertise_tags = ''.join([f'<span class="expertise-tag">{exp}</span>' for exp in leader['expertise']])
        st.markdown(f'<div class="expertise-tags-container">{expertise_tags}</div>', unsafe_allow_html=True)
        
        # Close card
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Start button
        st.markdown('<div class="start-button-container">', unsafe_allow_html=True)
        if st.button("Start Chatting", key="start_chat", use_container_width=True):
            st.session_state.selected_leader = current_name
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        if st.button("→", key="next_btn", type="secondary"):
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
        <div class="chat-header-box">
            <div class="chat-avatar">{first_name[0]}</div>
            <div class="chat-info">
                <h2>{name}</h2>
                <p>{leader['title']} {leader['emoji']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Display chat messages
    for msg in st.session_state.messages[name][1:]:
        role_class = "user" if msg["role"] == "user" else "assistant"
        st.markdown(f"""
        <div class="message-container {role_class}">
            <div class="message-bubble {role_class}">{msg["content"]}</div>
        </div>
        """, unsafe_allow_html=True)
    
    if st.session_state.typing:
        st.markdown("""
        <div class="message-container assistant">
            <div class="message-bubble assistant">💭 Thinking...</div>
        </div>
        """, unsafe_allow_html=True)
    
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
