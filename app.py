import streamlit as st

# Page Config (Agar pehle se nahi lagaya)
st.set_page_config(page_title="Rayyan | Projects Showcase", layout="wide")

# Custom CSS for Interactive Cards
st.markdown("""
<style>
/* Card Styling */
.project-card {
    background-color: #1e293b;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(56, 189, 248, 0.2);
    border-color: #38bdf8;
}

/* Card Titles & Text */
.card-title {
    color: #38bdf8;
    font-size: 1.3rem;
    font-weight: bold;
    margin-bottom: 8px;
}

.card-desc {
    color: #94a3b8;
    font-size: 0.95rem;
    line-height: 1.5;
    margin-bottom: 15px;
}

/* Tech Stack Badges */
.tech-badge {
    background-color: rgba(56, 189, 248, 0.1);
    color: #38bdf8;
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 0.8rem;
    font-weight: 600;
    margin-right: 5px;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 Featured Projects")
st.write("Mere banaye gaye kuch interactive Python aur AI/Voice tools:")

# Grid Layout (3 Columns)
col1, col2, col3 = st.columns(3)

# --- Project Card 1 ---
with col1:
    st.markdown("""
    <div class="project-card">
        <div class="card-title">🎙️ Voice Command Calculator</div>
        <div class="card-desc">
            Speech recognition aur audio processing powered smart calculator jo voice commands par mathematical operations perform karta hai.
        </div>
        <div>
            <span class="tech-badge">Python</span>
            <span class="tech-badge">SoundDevice</span>
            <span class="tech-badge">SpeechRecognition</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View Source / Demo", "https://www.instagram.com/rayyanagenticdeveloper?stkn=MWxpMDdoeHRrMWJvdA==", use_container_width=True)

# --- Project Card 2 ---
with col2:
    st.markdown("""
    <div class="project-card">
        <div class="card-title">🤖 AI Agentic Assistant</div>
        <div class="card-desc">
            OpenRouter APIs aur custom LLM prompt workflows ka istemaal karke banaya gaya intelligent chatbot framework.
        </div>
        <div>
            <span class="tech-badge">Python</span>
            <span class="tech-badge">OpenRouter</span>
            <span class="tech-badge">AI Frameworks</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View Details", "https://www.facebook.com/share/1YTR5R27rd/", use_container_width=True)

# --- Project Card 3 ---
with col3:
    st.markdown("""
    <div class="project-card">
        <div class="card-title">📊 Interactive Streamlit Web Apps</div>
        <div class="card-desc">
            Data visualization, conditional security logic, aur user-friendly dashboards ke liye interactive Web Applications.
        </div>
        <div>
            <span class="tech-badge">Streamlit</span>
            <span class="tech-badge">Pandas</span>
            <span class="tech-badge">Python</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Explore Web Apps", "https://instagram.com/your_username", use_container_width=True)