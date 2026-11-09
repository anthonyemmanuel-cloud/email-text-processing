"""
GLAB 927.1.2: Hands-On Text Processing for Email Management with Python
Student: Anthony Emmanuel

This program uses the NLTK library to apply two text processing techniques
to business emails:
    1. Stemming       - chops words down to a rough root form
    2. Lemmatization  - turns words into their real dictionary form
"""

# ---------------------------------------------------------------
# Task 1: Importing Libraries
# ---------------------------------------------------------------

# Importing NLTK library
import nltk

# Checking NLTK version
nltk_version = nltk.__version__

# Print confirmation message and NLTK version
print(f"NLTK library successfully imported. NLTK version: {nltk_version}")
print()


# ---------------------------------------------------------------
# Task 2: Implementing Stemming
# ---------------------------------------------------------------
from nltk.stem import PorterStemmer

# Download NLTK resources (tokenizers)
# Newer NLTK versions use "punkt_tab", so we download both to be safe.
# quiet=True hides the download messages so the output stays clean.
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

# Sample email content for stemming
email_content = (
    "Our team will be working on the upcoming project deadlines. "
    "Please ensure that all deliverables are submitted before the end of the week."
)

# Create a Porter Stemmer instance
porter_stemmer = PorterStemmer()

# Apply stemming to each word in the email content
stemmed_words = [porter_stemmer.stem(word) for word in nltk.word_tokenize(email_content)]

# Print the original and stemmed text
print("=== Task 2: Stemming ===")
print("Original Email Content:", email_content)
print("Stemmed Email Content:", " ".join(stemmed_words))
print()


# ---------------------------------------------------------------
# Task 3: Applying Lemmatization
# ---------------------------------------------------------------
from nltk.stem import WordNetLemmatizer

# Sample email content for lemmatization
email_content_lemma = (
    "The team members are working on their tasks diligently. "
    "Please ensure that every report is submitted promptly."
)

# Download the WordNet dictionary that the lemmatizer uses
nltk.download("wordnet", quiet=True)

# Create a WordNet Lemmatizer instance
lemmatizer = WordNetLemmatizer()

# Apply lemmatization to each word in the email content
lemmatized_words = [lemmatizer.lemmatize(word) for word in nltk.word_tokenize(email_content_lemma)]

# Print the original and lemmatized text
print("=== Task 3: Lemmatization ===")
print("Original Email Content:", email_content_lemma)
print("Lemmatized Email Content:", " ".join(lemmatized_words))
print()

print("Congratulations! Stemming and lemmatization completed successfully.")