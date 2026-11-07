import re

text = "I like Artificial Intelligence."

tokens = text.split()

print("Original Text:", text)
print("Tokens:", tokens)

words = re.findall(r'\b\w+\b', text)

print("Clean Tokens:", words)