!pip install nltk
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import os

# Download necessary data
nltk.download('punkt')
nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Read input from file
with open("input.txt", "r") as file:
    text = file.read()

# Tokenize the text
tokens = word_tokenize(text)

# Lemmatize each token
lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]

# Print results
print("Original Text:")
print(text)
print("\nLemmatized Words:")
print(" ".join(lemmatized_words))