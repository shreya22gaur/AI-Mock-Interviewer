import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os



load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.set_page_config(page_title="AI Mock Interviewer")

st.title("🎤 AI Mock Interviewer")

role = st.selectbox(
    "Select Role",
    ["Software Engineer", "Data Analyst", "Machine Learning Engineer", "Frontend Developer"]
)

difficulty = st.selectbox(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)

if "question" not in st.session_state:
    st.session_state.question = ""

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

if st.button("Generate Interview Question"):

    prompt = f"""
    Generate ONE {difficulty} interview question
    for a {role}.

    Only return the question.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    st.session_state.question = response.choices[0].message.content

if st.session_state.question:

    st.subheader("Interview Question")

    st.write(st.session_state.question)

    answer = st.text_area(
        "Your Answer",
        height=200
    )

    if st.button("Evaluate Answer"):

        evaluation_prompt = f"""
        You are an interview evaluator.

        Question:
        {st.session_state.question}

        Candidate Answer:
        {answer}

        Evaluate using:

        Score out of 10

        Strengths

        Weaknesses

        Improved Answer

        Interview Tip
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": evaluation_prompt}
            ]
        )

        st.session_state.feedback = (
            response.choices[0]
            .message
            .content
        )

if st.session_state.feedback:

    st.subheader("Feedback")

    st.write(st.session_state.feedback)