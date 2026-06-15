# 🎤 AI Mock Interviewer

An AI-powered interview preparation platform that generates role-specific interview questions, evaluates candidate responses, and provides detailed feedback to help users improve their interview performance.

## 🚀 Live Demo



https://ai-mock-interviewer-npxs.onrender.com/

---

## 📌 Features

* Generate interview questions based on job role
* Multiple difficulty levels (Easy, Medium, Hard)
* AI-powered answer evaluation
* Detailed feedback and scoring
* Strengths and weaknesses analysis
* Suggested improved answers
* Interview preparation tips
* Simple and interactive Streamlit UI

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Groq API
* Llama 3.3 70B Versatile
* Render (Deployment)

---

## 📂 Project Structure

```text
ai-mock-interviewer/
│
├── app.py
├── requirements.txt
├── render.yaml
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/ai-mock-interviewer.git
cd ai-mock-interviewer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 🧠 How It Works

1. Select a job role.
2. Choose a difficulty level.
3. Generate an interview question.
4. Submit your answer.
5. Receive:

   * Score
   * Strengths
   * Weaknesses
   * Improved Answer
   * Interview Tips

---

## 🎯 Use Cases

* Technical interview preparation
* Campus placement practice
* Internship interview readiness
* Self-assessment and learning
* Skill improvement through AI feedback

---

## 💡 Future Enhancements

* Multi-question interview rounds
* Overall interview scorecard
* Downloadable interview reports
* Voice-based mock interviews
* Domain-specific interview tracks
* Interview history tracking

---

## 📈 Resume Description

Developed an AI-powered Mock Interviewer using Streamlit and Groq LLMs that generates role-specific interview questions, evaluates candidate responses, provides detailed feedback, and helps users improve interview readiness through personalized assessments.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

---


This project is licensed under the MIT License.
