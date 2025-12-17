import streamlit as st 
import google.generativeai as genai
st.title("Generative AI App with Streamlit")    
st.write("my app")
user_input = st.text_input("Enter your prompt:")
genai.configure(api_key="AIzaSyAhLMlfTBXt9xkcvc8ZU7Z5zhJB-WBinAA")
model=genai.GenerativeModel("models/GEMINI-2.5-flash")
if user_input:
    response=model.generate_content(user_input)
    st.write(response.text)
