# Meeting Intelligence Hub

### *Turning conversations into decisions.*

---

## 🎥 Demo

![Demo](demo.gif)


---

## 🔴 The Problem

Modern organizations conduct frequent meetings that generate long transcripts. Important information such as decisions, action items, and risks often gets buried in these transcripts, forcing teams to revisit discussions instead of executing tasks efficiently.

---

## 🟢 The Solution

Meeting Intelligence Hub transforms raw meeting transcripts into structured insights. It automatically extracts summaries, action items, decisions, and risks, helping teams quickly understand outcomes and take action without re-reading entire transcripts.

---

## ⚙️ Tech Stack

* **Languages:** Python, JavaScript
* **Backend:** FastAPI
* **Frontend:** HTML, CSS, JavaScript
* **AI Integration:** OpenAI API
* **Other Tools:** dotenv

---

## 🛠 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/aryagithubrit/meeting-intelligence-hub.git
cd meeting-intelligence-hub
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API key

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

### 5. Run backend

```bash
uvicorn backend.app:app --reload --port 8006
```

### 6. Run frontend

Open:

```
frontend/index.html
```


## 📸 Screenshots

### 🔹 Welcome Page
![Welcome](screenshot3.png)

### 🔹 Upload Page
![Upload](screenshot6.png)

### 🔹 Analysis Page
![Analysis](screenshot5.png)

### 🔹 Analysis cont
![Results](screenshot4.png)

---

## 🚧 Challenges I Faced 

This project wasn’t straightforward at all:

*  GitHub blocked my push because of exposed API key
  → learned how to properly secure secrets

*  Frontend couldn't talk to backend
  → fixed using middleware

*  FastAPI import issues (`ModuleNotFoundError`)
  → restructured project properly

*  Infinite loading bug in frontend
  → debugged using browser console

---

##  Security

API keys are **not stored in the code**.

They are handled using:

* `.env` file
* environment variables

---

##  Future Scope

* Real-time meeting transcription
* Meeting analytics dashboard
* Team collaboration features
* Deployment as SaaS

---

## 👨‍💻 About Me

Hi,i am arya a btech undergrad in the trade electronics and communication..As a beginner in this field it was indeed very much difficult to handle too much of data together and coordinating them all together...however finnally managed to work it out.

---

##  Final Thought

This started as a simple idea,
but ended up becoming a full-stack system combining:

* backend logic
* frontend experience
* AI integration

And a lot of debugging as always 
