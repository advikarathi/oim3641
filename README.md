# Advika Rathi — OIM 3641 Classwork

This is where I'm keeping all my work for **OIM 3641** at Babson College — in-class demos, problem sets, and whatever project stuff comes out of the second half of the semester.

## About Me

Hi, I'm Advika! I'm an undergrad at Babson studying OIM (Operations & Information Management). This class is my first real dive into working with LLM APIs and retrieval-augmented generation, so expect this repo to grow a lot messier (and hopefully more interesting) as the term goes on.

## Skills & Tools

**Languages**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=postgresql&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=flat&logo=markdown&logoColor=white)

**Libraries & Frameworks**

![Pandas](https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![LlamaIndex](https://img.shields.io/badge/LlamaIndex-000000?style=flat)
![Google Gemini API](https://img.shields.io/badge/Gemini_API-4285F4?style=flat&logo=googlegemini&logoColor=white)
![OpenAI API](https://img.shields.io/badge/OpenAI_API-412991?style=flat&logo=openai&logoColor=white)

**Tools**

![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat&logo=visualstudiocode&logoColor=white)

## Directory Structure

```
oim3641/
├── data/                    # Datasets and reference files used in demos/exercises
│   ├── handbook/             # PDF reference documents
│   └── *.tsv.zip              # Sample datasets (e.g., Amazon reviews)
├── 01-llm-call.py           # Basic LLM API call example (Gemini)
├── 02-python_concepts.ipynb # Python fundamentals exercises
├── 03-demo_create_llamaindex.py        # Building a LlamaIndex from parsed documents
├── 03-demo_llama_gemini_retrieval.py   # RAG retrieval using LlamaIndex + Gemini
├── 03-demo_llama_retrieval.py          # RAG retrieval using LlamaIndex + OpenAI
└── README.md                # This file
```

Everything's numbered by lesson (`01-`, `02-`, `03-`...) so it's easy to tell what week something came from. New problem sets and the project milestones will get added the same way as the semester goes on.

## Install Instructions

Want to run any of this yourself? Here's how.

**1. Clone the repository**

```bash
git clone https://github.com/advikarathi/oim3641.git
cd oim3641
```

**2. Set up a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

**3. Install dependencies**

```bash
pip install python-dotenv google-genai llama-index llama-cloud-services pandas scikit-learn jupyter
```

**4. Add your API keys**

A few of the scripts hit external LLM APIs, so you'll need your own keys in a `.env` file in the project root:

```
GEMINI_API_KEY=your_key_here
LLAMA_CLOUD_API_KEY=your_key_here
ORGANIZATION_ID=your_org_id_here
OPENAI_API_KEY=your_key_here
```

**5. Run a script or notebook**

```bash
python 01-llm-call.py
jupyter notebook 02-python_concepts.ipynb
```

## Let's Connect

Feel free to reach out — always happy to chat about class projects, internships, or anything data/AI related.

- **LinkedIn:** [linkedin.com/in/advikarathi](https://www.linkedin.com/in/advikarathi/)
- **GitHub:** [github.com/advikarathi](https://github.com/advikarathi)
- **Email:** advikarathi2@gmail.com
