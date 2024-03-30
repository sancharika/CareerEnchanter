---
title: CareerEnchanter
emoji: ⚡
colorFrom: purple
colorTo: yellow
sdk: streamlit
sdk_version: 1.32.2
app_file: app.py
pinned: false
---

# Career Enchanter 🚀

Welcome to Career Enchanter, your ultimate AI companion for job hunting! With a plethora of features designed to enhance your job search experience, Career Enchanter is here to revolutionize the way you approach your career goals. 

## Features Galore 🎉

1. **ATS Score**: Wondering if your resume will make the cut? Let Career Enchanter calculate your ATS score using AI and BERT Model! No more guesswork, just precise results.

2. **Resume Review**: Get a professional evaluation of your profile's alignment with the role you're eyeing. No more shooting in the dark!

3. **Resume Enhancements**: Receive expert suggestions on key points to boost your resume's impact. Make those recruiters take notice!

4. **Resume Improvements**: Transform paragraphs into powerful bullet points with tailored suggestions. Let your achievements shine through!

5. **Recommendations**: Curated advice on what to add or modify, whether it's your entire resume or specific sections. Stay ahead of the game!

6. **Keywords**: Analyze job descriptions and find the perfect keywords to make your resume stand out. Plus, discover the best synonyms to amp up your content!

7. **Generate Cover Letter**: Craft a killer cover letter effortlessly, tailored to the job at hand. Impress recruiters from the get-go!

8. **Resume Generator**: Generate a brand new resume in LaTeX format based on your details and job description. It's like having your own personal resume magician!

9. **LinkedIn Profile Update**: Get creative ideas and examples to spruce up your LinkedIn profile. Let your professional persona shine bright!

10. **Possible Interview Questions**: Prepare for success with a curated list of interview questions based on the job description. Nail that interview like a pro!

11. **Company Recommendations**: Receive personalized job and company recommendations based on your skills and experience. It's like having a career genie in your pocket!

## Technologies Used 💡

- **AI Model Used**: Gemini-Pro
- **Tech Stack**: Python, LangChain-GenAI, NLTK, Streamlit, Torch, BERT-Transformers
- **Deployment**: Hugging Face

## Project Structure 🌟

```
career-enchanter
│   app.py
│
└───components
│   │   docLoader.py
│   │   Modified app.py
│   │   functions.py
│   │   prompts.py
│   
└───features
    │   analyzer.py
    │   ats.py
    │   company_recommend.py
    │   cover_letter.py
    │   enhance.py
    │   improve.py
    │   interview.py
    │   linkedin.py
    │   newresume.py
    │   recommend.py
    │   review.py
```

## Getting Started 🚀

To get started with Career Enchanter, simply clone the repository and run the `app.py` file. Ensure you have all the necessary dependencies installed, and you're good to go!

---
1. Clone the repository and install dependencies
```bash
$ git clone https://github.com/sancharika/CareerEnchanter.git
```
```
cd CareerEnchanter
```
```
pip install -r requirements.txt
```
2. Run the application locally (Streamlit)
```
streamlit run app.py
```
3. Open your web browser and go to http://localhost:8501 to see the application in action!

---

With Career Enchanter by your side, you'll navigate the job market with confidence and finesse. Happy job hunting! 🌟
