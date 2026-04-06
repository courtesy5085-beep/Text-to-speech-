import streamlit as st
from gtts import gTTS
import tempfile

st.set_page_config(page_title="Speak It Pro", page_icon="🔊", layout="centered")

st.title("🔊 Speak It Pro (Streamlit Version)")
st.write("Type text → Generate → Listen")

# ---------- Text Input ----------
text = st.text_area("Enter your text", height=150)

# ---------- Language ----------
lang = st.selectbox(
    "Select Language",
    {
        "English (US)": "en",
        "English (UK)": "en",
        "Urdu": "ur",
        "Arabic": "ar",
        "Hindi": "hi"
    }
)

# ---------- Controls ----------
col1, col2 = st.columns(2)

with col1:
    slow = st.checkbox("Slow Voice")

with col2:
    clear = st.button("Clear Text")

if clear:
    st.rerun()

# ---------- Generate Speech ----------
if st.button("▶ Generate & Play"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        try:
            tts = gTTS(text=text, lang=lang, slow=slow)

            # Save temp audio file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                audio_file = open(fp.name, "rb")

                st.audio(audio_file.read(), format="audio/mp3")

            st.success("Audio generated successfully!")

        except Exception as e:
            st.error(f"Error: {e}")

# ---------- Info ----------
st.markdown("---")
st.caption("⚡ Powered by gTTS | Works on Streamlit Cloud")
