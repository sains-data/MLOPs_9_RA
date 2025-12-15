import streamlit as st
from chatbot import get_answer

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="PerpusBot ITERA",
    page_icon="📚",
    layout="centered"
)

# ================== CUSTOM CSS ==================
st.markdown("""
<style>
.chat-box {
    border-radius: 12px;
    padding: 10px;
    margin-bottom: 8px;
}
.user {
    background-color: #E3F2FD;
}
.bot {
    background-color: #F1F8E9;
}
.footer {
    text-align: center;
    color: gray;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)

# ================== SIDEBAR ==================
with st.sidebar:
    st.title("📚 PerpusBot ITERA")
    st.markdown("""
    Chatbot Informasi Perpustakaan ITERA  
    Dibangun dengan pendekatan **Information Retrieval**

    **Teknologi:**
    - TF-IDF
    - Cosine Similarity
    - Streamlit
    - Pandas & Scikit-Learn

    ---
    👨‍🎓 *Proyek Tugas MLOps*
    """)

    if st.button("🗑 Reset Percakapan"):
        st.session_state.messages = []
        st.rerun()

# ================== HEADER ==================
st.markdown("<h2 style='text-align:center;'>📖 PerpusBot ITERA</h2>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;color:gray;'>Tanya apa saja seputar layanan dan aturan perpustakaan ITERA</p>",
    unsafe_allow_html=True
)
st.divider()

# ================== SESSION STATE ==================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ================== CHAT HISTORY ==================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ================== USER INPUT ==================
user_input = st.chat_input("Ketik pertanyaan kamu di sini...")

if user_input:
    # simpan pesan user
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # respons bot
    with st.spinner("PerpusBot sedang mencari jawaban..."):
        response = get_answer(user_input)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.markdown(response)

# ================== FOOTER ==================
st.markdown(
    "<div class='footer'>© 2025 PerpusBot ITERA | Sistem Informasi Perpustakaan</div>",
    unsafe_allow_html=True
)
