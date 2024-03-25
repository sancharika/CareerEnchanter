resume_review = """
    You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
    Please share your professional evaluation on whether the candidate's profile aligns with the role. 
    Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.

    Human-Like Resume Review for {info}
    Job Description: {input_text}
    Resume: {doc}
    Format:
**Resume Review Context:**  
**Detailed Evaluation:**  
- **Relevance to the Field:** Assess how the candidate's experience and skills match the specific requirements of the job in [User-Specified Field].  
- **Key Strengths:** Identify the strongest aspects of the candidate's resume, such as specific skills, achievements, or experiences that are particularly aligned with the job description.  
- **Areas for Development:** Highlight any areas where the candidate may need further development or additional experience to fully meet the job requirements.  
- **Career Progression:** Analyze the candidate's career trajectory and how it aligns with the expectations for the role.  
- **Education and Certifications:** Evaluate the relevance and level of the candidate's educational background and any professional certifications.  
- **Cultural Fit:** Provide insights on the candidate's potential cultural fit within the organization, based on the information in the resume.
**Skills and Experience Table:**  
| Skill/Experience | Relevance to Job | Candidate's Proficiency | Notes |
| ---------------- | ---------------- | ----------------------- | ----- |
| [Skill 1]        | [High/Medium/Low] | [Expert/Intermediate/Novice] | [Any specific notes] |
| [Skill 2]        | [High/Medium/Low] | [Expert/Intermediate/Novice] | [Any specific notes] |
| ...              | ...              | ...                     | ...   |

**Conclusion:**  
- Summarize the overall suitability of the candidate for the position in [User-Specified Field]. Include recommendations for any additional qualifications or experiences that might Improve the candidate’s profile for this role.
                 """

ats_resume = """
## Human-Like Resume Analysis for {info}
    Job Description: {input_text}
    Resume: {doc}
    Format:
**Resume Analysis Context:**  
**Automated Evaluation:**  
- **Keyword Matching:** Identify key skills, technologies, and qualifications mentioned in the job description and evaluate the presence and frequency of these keywords in the candidate's resume.  
- **Skills Assessment:** Analyze the candidate's listed skills against those required in the job description. Provide a match percentage or rating.  
- **Experience Relevance:** Calculate the relevance of the candidate's previous job titles, companies, and industries in relation to the job description.  
- **Education and Certifications Matching:** Match the candidate's education level and certifications with the requirements specified in the job description.
**AI-ATS Analysis Table:**  
| Category | Details from Resume | Match with Job Description | Notes |
| -------- | ------------------- | -------------------------- | ----- |
| Skills   | [List of skills from resume] | [Match percentage/rating] | [Any specific notes] |
| Experience | [List of experiences from resume] | [Relevance rating] | [Any specific notes] |
| Education | [Candidate's education details] | [Match/No Match] | [Any specific notes] |
| ...      | ...                 | ...                        | ...   |

**Conclusion:**  
- Provide an overall rating or score of the candidate’s resume based on the AI/ATS analysis. Suggest areas where the candidate might improve their resume to better align with the job description in [User-Specified Field].

    """

ats_score = """
    You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
    your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
    the job description. First the output should come as percentage and then keywords missing.

    Job Description: {input_text}
    Resume: {doc}
    """

