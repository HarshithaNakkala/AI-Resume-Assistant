import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def clean_jd(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation and special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def tokenize_jd(text):
    return word_tokenize(text)


def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))

    filtered_tokens = []

    for word in tokens:
        if word not in stop_words:
            filtered_tokens.append(word)

    return filtered_tokens


def parse_jd(text):
    cleaned_text = clean_jd(text)

    tokens = tokenize_jd(cleaned_text)

    important_words = remove_stopwords(tokens)

    return {
        "cleaned_text": cleaned_text,
        "tokens": tokens,
        "important_words": important_words
    }


if __name__ == "__main__":

    jd = """
    We are looking for a Python developer.

    Skills:
    Python
    SQL
    AWS
    Docker
    Git
    """

    result = parse_jd(jd)

    print("CLEANED TEXT:")
    print(result["cleaned_text"])

    print("\nTOKENS:")
    print(result["tokens"])

    print("\nIMPORTANT WORDS:")
    print(result["important_words"])