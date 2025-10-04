import streamlit as st
from openai import OpenAI
import os

# OpenAI API Key
OPENAI_API_KEY = "YOUR_API_KEY_HERE"
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

# Custom CSS for light blue glowing background and pop-up cards
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');

.stApp {
    background: linear-gradient(-45deg, #B3E5FC, #E1F5FE, #81D4FA, #B3E5FC);
    background-size: 400% 400%;
    animation: gradientShift 20s ease infinite;
}

@keyframes gradientShift {
    0%,100% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
}

.main-title {
    text-align:center;
    font-size:4rem;
    font-weight:900;
    background: linear-gradient(135deg,#667eea,#764ba2,#f093fb);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    animation: pulse 3s ease-in-out infinite;
    letter-spacing:5px;
    font-family:'Orbitron',sans-serif;
}

@keyframes pulse {
    0%,100%{transform:scale(1);}
    50%{transform:scale(1.02);}
}

.leader-card {
    background:white;
    border-radius:25px;
    border:3px solid rgba(102,126,234,0.2);
    box-shadow:0 20px 60px rgba(0,0,0,0.15);
    transition: all 0.6s cubic-bezier(0.175,0.885,0.32,1.275);
    cursor:pointer;
    transform-style:preserve-3d;
    perspective:1000px;
    margin-bottom:30px;
}

.leader-card:hover {
    transform: translateY(-20px) scale(1.08);
    box-shadow:0 40px 80px rgba(102,126,234,0.4),0 0 60px rgba(102,126,234,0.3) inset;
}

.profile-image-wrapper {display:flex;justify-content:center;padding:20px;}
.profile-image {width:180px;height:180px;border-radius:50%;object-fit:cover;border:5px solid white;box-shadow:0 20px 40px rgba(0,0,0,0.2);}
.card-content {text-align:center;padding:10px;}
.card-content h3 {font-family:'Orbitron',sans-serif;font-weight:900;margin-bottom:5px;}
.card-content .title {color:#667eea;font-weight:700;font-size:14px;margin-bottom:10px;}
.card-content .description {color:#4A5568;font-size:13px;margin-bottom:10px;}
.expertise-tag {display:inline-block;background:#E0F2FF;color:#0A5276;padding:4px 10px;margin:2px;border-radius:12px;font-size:12px;}
</style>
""", unsafe_allow_html=True)

# Main Title
st.markdown('<h1 class="main-title">Finance Leaders AI Chat 💼</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center;font-size:16px;color:#333;'>Click a card to chat with a leader about finance, investing, or strategy!</p>", unsafe_allow_html=True)

# Display leaders in 3 columns
cols = st.columns(3)
for i, (name, info) in enumerate(leaders.items()):
    with cols[i % 3]:
        if st.button(f"{info['emoji']} {name}", key=name):
            st.session_state['selected_leader'] = name
        st.markdown(f"""
        <div class="leader-card">
            <div class="profile-image-wrapper">
                <img class="profile-image" src="{info['image']}" />
            </div>
            <div class="card-content">
                <h3>{name}</h3>
                <div class="title">{info['title']}</div>
                <div class="description">{info['description']}</div>
                {" ".join([f'<span class="expertise-tag">{topic}</span>' for topic in info['topics']])}
            </div>
        </div>
        """, unsafe_allow_html=True)

# Chat interface
if 'selected_leader' in st.session_state:
    leader = st.session_state['selected_leader']
    st.subheader(f"Chat with {leader}")
    user_input = st.text_input("Ask a question:")
    if user_input:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": f"You are {leader}, a finance expert. Answer the user's questions in your expertise style."},
                {"role": "user", "content": user_input}
            ]
        )
        st.markdown(f"**{leader}:** {response.choices[0].message['content']}")