resume_improve = """
    As an experienced Technical Human Resource Manager, evaluating the provided resume against the job description involves a thorough analysis of the candidate's profile, strengths, weaknesses, and alignment with the specified job requirements. Here's a structured approach to provide a professional evaluation and key points for enhancing the resume:

1. **Evaluation of Alignment:**
   - Assess the candidate's qualifications, skills, and experience in relation to the job requirements outlined in the job description.
   - Determine the extent to which the candidate's profile aligns with the technical aspects, HR management responsibilities, and other specified criteria.

2. **Strengths and Weaknesses Assessment:**
   - Highlight the candidate's strengths that directly match the job requirements, such as relevant technical skills, HR management experience, and achievements.
   - Identify any weaknesses or areas where the candidate's profile may fall short in meeting the job requirements, such as lacking specific technical skills or limited experience in certain areas.

3. **Recommendations for Resume Improvement:**
   - For areas of alignment:
     - Emphasize the candidate's relevant technical skills, HR management experience, and achievements prominently in the resume.
     - Provide specific examples or quantifiable results to demonstrate the candidate's contributions and impact in previous roles.
   - For areas needing improvement:
     - Suggest adding relevant technical skills or certifications to Improve the candidate's qualifications.
     - Recommend highlighting transferable skills or experiences that demonstrate adaptability and readiness to learn new technologies or processes.
     - Encourage showcasing any HR management initiatives, projects, or leadership roles that align with the job requirements.
   
4. **Key Points for Resume Improvement:**
   - Technical Skills:
     - Identify and include key technical skills mentioned in the job description, such as programming languages, software tools, or platforms.
     - Provide details of projects or experiences that demonstrate proficiency in these technical skills.
   - HR Management Experience:
     - Highlight HR management responsibilities, such as recruitment, performance evaluation, training, and employee relations.
     - Showcase leadership skills, teamwork, and collaboration experiences in managing technical teams or projects.
   - Achievements and Impact:
     - Include quantifiable achievements, awards, or recognition received in previous roles.
     - Describe specific contributions or projects that resulted in positive outcomes, cost savings, or process improvements.

5. **Stand-Out Factors:**
   - Provide insights to the candidate on how to differentiate themselves by highlighting unique experiences, innovative approaches, or specialized expertise relevant to the role.
   - Asses adding professional development activities, industry involvement, or contributions to open-source projects to showcase continuous learning and engagement in the field whichever5 is best based on provided resume.



    Job Description: {input_text}
    Resume: {doc}
    """

resume_enhance = """
    You are an experienced Technical Human Resource Manager,your task is to Provide specific suggestions in bullet points to tailor the resume to the job description from the provided paragraph. 
    Please share your professional suggestions on what to write and how to write the given pargraph so that the candidate's profile aligns with the role. 
    Highlight weaknesses of the applicant in relation to the specified job requirements and provide sugestions on how to enhance it and make it strength.

    Job Description: {input_text}
    Resume: {doc}
    paragraph: {info}
    """

resume_recommendation = """
You are an experienced Technical Human Resource Manager,your task is to Provide specific recommendations to tailor the resume to the job description. 
Suggest possible next steps, certifications, courses or experiences the person could do. 
Make sure the suggestions are all FACTUALLY ACCURATE given the original resume and specify 
which suggestions require further action. Mention where resume is good and where resume lacks. FOR EVERY CHANGE YOU SUGGEST, PROVIDE A SIMPLE EXPLANATION 
FOR WHY< Additionally include critiques on a granular level including strong word choice suggestion etc. 
Output in formatted, aesthetically pleasing markdown text.
Job Description: {input_text}
Resume: {doc}
"""

recommendation_section = """
You are an experienced Technical Human Resource Manager,your task is to Provide specific recommendations to tailor the resume to the job description. 
    Please share your professional recommendations on what to write and how to write the given pargraph so that the candidate's profile aligns with the role. 
    Talk about each section of user's resume and talk good and bad points of it. Recommend how to modify it better.

Job Description: {input_text}
    Resume: {doc}
"""

keyword_analysis = """
Perform keyword analysis on both the input job description and the existing resume to identify missing keywords, 
Analyze the provided document for keywords related to the job description. 
Return a list of relevant keywords from the document with their number of occurance.  
If no pages are found containing any of the keywords return "No Matching Keywords Found".  
Output as a Markdown List where missing keywords are listed along with the Keywords presnet in the resume with number of time it occured in resume.
Job Description: {input_text}
Resume: {doc}
"""

keyword_synonyms = """
Provide a list of minimum 10 synonums of the given  keyword. If there are less than 10
synonyms provide as many as you can find. The output should be in a markdown numbered list format where the synonyms of the keyword are listed in numbered list, 
return as many as you can provide maximum 15.
Also suggest synonyms of the keyword based on job description
Job Description: {input_text}
Resume: {doc}
Keyword: {info}
"""

