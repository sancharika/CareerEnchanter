# app.py
import os
import streamlit as st
from features import (ats, 
                      analyzer, 
                      company_recommend, 
                      cover_letter, 
                      enhance, 
                      improve, 
                      interview,
                      linkedin,
                      newresume,
                      recommend, 
                      review)
from components import docLoader
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class CareerEnchanter(object):
    def __init__(self, title="CareerEnchanter"):
        self.title = title

    @staticmethod
    def model():
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        return ChatGoogleGenerativeAI(model="gemini-pro")
    
enchanter = CareerEnchanter()
st.set_page_config(page_title=enchanter.title, page_icon='🤖', layout='centered')

st.title("Enchant your Career")

text = docLoader.load_doc()
st.session_state['doc_text'] = text
jd=st.text_area("Job Description: ",key="input")
with st.sidebar:
        st.title(' :blue[_Career Enchanter_] 🤖')
        option = st.radio("Select an option: ", (
            "ATS Score", 
            "Resume Review", 
            "Resume Enhancements", 
            "Resume Improvements", 
            "Recommendation", 
            "Keywords", 
            "Generate Cover Letter", 
            "Resume Generator", 
            "Linkedin Profile Update", 
            "Posssible Interview Questions", 
            "Company Recommendations"
            ))

        
        if option == "ATS Score":
            calculation_method = st.radio("Choose how you want to calculate ATS Score: ", ("Using AI", "Manually (Cosine Similarity)"), horizontal=True)

        elif option == "Recommendation":
            recommendation_type = st.radio("Select the type of recommendation you want: ", ("Entire Resume", "Section Wise"), horizontal=True)

        elif option == "Keywords":
            analyz_type = st.radio("Select the type of Keywords Fucntion you want: ", ("Analyse Keywords", "Keyword Synonyms"), horizontal=True)

        with st.spinner("Loading Model..."):
            llm = enchanter.model()


# Create a dictionary mapping options to functions
option_functions = {
    "ATS Score": ats.run_ats,
    "Resume Review": review.run_review,
    "Resume Enhancements": enhance.run_enhance,
    "Resume Improvements": improve.run_improve,
    "Recommendation": recommend.run_recommend,
    "Keywords": analyzer.run_analyzer,
    "Generate Cover Letter": cover_letter.run_letter,
    "Resume Generator": newresume.run_newresume,
    "Linkedin Profile Update": linkedin.run_linkedin,
    "Posssible Interview Questions": interview.run_interview,
    "Company Recommendations": company_recommend.run_company
}

# Handle the selected option
if option in option_functions:
    func = option_functions[option]
    if option == "ATS Score":
        if calculation_method == "Manually (Cosine Similarity)":
            func(llm, st.session_state['doc_text'], jd, manual=True)
        else:
            func(llm, st.session_state['doc_text'], jd)
    elif option == "Recommendation":
        if recommendation_type == "Entire Resume":
            func(llm, st.session_state['doc_text'], jd, section=True)
        else:
            func(llm, st.session_state['doc_text'], jd)
    elif option == "Keywords":
        if analyz_type == "Analyse Keywords":
            func(llm, st.session_state['doc_text'], jd, analysis=True)
        else:
            func(llm, st.session_state['doc_text'], jd)
    else:
        func(llm, st.session_state['doc_text'], jd)