#Make necessary imports

# ====================== CONFIG ======================
st.set_page_config(page_title="AI Weather Assistant", page_icon="🌤️")

st.title("🌤️ AI Weather Information Assistant")
st.subheader("Dynamic Context Injection Demo")

# Sidebar - Groq API Key
with st.sidebar:
    st.header("Settings")
    groq_key = st.text_input("Groq API Key", type="password")
    if groq_key:
        #Enter your code here
        st.success("✅ Groq Connected")

# ====================== MAIN UI ======================
city = st.text_input("Enter City Name", value="Hyderabad")
user_question = st.text_area(
    "Ask a weather-related question",
    value="Will it rain today? What should I wear?"
)

if st.button("Get Weather & Answer", type="primary"):
    if not groq_key:
        st.error("Please enter your Gemini API Key in the sidebar")
    else:
        with st.spinner("Fetching live weather..."):
            #Enter your code here to get weather data

          

            # Build dynamic prompt
            #Enter Your code here to call the prompt
            # Call Groq
            with st.spinner("Thinking with injected weather data..."):
                
            #Enter Your code here to get response
            st.subheader("🤖 AI Response")
            #st.write(uncomment this and write text response of AI)

            # Show what was injected (Educational)
            with st.expander("See Dynamic Context Injected"):
                st.code(prompt, language="markdown")