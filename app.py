import streamlit as st
import re

def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8: score += 1
    else: suggestions.append("Increase total length to at least 8 characters.")

    if re.search(r"[a-z]", password): score += 1
    else: suggestions.append("Include at least one lowercase letter (a-z).")

    if re.search(r"[A-Z]", password): score += 1
    else: suggestions.append("Include at least one uppercase letter (A-Z).")

    if re.search(r"[0-9]", password): score += 1
    else: suggestions.append("Include at least one numerical digit (0-9).")

    special_char_pattern = re.escape(r"!@#$%^&*()-_=+[{]};:'\",<.>/?\\|`~")
    if re.search(r"[{}]".format(special_char_pattern), password): score += 1
    else: suggestions.append("Include at least one special character (e.g., @, #, $, %).")

    return score, suggestions

# --- UI Configuration ---
st.set_page_config(
    page_title="Password Guard Pro", 
    page_icon="🛡️", 
    layout="centered"
)

# Custom CSS Layout එකක් එකතු කිරීම (ලස්සන background සහ fonts සඳහා)
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stTitle {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        color: #1e3a8a;
        font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (වම්පස මෙනුව) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluent/100/000000/shield.png", width=80)
    st.title("About Password Guard")
    st.info("""
    This analyzer evaluates your credentials against standard industry metrics:
    - Length Check
    - Case Sensitivity
    - Numerical Analysis
    - Special Notation
    """)
    st.caption("🔒 Privacy Guaranteed: Processing occurs 100% locally in your RAM.")

# --- MAIN INTERFACE (ප්‍රධාන පිටුව) ---
st.title("🛡️ SecureAuth Password Analyzer")
st.write("Check your password strength instantly. Our local algorithm ensures your data remains safe and private.")
st.markdown("---")

# User Input Component
user_password = st.text_input(
    label="🔐 Enter Password to Evaluate:", 
    type="password", 
    help="Type your password securely. Characters are masked automatically."
)

if user_password:
    score, suggestions = check_password_strength(user_password)
    
    st.markdown("### **Security Analysis**")
    
    # Dynamic Metrics & Progress Bars (ලකුණු අනුව වෙනස් වන ලස්සන වර්ණ)
    if score == 5:
        st.success("🔥 **Excellent Score!** Your password is exceptionally robust.")
        st.progress(100)
    elif score == 4:
        st.info("💪 **Strong Score:** High complexity, minor enhancements possible.")
        st.progress(80)
    elif score == 3:
        st.warning("⚠️ **Moderate Score:** Contains structural vulnerabilities.")
        st.progress(60)
    else:
        st.error("❌ **Critical Risk:** Highly vulnerable to brute-force attacks.")
        st.progress(30)
        
    # Display Score Badge
    col1, col2 = st.columns([1, 3])
    with col1:
        st.metric(label="Security Score", value=f"{score} / 5")
    
    # Recommendations Box (ලස්සන වැටෙන මෙනුවක් ලෙස)
    if suggestions:
        with st.expander("💡 Click here to view Actionable Recommendations", expanded=True):
            for item in suggestions:
                st.markdown(f"📍 <span style='color:#b91c1c; font-weight:500;'>{item}</span>", unsafe_allow_html=True)
    else:
        st.balloons()
        st.markdown("✨ **Perfect Compliance!** No recommendations needed.")