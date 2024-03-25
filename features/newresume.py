#newresume.py

from dotenv import load_dotenv
from components.functions import Functions
import streamlit as st
from components.prompts import resume_update

def run_newresume(llm,doc='',jd=''):
    load_dotenv()
    newresume = Functions()
    st.write("Generate new resume in LateX Format.")
    submit = st.button("Generate Resume")    
    
    if submit:
        if doc is not None:
            with st.spinner("Generating..."):
                response=newresume.get_gemini_response(llm=llm,template=resume_update,doc=doc,input_text=jd)
            st.subheader("Resume In LateX Format")
            st.write(response)
        else:
            st.write("Please upload the resume")

if __name__ == "__main__":
    newresume = Functions()
    run_newresume(newresume.model())