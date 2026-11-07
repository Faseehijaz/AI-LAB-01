text = """
Artificial Intelligence is growing.
NLP helps computers understand text.
Text processing is useful.
"""

sentences = text.split(".")

sentences = [s.strip() for s in sentences if s.strip()]

print("Text Chunks:")

for chunk in sentences:
    print(chunk)