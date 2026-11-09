# Email Text Processing with NLTK

**GLAB 927.1.2: Hands-On Text Processing for Email Management with Python**
Per Scholas AI Prompt Engineering (2026-CAX-255) · Anthony Emmanuel

## What this app does

This program uses Python's **NLTK** (Natural Language Toolkit) library to clean up business email text so it is easier to sort and analyze:

- **Stemming** chops words down to a rough root (for example, `deadlines` → `deadlin`, `submitted` → `submit`). It is fast and good for grouping similar emails.
- **Lemmatization** turns words into their real dictionary form (for example, `members` → `member`, `tasks` → `task`). It is slower but gives real words.

## What problem it solves

When a business receives thousands of emails, words like *submit*, *submitted* and *submitting* should count as the same idea. Stemming and lemmatization make those words match, which helps with categorizing emails and finding common themes.

## Technologies used

- Python 3
- [uv](https://docs.astral.sh/uv/) for project and dependency management
- [NLTK](https://www.nltk.org/): `PorterStemmer`, `WordNetLemmatizer`, `word_tokenize`

## How to install dependencies

```bash
uv sync
```

## How to run

```bash
uv run python src/email_text_processing/email_processing.py
```

The first run downloads small NLTK data files (`punkt`, `punkt_tab`, `wordnet`), so it needs an internet connection.