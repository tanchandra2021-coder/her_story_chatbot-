import streamlit as st
import openai
from openai import OpenAI
import os

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
        "gradient": "from-rose-400 via-pink-500 to-purple-500"
    },
    "Angela Merkel": {
        "title": "Economic Policy Expert",
        "description": "Analytical approach to fiscal policy, European economics, and strategic financial planning",
        "style": "analytical and methodical",
        "expertise": ["Fiscal Policy", "European Markets", "Economic Strategy"],
        "image": "Angela_Merkel.png",
        "gradient": "from-blue-400 via-indigo-500 to-purple-500"
    },
    "Malala Yousafzai": {
        "title": "Social Finance Advocate",
        "description": "Passionate insights on funding education, microfinance, and investing in social change",
        "style": "passionate and principled",
        "expertise": ["Microfinance", "Social Bonds", "Education Funding"],
        "image": "Malala_Yousafazi.png",
        "gradient": "from-purple-400 via-fuchsia-500 to-pink-500"
    },
    "Ruth Bader Ginsburg": {
        "title": "Financial Law & Ethics",
        "description": "Precise guidance on financial regulations, investment law, and ethical wealth management",
        "style": "precise and principled",
        "expertise": ["Financial Law", "Securities", "Compliance"],
        "image": "Ruth_Bader_Ginsburg.png",
        "gradient": "from-amber-400 via-orange-500 to-red-500"
    },
    "Indra Nooyi": {
        "title": "Corporate Finance Leader",
        "description": "Strategic insights on corporate finance, M&A, sustainable business growth, and CFO excellence",
        "style": "strategic and visionary",
        "expertise": ["Corporate Finance", "M&A", "Business Strategy"],
        "image": "Indra_Nooyi.png",
        "gradient": "from-emerald-400 via-teal-500 to-cyan-500"
    },
    "Sheryl Sandberg": {
        "title": "Tech Finance Executive",
        "description": "Data-driven approach to tech valuations, scaling startups, and financial operations",
        "style": "analytical and motivational",
        "expertise": ["Tech Finance", "Scaling", "Operations"],
        "image": "Sheryl_Sandberg.png",
        "gradient": "from-cyan-400 via-blue-500 to-indigo-500"
    },
    "Jacinda Ardern": {
        "title": "Wellbeing Economics",
        "description": "Compassionate approach to budget management, public finance, and wellbeing economics",
        "style": "empathetic and pragmatic",
        "expertise": ["Public Finance", "Budget Policy", "Wellbeing Economy"],
        "image": "Jacinda_Ardern.png",
        "gradient": "from-red-400 via-pink-500 to-rose-500"
    },
    "Mae Jemison": {
        "title": "STEM Finance Pioneer",
        "description": "Innovative thinking on R&D funding, STEM investment, and technology venture capital",
        "style": "innovative and scientific",
        "expertise": ["Venture Capital", "R&D Finance", "Tech Investment"],
        "image": "Mae_Jemison.png",
        "gradient": "from-violet-400 via-purple-500 to-indigo-500"
    },
    "Reshma Saujani": {
        "title": "Startup Finance Advocate",
        "description": "Bold approach to fundraising, startup equity, and building financial resilience in tech",
        "style": "bold and resourceful",
        "expertise": ["Fundraising", "Startup Equity", "Angel Investing"],
        "image": "Reshman_Saujani.png",
        "gradient": "from-fuchsia-400 via-pink-500 to-purple-500"
    },
    "Sara Blakely": {
        "title": "Bootstrap Finance Expert",
        "description": "Self-made approach to bootstrapping businesses, cash flow management, and building wealth",
        "style": "creative and determined",
        "expertise": ["Bootstrapping", "Cash Flow", "Wealth Building"],
        "image": "Sara_Blakely.png",
        "gradient": "from-rose-400 via-red-500 to-orange-500"
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
# 💅 Custom CSS Styling
# -------------------
st.markdown("""
<style>
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
    }
    
    /* Card styling */
    .leader-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        transition: all 0.3s ease;
        cursor: pointer;
        height: 100%;
        overflow: hidden;
    }
    
    .leader-card:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: rgba(255, 255, 255, 0.3);
        box-shadow: 0 20px 60px rgba(168, 85, 247, 0.4);
    }
    
    .leader-image {
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 16px;
        margin-bottom: 16px;
        border: 3px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Chat message styling */
    .user-message {
        background: linear-gradient(135deg, #a855f7, #ec4899);
        color: white;
        padding: 16px 20px;
        border-radius: 20px;
        margin: 10px 0;
        margin-left: auto;
        max-width: 70%;
        box-shadow: 0 4px 20px rgba(168, 85, 247, 0.3);
    }
    
    .assistant-message {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        color: white;
        padding: 16px 20px;
        border-radius: 20px;
        margin: 10px 0;
        max-width: 70%;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Title styling */
    .main-title {
        text-align: center;
        font-size: 4rem;
        font-weight: 800;
        color: white;
        margin-bottom: 10px;
        text-shadow: 0 0 40px rgba(168, 85, 247, 0.5);
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.5rem;
        color: #c084fc;
        margin-bottom: 40px;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #a855f7, #ec4899);
        color: white;
        border: none;
        border-radius: 16px;
        padding: 12px 28px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(168, 85, 247, 0.4);
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 30px rgba(168, 85, 247, 0.6);
    }
    
    /* Input styling */
    .stTextInput>div>div>input {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border: 2px solid rgba(255, 255, 255, 0.2);
        border-radius: 16px;
        color: white;
        padding: 12px 20px;
        font-size: 16px;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #a855f7;
        box-shadow: 0 0 20px rgba(168, 85, 247, 0.5);
    }
    
    /* Expertise tags */
    .expertise-tag {
        display: inline-block;
        background: rgba(255, 255, 255, 0.15);
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 12px;
        color: #c084fc;
        margin: 4px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Header styling */
    .chat-header {
        background: linear-gradient(135deg, #a855f7, #ec4899);
        padding: 24px;
        border-radius: 16px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px rgba(168, 85, 247, 0.4);
    }
    
    /* Leader header image in chat */
    .chat-leader-image {
        width: 70px;
        height: 70px;
        object-fit: cover;
        border-radius: 16px;
        border: 3px solid rgba(255, 255, 255, 0.4);
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

# -------------------
# 🏠 Leader Selection Page
# -------------------
if st.session_state.selected_leader is None:
    # Hero Section
    st.markdown('<h1 class="main-title">💼 Finance Leaders</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Learn from Visionaries Who Changed the World</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #c084fc; margin-bottom: 50px;">Select a leader to explore their financial expertise</p>', unsafe_allow_html=True)
    
    # First Row - 5 Leaders
    cols1 = st.columns(5, gap="medium")
    leader_names = list(leaders.keys())
    
    for idx, col in enumerate(cols1):
        if idx < len(leader_names):
            leader_name = leader_names[idx]
            leader = leaders[leader_name]
            
            with col:
                # Try to load image, fall back to emoji if not found
                try:
                    if os.path.exists(leader['image']):
                        st.image(leader['image'], use_container_width=True)
                    else:
                        st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 16px;">
                            <div style="width: 100%; height: 180px; background: linear-gradient(135deg, #a855f7, #ec4899); border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 80px; border: 3px solid rgba(255, 255, 255, 0.2);">
                                💼
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                except:
                    st.markdown(f"""
                    <div style="text-align: center; margin-bottom: 16px;">
                        <div style="width: 100%; height: 180px; background: linear-gradient(135deg, #a855f7, #ec4899); border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 80px; border: 3px solid rgba(255, 255, 255, 0.2);">
                            💼
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class="leader-card" style="padding-top: 0;">
                    <h3 style="color: white; font-size: 18px; font-weight: bold; margin-bottom: 8px;">{leader_name}</h3>
                    <p style="color: #c084fc; font-size: 13px; margin-bottom: 12px;">📊 {leader['title']}</p>
                    <p style="color: #e9d5ff; font-size: 12px; line-height: 1.5; margin-bottom: 16px;">{leader['description'][:80]}...</p>
                    <div style="margin-bottom: 16px;">
                        {''.join([f'<span class="expertise-tag">{skill}</span>' for skill in leader['expertise'][:2]])}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"Chat with {leader_name.split()[0]}", key=f"btn_{idx}", use_container_width=True):
                    st.session_state.selected_leader = leader_name
                    st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Second Row - 5 Leaders
    cols2 = st.columns(5, gap="medium")
    
    for idx, col in enumerate(cols2):
        actual_idx = idx + 5
        if actual_idx < len(leader_names):
            leader_name = leader_names[actual_idx]
            leader = leaders[leader_name]
            
            with col:
                # Try to load image, fall back to emoji if not found
                try:
                    if os.path.exists(leader['image']):
                        st.image(leader['image'], use_container_width=True)
                    else:
                        st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 16px;">
                            <div style="width: 100%; height: 180px; background: linear-gradient(135deg, #10b981, #06b6d4); border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 80px; border: 3px solid rgba(255, 255, 255, 0.2);">
                                💼
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                except:
                    st.markdown(f"""
                    <div style="text-align: center; margin-bottom: 16px;">
                        <div style="width: 100%; height: 180px; background: linear-gradient(135deg, #10b981, #06b6d4); border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 80px; border: 3px solid rgba(255, 255, 255, 0.2);">
                            💼
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class="leader-card" style="padding-top: 0;">
                    <h3 style="color: white; font-size: 18px; font-weight: bold; margin-bottom: 8px;">{leader_name}</h3>
                    <p style="color: #c084fc; font-size: 13px; margin-bottom: 12px;">📊 {leader['title']}</p>
                    <p style="color: #e9d5ff; font-size: 12px; line-height: 1.5; margin-bottom: 16px;">{leader['description'][:80]}...</p>
                    <div style="margin-bottom: 16px;">
                        {''.join([f'<span class="expertise-tag">{skill}</span>' for skill in leader['expertise'][:2]])}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"Chat with {leader_name.split()[0]}", key=f"btn_{actual_idx}", use_container_width=True):
                    st.session_state.selected_leader = leader_name
                    st.rerun()
    
    # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; padding: 30px;">
        <div style="display: inline-flex; align-items: center; gap: 12px; background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(20px); padding: 16px 32px; border-radius: 50px; border: 1px solid rgba(255, 255, 255, 0.1);">
            <span style="font-size: 20px;">✨</span>
            <span style="color: #c084fc; font-weight: 600;">Powered by financial wisdom and leadership excellence</span>
            <span style="font-size: 20px;">📈</span>
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
        # Try to show leader image in header
        try:
            if os.path.exists(leader['image']):
                image_html = f'<img src="data:image/png;base64,{st.image(leader["image"], width=70)}" class="chat-leader-image" style="display: none;">'
                # Use file path directly
                st.markdown(f"""
                <div class="chat-header">
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div style="width: 70px; height: 70px; background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(10px); border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 36px; border: 3px solid rgba(255, 255, 255, 0.4); overflow: hidden;">
                            💼
                        </div>
                        <div>
                            <h2 style="color: white; margin: 0; font-size: 28px; font-weight: bold;">{leader_name}</h2>
                            <p style="color: rgba(255, 255, 255, 0.9); margin: 4px 0; font-size: 16px; font-weight: 500;">{leader['title']}</p>
                            <div style="margin-top: 8px;">
                                {''.join([f'<span style="background: rgba(255, 255, 255, 0.25); padding: 4px 12px; border-radius: 20px; font-size: 13px; color: white; margin-right: 8px; border: 1px solid rgba(255, 255, 255, 0.3);">{skill}</span>' for skill in leader['expertise']])}
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                raise FileNotFoundError
        except:
            st.markdown(f"""
            <div class="chat-header">
                <div style="display: flex; align-items: center; gap: 20px;">
                    <div style="width: 70px; height: 70px; background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(10px); border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 36px; border: 3px solid rgba(255, 255, 255, 0.4);">
                        💼
                    </div>
                    <div>
                        <h2 style="color: white; margin: 0; font-size: 28px; font-weight: bold;">{leader_name}</h2>
                        <p style="color: rgba(255, 255, 255, 0.9); margin: 4px 0; font-size: 16px; font-weight: 500;">{leader['title']}</p>
                        <div style="margin-top: 8px;">
                            {''.join([f'<span style="background: rgba(255, 255, 255, 0.25); padding: 4px 12px; border-radius: 20px; font-size: 13px; color: white; margin-right: 8px; border: 1px solid rgba(255, 255, 255, 0.3);">{skill}</span>' for skill in leader['expertise']])}
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
    
    # Chat Input
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([6, 1])
    
    with col1:
        user_input = st.text_input(
            "Message",
            placeholder=f"Ask {leader_name} about {leader['expertise'][0].lower()}...",
            key="user_input",
            label_visibility="collapsed"
        )
    
    with col2:
        send_button = st.button("Send 📤", use_container_width=True)
    
    # Process Message
    if send_button and user_input:
        # Add user message
        st.session_state.messages[leader_name].append({"role": "user", "content": user_input})
        
        # Get AI response
        with st.spinner(f"{leader_name} is thinking..."):
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
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
        
        st.rerun()

# -------------------
# 📊 Sidebar Info (Optional)
# -------------------
with st.sidebar:
    st.markdown("### 💼 About")
    st.markdown("Connect with 10 inspiring women leaders and learn from their unique perspectives on finance, business, and leadership.")
    st.markdown("---")
    st.markdown("### 🎯 Features")
    st.markdown("- Personalized financial advice")
    st.markdown("- Expert insights from diverse fields")
    st.markdown("- Real-time AI conversations")
    st.markdown("---")
    st.markdown("**Powered by OpenAI GPT-3.5**")
