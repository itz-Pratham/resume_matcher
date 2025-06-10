# Resume Matcher MVP

This Streamlit demo ranks resumes against a job description using spaCy and Sentence-Transformers.

## Setup

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
pytest  # run unit tests
```

## Running

```bash
streamlit run main.py
```

The app now provides per-candidate **View Details** navigation and keeps a history
of past job description runs in `uploads/job_history.json` which can be recalled
from the sidebar.