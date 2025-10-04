import streamlit as st
import openai

# -------------------
# 🔑 OpenAI API Key
# -------------------
openai.api_key = "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"

# -------------------
# 👩‍💻 Leaders Dictionary
# -------------------
leaders = {
    "Indra": {"style": "professional and concise"},
    "Janet Yellen": {"style": "calm, analytical, and precise"},
    "Sheryl Sandberg": {"style": "strategic and motivational"}
}

# -------------------
# Streamlit Layout
# -------------------
st.set_page_config(
    page_title="Finance Leaders AI Chat",
    layout="wide"
)

st.markdown('<h1 style="text-align:center; color:#00e6ac;">💼 Finance Leaders AI Chat</h1>', unsafe_allow_html=True)

# -------------------
# 👩 Select Leader
# -------------------
leader_name = st.selectbox("👩 Choose a leader to chat with:", list(leaders.keys()))
leader = leaders[leader_name]

# -------------------
# 💬 Chat History Initialization
# -------------------
if "messages" not in st.session_state:
    st.session_state.messages = {
        name: [{"role": "system", "content": f"You are a financial expert, {name}, speaking in a {leaders[name]['style']} style."}]
        for name in leaders
    }

# Reset chat if leader changes
if "last_leader" not in st.session_state:
    st.session_state.last_leader = leader_name
elif st.session_state["last_leader"] != leader_name:
    st.session_state.last_leader = leader_name

# Display previous messages for selected leader
for msg in st.session_state.messages[leader_name][1:]:
    with st.chat_message("assistant" if msg["role"] == "assistant" else "user"):
        st.write(msg["content"])

# -------------------
# ✍️ Chat Input
# -------------------
if prompt := st.chat_input(f"Ask {leader_name} a finance or business question..."):
    # Append user message
    st.session_state.messages[leader_name].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # -------------------
    # 💬 Use OpenAI v2 API (new syntax)
    # -------------------
    with st.spinner(f"{leader_name} is thinking..."):
        client = openai.OpenAI(api_key=openai.api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages[leader_name],
            temperature=0.7,
            max_tokens=300
        )
        reply = response.choices[0].message.content

    # Append assistant message
    st.session_state.messages[leader_name].append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)

# -------------------
# Footer
# -------------------
st.markdown("""
<div style="text-align:center; margin-top:40px; color:#aaa;">
Developed with ❤️ using Streamlit & OpenAI GPT-3.5
</div>
""", unsafe_allow_html=True)
