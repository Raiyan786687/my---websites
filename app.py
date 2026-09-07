import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Rayyan | Agentic Developer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Advanced Custom CSS Injection
st.markdown("""
<style>
    /* Dark Metallic Background */
    .stApp {
        background: #0b0f19;
        color: #e2e8f0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Neon Hero Section */
    .hero-container {
        text-align: center;
        padding: 50px 20px 30px 20px;
        background: linear-gradient(180deg, rgba(56,189,248,0.08) 0%, rgba(11,15,25,0) 100%);
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        margin-bottom: 40px;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(90deg, #38bdf8 0%, #818cf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
        letter-spacing: -1px;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        color: #94a3b8;
        max-width: 650px;
        margin: 0 auto 20px auto;
    }
    
    .glow-badge {
        background: rgba(56, 189, 248, 0.1);
        color: #38bdf8;
        border: 1px solid rgba(56, 189, 248, 0.3);
        padding: 6px 18px;
        border-radius: 30px;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        display: inline-block;
        margin-bottom: 15px;
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.2);
    }

    /* Glassmorphism Project Cards */
    .glass-card {
        background: rgba(18, 24, 38, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 28px;
        height: 100%;
        backdrop-filter: blur(12px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        margin-bottom: 15px;
    }
    
    .card-title {
        color: #f8fafc;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .card-text {
        color: #94a3b8;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 20px;
    }
    
    /* Tech Pills */
    .pill {
        background: #1e293b;
        color: #38bdf8;
        padding: 4px 12px;
        border-radius: 8px;
        font-size: 0.78rem;
        font-weight: 600;
        display: inline-block;
        margin-right: 6px;
        border: 1px solid rgba(255,255,255,0.05);
    }
    
    /* Hide Default Header/Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Hero Header
st.markdown("""
<div class="hero-container">
    <div class="glow-badge">RAYYAN AGENTIC DEVELOPER</div>
    <h1 class="hero-title">Crafting Intelligent AI Tools & Apps</h1>
    <p class="hero-subtitle">Software Engineering Student & Python Developer specializing in Voice Commands, AI Workflows, and Custom Interactive Interfaces.</p>
</div>
""", unsafe_allow_html=True)

# Social Media Strip
col_a, col_b, col_c = st.columns([1, 2, 1])
with col_b:
    sc1, sc2 = st.columns(2)
    with sc1:
        st.link_button("📸 Follow on Instagram", "https://www.instagram.com/rayyanagenticdeveloper?stkn=MWxpMDdoeHRrMWJvdA==", use_container_width=True, type="primary")
    with sc2:
        st.link_button("📘 Connect on Facebook", "https://www.facebook.com/share/1YTR5R27rd/", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# Showcase Title
st.markdown("<h2 style='text-align: center; color: #f8fafc; font-weight: 800;'>Featured Projects</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; margin-bottom: 30px;'>Explore some of my recent Python & AI engineering builds</p>", unsafe_allow_html=True)

# Projects Grid
p1, p2, p3 = st.columns(3)

with p1:
    st.markdown("""
    <div class="glass-card">
        <div class="card-title">🎙️ Voice Calculator</div>
        <p class="card-text">Smart audio-driven math utility built with speech recognition and Python audio processing for seamless voice command input.</p>
        <div style="margin-bottom: 15px;">
            <span class="pill">Python</span>
            <span class="pill">SoundDevice</span>
            <span class="pill">SpeechRec</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View Code / Demo ➔",  "https://www.instagram.com/rayyanagenticdeveloper?stkn=MWxpMDdoeHRrMWJvdA==", use_container_width=True)

with p2:
    st.markdown("""
    <div class="glass-card">
        <div class="card-title">🤖 Agentic AI Bot</div>
        <p class="card-text">Custom LLM integration framework leveraging OpenRouter API endpoints to build intelligent, autonomous chat and task workflows.</p>
        <div style="margin-bottom: 15px;">
            <span class="pill">Python</span>
            <span class="pill">OpenRouter</span>
            <span class="pill">AI Agents</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View Code / Demo ➔",  "https://www.facebook.com/share/1YTR5R27rd/", use_container_width=True)

with p3:
    st.markdown("""
    <div class="glass-card">
        <div class="card-title">🌐 Streamlit Apps</div>
        <p class="card-text">Fast, responsive web apps focused on interactive logic, security scripts, and dynamic graphical user interfaces for desktop and web.</p>
        <div style="margin-bottom: 15px;">
            <span class="pill">Streamlit</span>
            <span class="pill">Tkinter</span>
            <span class="pill">UI/UX</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View Code / Demo ➔","https://www.instagram.com/rayyanagenticdeveloper?stkn=MWxpMDdoeHRrMWJvdA==", use_container_width=True)
