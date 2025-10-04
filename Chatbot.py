import streamlit as st
from openai import OpenAI
import os
from PIL import Image

# SECURITY WARNING: Remove this API key and use environment variables instead!
OPENAI_API_KEY = "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"
client = OpenAI(api_key=OPENAI_API_KEY)

leaders = {
    "Michelle Obama": {
        "title": "Education & Social Impact",
        "specialty": "Passionate about financial literacy through education reform and community investment strategies. Empowering communities through strategic financial planning.",
        "emoji": "📚",
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
    
    .curved-greeting {
        text-align: center;
        font-size: 1.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #E91E63, #9C27B0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 30px;
        font-family: 'Playfair Display', serif;
        letter-spacing: 1px;
    }
    
    .leader-name-display {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800;
        color: #2D3748;
        margin: 20px 0 10px;
        font-family: 'Playfair Display', serif;
    }
    
    .leader-title-display {
        text-align: center;
        font-size: 1.2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #E91E63, #9C27B0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 20px;
    }
    
    .leader-specialty-display {
        text-align: center;
        font-size: 1rem;
        color: #4A5568;
        line-height: 1.7;
        margin: 0 auto 25px;
        max-width: 550px;
        font-weight: 500;
    }
    
    .expertise-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        flex-wrap: wrap;
        margin-bottom: 30px;
    }
    
    .expertise-tag {
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
    
    div[data-testid="stImage"] {
        display: flex;
        justify-content: center;
        margin: 30px auto;
    }
    
    div[data-testid="stImage"] > img {
        border-radius: 50% !important;
        border: 6px solid white !important;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.2), 0 0 0 12px rgba(233, 30, 99, 0.15) !important;
        animation: popIn 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
        max-width: 240px !important;
        max-height: 240px !important;
        width: 240px !important;
        height: 240px !important;
        object-fit: cover !important;
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
        font-family: 'Poppins', sans-serif !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05) !important;
        box-shadow: 0 15px 40px rgba(233, 30, 99, 0.5) !important;
    }
    
    div[data-testid="column"] button[kind="secondary"] {
        background: linear-gradient(135deg, #E91E63, #9C27B0) !important;
        border: none !important;
        border-radius: 50% !important;
        width: 60px !important;
        height: 60px !important;
        min-width: 60px !important;
        min-height: 60px !important;
        font-size: 24px !important;
        color: white !important;
        box-shadow: 0 8px 25px rgba(233, 30, 99, 0.4) !important;
        transition: all 0.3s ease !important;
        padding: 0 !important;
    }
    
    div[data-testid="column"] button[kind="secondary"]:hover {
        transform: scale(1.15) !important;
        box-shadow: 0 12px 35px rgba(233, 30, 99, 0.6) !important;
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
        if st.button("←", key="prev_btn", type="secondary"):
            st.session_state.current_index = (st.session_state.current_index - 1) % len(leaders_list)
            st.rerun()
    
    with col2:
        current_name = leaders_list[st.session_state.current_index]
        leader = leaders[current_name]
        first_name = current_name.split()[0]
        
        # Create card container
        card_container = st.container()
        with card_container:
            # Curved greeting
            st.markdown(f'<p class="curved-greeting">Hi, I\'m {first_name}. Let\'s Chat!</p>', unsafe_allow_html=True)
            
            # Profile image
            try:
                if os.path.exists(leader['image']):
                    img = Image.open(leader['image'])
                    st.image(img, width=240, use_container_width=False)
                else:
                    st.markdown(f"""
                    <div style="display: flex; justify-content: center; margin: 30px auto;">
                        <div style="width: 240px; height: 240px; border-radius: 50%; background: linear-gradient(135deg, #E91E63, #9C27B0); display: flex; align-items: center; justify-content: center; font-size: 100px; border: 6px solid white; box-shadow: 0 20px 50px rgba(0, 0, 0, 0.2), 0 0 0 12px rgba(233, 30, 99, 0.15);">
                            👩
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            except:
                st.markdown(f"""
                <div style="display: flex; justify-content: center; margin: 30px auto;">
                    <div style="width: 240px; height: 240px; border-radius: 50%; background: linear-gradient(135deg, #E91E63, #9C27B0); display: flex; align-items: center; justify-content: center; font-size: 100px; border: 6px solid white; box-shadow: 0 20px 50px rgba(0, 0, 0, 0.2), 0 0 0 12px rgba(233, 30, 99, 0.15);">
                    👩
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            # Leader info
            st.markdown(f'<h2 class="leader-name-display">{current_name}</h2>', unsafe_allow_html=True)
            st.markdown(f'<p class="leader-title-display">{leader["title"]} {leader["emoji"]}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="leader-specialty-display">{leader["specialty"]}</p>', unsafe_allow_html=True)
            
            # Expertise tags
            tags_html = '<div class="expertise-container">'
            for exp in leader['expertise']:
                tags_html += f'<span class="expertise-tag">{exp}</span>'
            tags_html += '</div>'
            st.markdown(tags_html, unsafe_allow_html=True)
            
            # Start chatting button
            if st.button("Start Chatting", key="start_chat", use_container_width=True):
                st.session_state.selected_leader = current_name
                st.rerun()
    
    with col3:
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