resume_update = """
## Writing an Updated Resume which is ATS friendly in latex format

### Step-by-Step Guide for the Updated Resume

#### 1. Header
- **Full Name**
- **Contact Information:** Phone number, Email address, LinkedIn profile (if applicable)
- **Location:** City, State (optional, depending on privacy preferences)

#### 2. Professional Summary
- Craft a 2-3 sentence summary focusing on key qualifications and alignment with the target job description.

#### 3. Skills
- List skills that are relevant to the job description. 
- Use bullet points and ensure to include keywords from the job description for ATS optimization.

#### 4. Professional Experience
- For each relevant position, include **Job Title**, **Company Name**, **Location**, and **Dates of Employment**.
- Under each role, list bullet points that detail responsibilities and achievements, emphasizing quantifiable outcomes and incorporating job description keywords.

#### 5. Education
- List degrees obtained, including **Degree Title**, **Institution Name**, **Location**, and **Graduation Date**.
- Add relevant coursework or projects if they align with the job description.

#### 6. Certifications (Optional)
- Include certifications relevant to the job description.

#### 7. Additional Sections (Optional)
- Sections like Volunteer Experience, Publications, or Awards can be added if they are relevant to the job and add value.

#### 8. ATS Compatibility and Formatting
- Ensure the resume format is simple with a standard, easy-to-read font like Arial or Times New Roman.
- Avoid complex elements like tables or columns that can confuse ATS systems.

#### 9. Final Review
- Proofread for any spelling or grammatical errors.
- Check alignment with the job description and ensure all important keywords are included.

### Conclusion:
- Provide a brief summary highlighting the key changes made to the resume and how they align with the target job description.
- Offer suggestions for any additional improvements or steps the candidate can take to further tailor their resume for similar roles in the future.

### Example

- Create a new resume in the given LaTeX format.

**Job Description:** {input_text}

**Resume data:** {doc}

The output should be first show step by step guide for updated resume after that generate new resume based on provided information
and then also add the latex format of the generated resume .
"""

#info contains company name also
cover_letter = """
## Writing a Cover Letter for {info}
Job Description: {input_text}
Resume: {doc}
### Step-by-Step Guide for the Cover Letter
#### 1. Contact Information and Date
- Include your contact information at the top: Name, Address (optional), Phone Number, Email.
- Add the date of writing the letter.
#### 2. Salutation
- If possible, address the letter to a specific person (e.g., "Dear [Hiring Manager's Name]").
- If the specific contact is not known, use a general salutation like "Dear Hiring Manager".
#### 3. Introduction
- Open with a strong, engaging sentence that captures the reader’s attention.
- Mention the job title you’re applying for and where you found the job listing.
- Briefly state why you are interested in the role and the company.
#### 4. Body of the Letter (1-2 Paragraphs)
- In the first paragraph, summarize your relevant experience and skills, aligning them with key requirements of the job description.
- In the second paragraph, provide specific examples from your past work that demonstrate your abilities and successes. Use quantifiable achievements when possible.
- Explain how your skills and experiences make you an ideal fit for the role and how you can contribute to the company.
#### 5. Conclusion
- Reiterate your enthusiasm for the position.
- Mention any attached documents (like your resume or portfolio).
- State your availability for an interview and propose the next steps or indicate your intention to follow up.
#### 6. Sign-off
- Close the letter with a professional sign-off such as "Sincerely" or "Best regards," followed by your name.
- If you’re submitting a printed letter, leave space for your handwritten signature above your typed name.
### Final Tips:
- Keep the cover letter concise, ideally not exceeding one page.
- Tailor the letter to the job and company – avoid using a generic template.
- Proofread carefully to avoid any spelling or grammatical errors.
- Use a professional tone, but allow your personality to shine through.
## Example:
- Provide an cover letter also as example
"""

linkedin_profile = """
## Comprehensive LinkedIn Profile and Headline Update
Job Description: {input_text}
Resume: {doc}
### Step-by-Step Guide for LinkedIn Update
#### 1. LinkedIn Headline
- Create a headline combining your current role or expertise, key skills from your resume, and aspects of the job you are targeting.
- Example format: “[Current Role/Expertise] with [Key Skills] | Aspiring [Target Job Title]”
#### 2. Profile Photo and Background Image
- Choose a professional profile picture and a background image that reflects your professional brand.
#### 3. About Section
- Write a summary that includes your professional background, achievements, skills, and career aspirations, tailored to align with your resume and the job description.
#### 4. Experience Section
- Update to mirror your resume, highlighting roles, responsibilities, and achievements relevant to your career goals.
- Use language and keywords from the job description to Improve alignment.
#### 5. Education
- Ensure your educational background matches your resume, including relevant courses and certifications.
#### 6. Skills & Endorsements
- Add and prioritize skills from your resume and the job description, focusing on those most relevant to your career goals.
#### 7. Recommendations
- Request recommendations that reinforce your skills and experiences, particularly those aligning with your target job.
#### 8. Licenses and Certifications
- Include any relevant certifications, aligning with both your resume and job description.
#### 9. Volunteer Experience
- Add volunteer work if it supports your professional image and career objectives.
#### 10. Accomplishments
- Include any relevant publications, patents, projects, honors, and awards.
#### 11. Customized URL
- Customize your LinkedIn URL for a professional touch.
### Final Steps:
- Review for consistency in language and tone.
- Proofread to ensure there are no errors.
- Update your profile regularly to reflect your current professional status and aspirations.
### Conclusion:
- Your LinkedIn profile should be a dynamic representation of your professional life, showcasing both your experience and personality, and aligned with your career goals and targeted job opportunities.
"""

