documents = [
    "NLP helps computers understand language.",
    "Python is used for programming.",
    "Tokenization splits text into words.",
    "Artificial Intelligence is a useful field."
]

query = input("Enter your question: ").lower()

scores = []

for doc in documents:
    score = 0

    for word in query.split():
        if word in doc.lower():
            score += 1

    scores.append((score, doc))

scores.sort(reverse=True)

print("\nSearch Results:")

for score, doc in scores[:3]:
    print(doc, "Score:", score)