import streamlit as st
from pipeline.generator import generate_responses
from pipeline.judge import judge

# Add custom CSS for better response boxes
st.markdown("""
<style>
    /* Container for the two columns */
    .responses-container {
        margin: 1rem 0;
    }
    
    /* Individual response box styling */
    .response-card {
        padding: 1.2rem;
        border-radius: 12px;
        height: auto;
        min-height: 300px;
        max-height: 500px;
        overflow-y: auto;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Left response (GPT) - align left */
    .response-left {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-left: 5px solid #ff6b6b;
        margin-right: 0.5rem;
    }
    
    /* Right response (Gemini) - align right */
    .response-right {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border-right: 5px solid #4ecdc4;
        margin-left: 0.5rem;
    }
    
    /* Title styling */
    .response-title {
        font-size: 1.3rem;
        font-weight: bold;
        color: white;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid rgba(255,255,255,0.3);
    }
    
    /* Content styling */
    .response-content {
        color: white;
        line-height: 1.6;
        font-size: 0.95rem;
    }
    
    /* Scrollbar styling */
    .response-card::-webkit-scrollbar {
        width: 8px;
    }
    
    .response-card::-webkit-scrollbar-track {
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
    }
    
    .response-card::-webkit-scrollbar-thumb {
        background: rgba(255,255,255,0.3);
        border-radius: 10px;
    }
    
    /* Result card styling */
    .result-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# initialize state
if "screen" not in st.session_state:
    st.session_state.screen = "input"

# ---------------- SCREEN 1 ----------------
if st.session_state.screen == "input":
    st.title("LLM Judge System")

    prompt = st.text_area("Enter your prompt:")

    if st.button("Generate"):
        if prompt:
            st.session_state.prompt = prompt
            st.session_state.screen = "responses"
            st.rerun()

# ---------------- SCREEN 2 ----------------
elif st.session_state.screen == "responses":
    st.title("Model Responses")

    prompt = st.session_state.prompt

    with st.spinner("Generating responses..."):
        responses = generate_responses(prompt)

    st.session_state.responses = responses

    # Two columns side by side
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="response-card response-left">
            <div class="response-title">
                🤖 Response A (GPT)
            </div>
            <div class="response-content">
                {responses["A"].replace(chr(10), '<br>')}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="response-card response-right">
            <div class="response-title">
                🧠 Response B (Gemini)
            </div>
            <div class="response-content">
                {responses["B"].replace(chr(10), '<br>')}
            </div>
        </div>
        """, unsafe_allow_html=True)

    if st.button("Judge"):
        st.session_state.screen = "result"
        st.rerun()

# ---------------- SCREEN 3 ----------------
elif st.session_state.screen == "result":
    st.title("Final Evaluation")

    prompt = st.session_state.prompt
    responses = st.session_state.responses

    with st.spinner("Judging responses..."):
        result = judge(prompt, responses)

    st.markdown(f"""
    <div class="result-card">
        <h3 style="margin: 0 0 1rem 0; color: white;">⚖️ Judgment Result</h3>
        <div style="line-height: 1.6;">
            {result.replace(chr(10), '<br>')}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Show previous responses (scrollable) - User can scroll up to see
    st.subheader("📋 Review Responses")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**🤖 Response A (GPT)**")
        st.text_area("", responses["A"], height=300, key="review_a", label_visibility="collapsed")

    with col2:
        st.markdown("**🧠 Response B (Gemini)**")
        st.text_area("", responses["B"], height=300, key="review_b", label_visibility="collapsed")

    if st.button("New Prompt"):
        st.session_state.screen = "input"
        st.rerun()