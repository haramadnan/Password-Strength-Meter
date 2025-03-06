import re
import streamlit as st

#Page Styling

st.set_page_config(page_title="Password Strength Checker By Haram Adnan" , page_icon="🔑" , layout="centered")
st.markdown("""
<style>
     .main {text-align: center};
     .stTextInput {width: 60% !important; margin: auto; }
     .sTButton button {width: 50%; background-color: blue; color: black; font-size: 18px; } 
     .stButton button:hover { background-color: skyblue; color: white} 
</style>
""", unsafe_allow_html=True)

#Page Title and Description

st.title("🔐 Password Strength Meter")
st.write("Enter your password below to assess it's security strength. 🔎")

#Function
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #Increased score by 1
    else:
        feedback.append("❌ Password should be **atleast 8 character long**.")

    if re.search(r"[A-Z]" , password) and re.search(r"[a-z]" , password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase letters (a-z)**.") 

    if re.search(r"\d" , password):
        score += 1
    else:
        feedback.append("❌ Password should include **atleast one number (0-9)**.")
    
    if re.search(r"[!@#$%^&*]" , password):
        score += 1
    else:
        feedback.append("❌ Include **atleast 1 special character (!@#$%^&*)**.")

 #Display Powerd Strength Results
    if score == 4:
        st.success("✔️ **Strong Password** - Your pasword is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Enhance security by incorporating additional features.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestion below to strength it.")

    #Feedback
    if feedback:
        with st.expander("💡 **Improve Your Password** "):
            for item in feedback:
                st.write(item)

password = st.text_input("Enter your password: ", type="password" , help="Ensure your password is strong 🔐")

#Button Working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")