# Auto Assignment Valuation System

An AI-powered web application that automatically evaluates student assignments using Natural Language Processing (NLP) and Machine Learning. Built as a final-year project at the University of Agriculture Faisalabad, Constituent College Toba Tek Singh.

**Author:** Romania Akram (2022-AG-6340)  
**Advisor:** Mr. Syed Ali Imran

---

## Overview

The system addresses the core challenges of manual grading — inconsistency, high workload, and delayed feedback — by automating the evaluation pipeline. It compares student responses against model answers using semantic similarity, checks grammar, and scores keyword coverage, then produces a final weighted grade with personalized feedback.

---

## Features

- **Role-based access** — Student, Teacher, and Admin roles with separate dashboards
- **Assignment management** — Teachers create assignments with model answers, keywords, and custom rubrics
- **AI scoring pipeline** — Three-component evaluation engine:
  - Semantic similarity via `sentence-transformers` (`all-MiniLM-L6-v2`)
  - Grammar checking via `language-tool-python` (LanguageTool Java server)
  - Keyword coverage via `spaCy` NLP (`en_core_web_sm`)
- **Weighted rubric** — Per-assignment configurable weights for semantic, grammar, and keyword scores
- **Instant feedback** — Automated, actionable feedback returned on submission
- **Teacher overrides** — Teachers can review and manually override any AI-generated score
- **Grade publishing** — Grades are only visible to students after the teacher publishes them

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django 6.x |
| Database | SQLite (development) |
| AI / NLP | sentence-transformers, spaCy, language-tool-python |
| ML Model | `all-MiniLM-L6-v2` (Sentence-BERT) |
| Frontend | HTML, CSS, JavaScript (Django templates) |
| Auth | Django custom user model with role field |

---

## Project Structure

```
Auto-assignment-valuation-system-/
├── auto_grader/               # Django project settings & URL routing
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── assignments/               # Main Django app
│   ├── models.py              # CustomUser, Assignment, Rubric, Submission, Grade
│   ├── views.py               # Login, dashboard routing, teacher & student views
│   ├── urls.py                # App URL patterns
│   ├── admin.py
│   ├── ai/                    # AI scoring modules
│   │   ├── semantic_scorer.py # Cosine similarity via Sentence-BERT
│   │   ├── grammar_checker.py # LanguageTool grammar analysis
│   │   ├── nlp_engine.py      # spaCy preprocessing & keyword scoring
│   │   └── scoring_aggregator.py  # Combines all scores with rubric weights
│   ├── templates/
│   │   ├── base.html
│   │   └── assignments/
│   │       ├── login.html
│   │       ├── teacher_dashboard.html
│   │       └── student_dashboard.html
│   └── migrations/
├── manage.py
├── setup_test_data.py         # Script to seed test users and assignments
├── db.sqlite3
└── requirements.txt           # (see setup below)
```

---

## Data Models

| Model | Description |
|---|---|
| `CustomUser` | Extends Django's `AbstractUser`; adds a `role` field (`student`, `teacher`, `admin`) |
| `Assignment` | Title, description, model answer, keywords (JSON), max points, linked teacher |
| `Rubric` | Per-assignment weights for semantic (default 60%), grammar (20%), keyword (20%) |
| `Submission` | Student's text answer linked to an assignment |
| `Grade` | AI scores (semantic, grammar, keyword, final), feedback JSON, teacher override, publish flag |

---

## AI Scoring Pipeline

```
Student submission
       │
       ├─► Semantic Scorer  ──► cosine similarity vs model answer  (0–100)
       ├─► Grammar Checker  ──► LanguageTool error density penalty  (0–100)
       └─► Keyword Scorer   ──► % of required keywords present      (0–100)
                │
         Weighted sum using Rubric
                │
          Final Score (capped at 100)  +  Feedback JSON
```

The aggregation formula:

```
final = (semantic_score × semantic_weight)
      + (grammar_score  × grammar_weight)
      + (keyword_score  × keyword_weight)
```

---

## Setup & Installation

### Prerequisites

- Python 3.10+
- Java (required by `language-tool-python` — JRE 8+ works)
- Git

### 1. Clone the repo

```bash
git clone https://github.com/your-username/Auto-assignment-valuation-system-.git
cd Auto-assignment-valuation-system-
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install django sentence-transformers spacy language-tool-python torch
python -m spacy download en_core_web_sm
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. (Optional) Seed test data

```bash
python setup_test_data.py
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## URL Routes

| URL | View | Description |
|---|---|---|
| `/` | `dashboard` | Redirects based on user role |
| `/login/` | `login_view` | Login page |
| `/logout/` | Django built-in | Logout |
| `/teacher/` | `teacher_dashboard` | Teacher's assignment overview |
| `/student/` | `student_dashboard` | Student's submission interface |
| `/admin/` | Django admin | Admin panel |

---

## User Roles

**Teacher**
- Create assignments with model answers, keywords, and rubric weights
- View all student submissions and AI-generated scores
- Override any AI score manually
- Publish grades to make them visible to students

**Student**
- Browse available assignments
- Submit text answers
- View published grades and feedback

**Admin**
- Full access via Django admin panel
- Manage users and system data

---

## Limitations (MVP)

- English language only
- Text-based assignments only (no math, code, diagrams)
- No plagiarism detection
- SQLite database — not suitable for production at scale
- First run downloads the LanguageTool Java server automatically (~200 MB)
- `all-MiniLM-L6-v2` model is downloaded on first use (~80 MB)

---

## Alignment with UN SDGs

- **SDG 4 — Quality Education**: Improves assessment efficiency and feedback quality for students at all resource levels
- **SDG 9 — Industry, Innovation, and Infrastructure**: Demonstrates practical AI integration into educational infrastructure

---

## License

This project was developed as an academic submission. Reuse or distribution should credit the original author.
