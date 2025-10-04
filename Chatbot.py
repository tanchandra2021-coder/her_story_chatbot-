import streamlit as st
from openai import OpenAI
import os
from PIL import Image
import base64
from io import BytesIO

# WARNING: Use environment variables for API key in production!
# OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    # Fallback/security message if key is missing during local development
    st.error("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    st.stop()
    
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
        # Check if the file exists in the current directory (for testing/simplicity)
        if not os.path.exists(image_path):
            return None 
            
        with Image.open(image_path) as img:
            # Convert to RGBA to handle transparency
            img = img.convert("RGBA")
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            return f"data:image/png;base64,{img_str}"
    except Exception:
        # In a real app, you'd log the error, but here we just return None for fallback
        return None

st.set_page_config(page_title="HerStory Finance AI", page_icon="👩", layout="wide", initial_sidebar_state="collapsed")

# --- Custom CSS for Design and Animations ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Poppins:wght@400;500;600;700&display=swap');
    
    /* General Setup */
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
    }

    /* Floating Glass Card Style */
    .leader-card {
        /* Glassmorphism Effect */
        background: rgba(255, 255, 255, 0.2); /* Semi-transparent white */
        backdrop-filter: blur(20px); /* Blur the background */
        -webkit-backdrop-filter: blur(20px); /* Safari support */
        border-radius: 45px;
        padding: 50px 60px 60px;
        /* Shadow for floating effect */
        box-shadow: 0 40px 90px rgba(0, 0, 0, 0.3), 0 0 0 1px rgba(255, 255, 255, 0.3); /* Big shadow + light border */
        max-width: 650px;
        width: 100%;
        position: relative;
        overflow: hidden; /* Important for clean look */
        border: 1px solid rgba(255, 255, 255, 0.5); /* Subtle white border */
        animation: cardSlideIn 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    /* Card Entry Animation */
    @keyframes cardSlideIn {
        0% {
            opacity: 0;
            transform: translateY(50px) scale(0.9);
        }
        100% {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }
    
    /* Card Exit Animation (Solitaire Floosh Off) */
    .card-exit {
        animation: cardSlideOut 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55) forwards;
    }
    
    @keyframes cardSlideOut {
        0% {
            opacity: 1;
            transform: translate(0, 0) scale(1) rotate(0deg);
        }
        100% {
            opacity: 0;
            transform: translate(150px, -150px) scale(0.5) rotate(45deg); /* Floosh up and to the side */
        }
    }
    
    /* Curved Text and Image Layout */
    .curved-image-section {
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 40px;
    }

    .curved-text-container {
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 320px;
        height: 160px; /* Gives space for the curve */
        display: flex;
        justify-content: center;
        align-items: flex-start;
        z-index: 10;
        pointer-events: none;
    }
    
    /* This element creates the visual curve */
    .text-arc {
        position: absolute;
        top: 0;
        width: 350px;
        height: 175px;
        background: rgba(255, 255, 255, 0.5); /* Semi-transparent backing for the text */
        border-radius: 0 0 175px 175px; /* Creates the top-half-of-a-circle shape */
        border-bottom: 5px solid white;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }
    
    .curved-text {
        position: relative;
        top: 25px; /* Adjust to sit perfectly on the "curve" */
        text-align: center;
        font-size: 1.6rem;
        font-weight: 700;
        background: linear-gradient(90deg, #E91E63, #9C27B0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Playfair Display', serif;
        letter-spacing: 1px;
    }
    
    /* Image Styling */
    .profile-circle-wrapper {
        width: 280px;
        height: 280px;
        margin-top: 50px; /* Push down to clear the curved text */
        position: relative;
        z-index: 5;
    }
    
    /* Streamlit Image Container Wrapper */
    div[data-testid="stImage"] {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0 auto;
    }
    
    /* The actual image tag */
    div[data-testid="stImage"] > img {
        border-radius: 50% !important;
        border: 8px solid white !important;
        /* Updated Shadow for extra pop */
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4), 0 0 0 15px rgba(233, 30, 99, 0.1) !important; 
        max-width: 280px !important;
        max-height: 280px !important;
        width: 280px !important;
        height: 280px !important;
        object-fit: cover !important;
        /* Image Pop-In Animation */
        animation: imagePopUp 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; 
    }
    
    @keyframes imagePopUp {
        0% {
            opacity: 0;
            transform: scale(0.5) rotateY(-90deg);
        }
        100% {
            opacity: 1;
            transform: scale(1) rotateY(0deg);
        }
    }

    /* Leader Info & Text */
    .leader-name-text {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 900;
        color: #2D3748;
        margin: 0 0 8px 0;
        font-family: 'Playfair Display', serif;
        animation: fadeInUp 0.6s ease-out 0.2s both;
    }
    
    .leader-title-text {
        text-align: center;
        font-size: 1.3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #E91E63, #9C27B0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0 0 20px 0;
        animation: fadeInUp 0.6s ease-out 0.3s both;
    }
    
    .leader-specialty-text {
        text-align: center;
        font-size: 1.05rem;
        color: #4A5568;
        line-height: 1.8;
        margin: 0 auto 30px;
        max-width: 520px;
        font-weight: 500;
        animation: fadeInUp 0.6s ease-out 0.4s both;
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
    
    /* Buttons */
    div[data-testid="column"] button[kind="secondary"] {
        /* Arrow button style refined */
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
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
        padding: 0 !important;
        font-weight: bold !important;
    }
    
    div[data-testid="column"] button[kind="secondary"]:hover {
        transform: scale(1.15) !important;
        box-shadow: 0 15px 45px rgba(233, 30, 99, 0.6) !important;
    }
</style>
""", unsafe_allow_html=True)


# --- JavaScript for Card Exit Animation (Pre-Rerun) ---
# This is crucial for triggering the exit animation *before* the page reloads.
st.markdown("""
<script>
function applyExitAnimation(direction) {
    const card = document.querySelector('.leader-card');
    if (card) {
        card.classList.add('card-exit');
        if (direction === 'next') {
            card.style.animationName = 'cardSlideOut'; 
        } else {
            // Apply a reversed animation for "previous" button if desired
            card.style.animationName = 'cardSlideOutReverse'; 
        }
    }
}

// Add a slight delay before rerunning to let the animation play
function delayedRerun(index_change) {
    applyExitAnimation(index_change > 0 ? 'next' : 'prev');
    setTimeout(() => {
        const rerunButton = document.querySelector('[data-testid="stForm"] button');
        if (rerunButton) {
            rerunButton.click();
        }
    }, 450); // 450ms, slightly less than the 500ms CSS animation duration
}
</script>
""", unsafe_allow_html=True)

# --- Session State Management ---
if "messages" not in st.session_state:
    st.session_state.messages = {
        name: [{"role": "system", "content": f"You are {name}, a {leaders[name]['style']} financial expert specializing in {leaders[name]['title']}. Provide helpful, insightful advice in your unique style."}] 
        for name in leaders
    }
if "selected_leader" not in st.session_state:
    st.session_state.selected_leader = None
if "current_index" not in st.session_state:
    st.session_state.current_index = 0

leaders_list = list(leaders.keys())

# --- Main Page - Carousel ---
if not st.session_state.selected_leader:
    st.markdown('<h1 class="hero-title">HerStory: Financial Wisdom</h1>', unsafe_allow_html=True)
    
    # Use st.form to capture button clicks without immediate rerun, 
    # allowing custom JS to handle the animation first.
    with st.form(key="carousel_form"):
        col1, col2, col3 = st.columns([1, 6, 1])
        
        current_index = st.session_state.current_index
        current_name = leaders_list[current_index]
        leader = leaders[current_name]
        first_name = current_name.split()[0]
        
        # --- Carousel Buttons ---
        with col1:
            st.write("") # Spacer
            if st.form_submit_button("←", key="prev_btn_form", type="secondary"):
                # Use st.experimental_rerun() for instant rerun after state update
                # but we'll use a hacky way with JS to trigger the animation
                st.session_state.current_index = (current_index - 1) % len(leaders_list)
                st.markdown(f'<script>applyExitAnimation("prev");</script>', unsafe_allow_html=True)
                st.rerun()

        with col3:
            st.write("") # Spacer
            if st.form_submit_button("→", key="next_btn_form", type="secondary"):
                st.session_state.current_index = (current_index + 1) % len(leaders_list)
                st.markdown(f'<script>applyExitAnimation("next");</script>', unsafe_allow_html=True)
                st.rerun()
        
        # --- Card Content ---
        with col2:
            # Start card
            st.markdown(f'<div class="leader-card">', unsafe_allow_html=True)
            
            st.markdown('<div class="curved-image-section">', unsafe_allow_html=True)
            
            # Curved Text Header
            st.markdown(f'''
                <div class="curved-text-container">
                    <div class="text-arc"></div>
                    <p class="curved-text">Hi, I'm **{first_name}**. Let's Chat!</p>
                </div>
            ''', unsafe_allow_html=True)
            
            # Profile image container
            st.markdown('<div class="profile-circle-wrapper">', unsafe_allow_html=True)
            
            # Try to load and display the image
            try:
                # To make st.image work reliably, it's best to use the actual Streamlit function
                # and override the style with CSS.
                if os.path.exists(leader['image']):
                    img = Image.open(leader['image'])
                    st.image(img, use_container_width=False)
                else:
                    # Fallback for missing image
                    st.markdown(f'''
                        <div style="width: 280px; height: 280px; margin: 0 auto; border-radius: 50%; background: linear-gradient(135deg, #E91E63, #9C27B0); display: flex; align-items: center; justify-content: center; font-size: 120px; border: 8px solid white; box-shadow: 0 25px 60px rgba(0, 0, 0, 0.25), 0 0 0 15px rgba(233, 30, 99, 0.2);">
                            {leader['emoji']}
                        </div>
                    ''', unsafe_allow_html=True)
            except Exception:
                # Fallback for error loading image
                 st.markdown(f'''
                    <div style="width: 280px; height: 280px; margin: 0 auto; border-radius: 50%; background: linear-gradient(135deg, #E91E63, #9C27B0); display: flex; align-items: center; justify-content: center; font-size: 120px; border: 8px solid white; box-shadow: 0 25px 60px rgba(0, 0, 0, 0.25), 0 0 0 15px rgba(233, 30, 99, 0.2);">
                        {leader['emoji']}
                    </div>
                ''', unsafe_allow_html=True)

            # Close profile container
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True) # Close curved-image-section
            
            # Leader info - Title and Specialty
            st.markdown(f'<h2 class="leader-name-text">{current_name}</h2>', unsafe_allow_html=True)
            st.markdown(f'<p class="leader-title-text">{leader["title"]} {leader["emoji"]}</p>', unsafe_allow_html=True)
            
            # The requested description right below the image:
            st.markdown(f'<p class="leader-specialty-text">"{leader["specialty"]}"</p>', unsafe_allow_html=True)
            
            # Expertise tags
            expertise_tags = ''.join([f'<span class="expertise-tag">{exp}</span>' for exp in leader['expertise']])
            st.markdown(f'<div class="expertise-tags-container">{expertise_tags}</div>', unsafe_allow_html=True)
            
            # Start Chat Button (needs to be inside the form for the form submit)
            if st.form_submit_button("Start Chatting", key="start_chat_form", use_container_width=True):
                st.session_state.selected_leader = current_name
                st.rerun()

            # Close card
            st.markdown('</div>', unsafe_allow_html=True)
    
# --- Chat Page (Left as is, as the request focused on the carousel) ---
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
        # Chat header uses the existing stylish header
        st.markdown(f"""
        <div class="chat-header-box">
            <div class="chat-avatar">{first_name[0]}</div>
            <div class="chat-info">
                <h2>{name}</h2>
                <p>{leader['title']} {leader['emoji']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Display chat messages (same as original code)
    for msg in st.session_state.messages[name][1:]:
        role_class = "user" if msg["role"] == "user" else "assistant"
        st.markdown(f"""
        <div class="message-container {role_class}">
            <div class="message-bubble {role_class}">{msg["content"]}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Input area
    user_input = st.chat_input(f"Ask {first_name} about finance...", key="user_input_chat")
    
    if user_input:
        st.session_state.messages[name].append({"role": "user", "content": user_input})
        
        try:
            with st.spinner(f"{first_name} is thinking..."):
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
        except Exception as e:
            st.error(f"Error communicating with AI: {str(e)}")
            
        st.rerun()