interview = """
## Customized Interview Questions and Candidate Questions to Interviewer
Job Description: {input_text}
Resume: {doc}
Role: {info}
### Part 1: Tailored Interview Questions Based on Job Description
#### 1. Role-Specific Technical Questions
- Generate questions that assess skills and experiences directly related to the key requirements in the job description.
- Example: "Your resume mentions experience in [specific skill from resume]; can you discuss how you've applied this skill in a past project?"
#### 2. Behavioral Questions Related to Job Role
- Formulate questions based on scenarios or challenges outlined in the job description.
- Example: "The job description emphasizes teamwork. Can you share an experience where you successfully collaborated on a challenging project?"
#### 3. Scenario-Based Problem-Solving Questions
- Create questions that relate to potential challenges or tasks in the new role, as described in the job description.
- Example: "Given a scenario of [specific challenge in the job description], how would you approach solving it?"
#### 4. Questions Assessing Cultural and Company Fit
- Based on the company culture hinted at in the job description, prepare questions to evaluate the candidate's fit.
- Example: "Our company values [specific value from job description]. Can you provide an example of how you've embodied this value in your professional life?"
### Part 2: Questions for the Candidate to Ask the Interviewer
#### 1. Clarifications on Role Responsibilities
- Suggest questions that seek deeper insights into the daily responsibilities and expectations.
- Example: "Could you elaborate on the typical day-to-day tasks for someone in this position?"
#### 2. Inquiries About Team Structure and Dynamics
- Based on the team information in the job description, propose questions about team collaboration and environment.
- Example: "Can you tell me more about the team I would be working with?"
#### 3. Questions About Growth and Development Opportunities
- Encourage questions about professional development, especially in areas highlighted as important in the job description.
- Example: "What opportunities for professional growth does the company provide in [area mentioned in the job description]?"
#### 4. Queries About Success Measurement
- Suggest questions about how success is measured in the role, relating to performance indicators mentioned in the job description.
- Example: "What are the key performance indicators for this role, and how are they measured?"
### Conclusion:
- These questions are designed to provide a comprehensive understanding of the candidate's suitability for the role and to help the candidate assess whether the role aligns with their career aspirations.
- Remind candidates to use these questions as a guide and personalize them to reflect their unique experiences and interests.
"""

company_recommendations = """
## Company Recommendations Based on Candidate's Resume and Job Description
Job Description: {input_text}
Resume: {doc}
### Process for Identifying Similar Companies
#### 1. Analyze the Job Description
- Identify key industry sectors, job responsibilities, and required skills from the job description.
- Note any specific company characteristics mentioned (e.g., startup culture, large multinational, specific sector focus).
#### 2. Review the Candidate's Resume
- Look for industries, skills, and types of roles the candidate has experience in.
- Consider the candidate’s career level and preferences indicated by their work history and achievements.
#### 3. Research and List Similar Companies
- Based on the collected information, identify companies in similar industries or those that offer similar roles.
- Consider companies that align with the candidate's experience level and career aspirations.
#### 4. Provide a Diverse Range of Options
- Include a mix of large corporations, mid-size companies, and startups, if relevant.
- Ensure the list covers various sectors within the industry that align with the candidate's skills and experience.
#### 5. Additional Considerations
- Take into account the candidate’s geographical preferences or willingness to relocate, if indicated in the resume or job description.
- Consider the current market trends and the demand for the candidate’s skill set in various companies.
### Example Output:
- Based on a resume with experience in digital marketing and a job description for a Digital Marketing Manager in the tech industry, the recommendations could include:
   - Tech companies with a strong online presence.
   - Marketing agencies specializing in digital strategies for tech clients.
   - Startups in the tech sector looking to build their digital marketing teams.
### Conclusion:
- Provide a list of recommended companies where the candidate might find similar roles to the one they are applying for.
- Encourage the candidate to research these companies further to find specific job openings that match their skills and career goals.
"""
