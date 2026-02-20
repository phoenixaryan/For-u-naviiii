import streamlit as st

st.set_page_config(page_title="For Navya ❤️", page_icon="🌹")

# Session State logic
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'is_forgiven' not in st.session_state:
    st.session_state.is_forgiven = False

no_messages = [
    "No 😠", "Sach mai? 🥺", "Phir soch lo... 🤔", 
    "Phir ek bar phir se... 🧐", "Sorry na bebe... Plzzz? 🎀", "Otheeeeee... ❤️"
]

st.markdown("""
    <style>
    .main { background-color: #fff5f5; }
    .stButton>button { border-radius: 20px; width: 100%; height: 3.5em; font-weight: bold; }
    .love-text {
        text-align: center; color: #ff4b4b; font-size: 45px;
        font-weight: bold; animation: heartbeats 1.5s infinite;
    }
    @keyframes heartbeats {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    </style>
    """, unsafe_allow_html=True)

if not st.session_state.is_forgiven:
    st.markdown("<h1 style='text-align: center;'>Hi Navya... ❤️</h1>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<h4 style='text-align: center;'>I am really sorry. Kya tumne mujhe maaf kiya?</h4>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes, Maaf kiya! 😍"):
            st.session_state.is_forgiven = True
            st.rerun()

    with col2:
        if st.session_state.no_count < len(no_messages):
            if st.button(no_messages[st.session_state.no_count]):
                st.session_state.no_count += 1
                st.rerun()
        else:
            st.write("Ab toh maaf kar do! ✨")
else:
    st.balloons()
    # Arctic Monkeys - I Wanna Be Yours (Sample Audio Link)
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3", autoplay=True)
    st.markdown("<div class='love-text'>I LOVE U NAVYA SO MUCH ❤️</div>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZ4bmZ4bmZ4bmZ4/l4pTfx2qLs35wMSWk/giphy.gif")
    st.markdown("<h3 style='text-align: center;'>Everything is better with you. ✨</h3>", unsafe_allow_html=True)
