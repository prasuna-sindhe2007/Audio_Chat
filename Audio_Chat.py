
import streamlit as st
from datetime import datetime
from audio_recorder_streamlit import audio_recorder

st.set_page_config(
    page_title="Voice_Chat",
    page_icon="🎤"
)

st.markdown("""
<style>
.stApp {
    background: #f0f2f6;
}
.header {
    background: #25D366;
    color: white;
    padding: 15px;
    border-radius: 10px;
    font-size: 28px;
    text-align: center;
    font-weight: bold;
}
.john {
    background: #DCF8C6;
    padding: 12px;
    border-radius: 15px;
    margin: 8px;
    text-align: right;
    color: black;
    margin-left: 20%;
}
.alice {
    background: white;
    padding: 12px;
    border-radius: 15px;
    margin: 8px;
    text-align: left;
    color: black;
    margin-right: 20%;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="header">🎤 Group Voice Chat</div>',
    unsafe_allow_html=True
)

if "messages" not in st.session_state:
    st.session_state.messages = []

user = st.selectbox(
    "Select User",
    ["John", "Alice", "Bob"]
)

st.subheader("Record Your Voice")

audio_bytes = audio_recorder(
    text="Click to record",
    recording_color="#e74c3c",
    neutral_color="#25D366",
    pause_threshold=2.0,
    sample_rate=44100
)

if audio_bytes:
    if st.button("Send Voice Message"):
        st.session_state.messages.append({
            "user": user,
            "audio": audio_bytes,
            "time": datetime.now().strftime("%H:%M")
        })
        st.rerun()

st.subheader("Voice Messages")

for msg in st.session_state.messages:
    css = "john" if msg["user"] == "John" else "alice"

    if msg["user"] == "Bob":
        css = "alice"

    st.markdown(
        f'<div class="{css}">'
        f'<b>{msg["user"]}</b><br>'
        f'<small>{msg["time"]}</small>'
        f'</div>',
        unsafe_allow_html=True
    )

    st.audio(msg["audio"], format="audio/wav")

if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()