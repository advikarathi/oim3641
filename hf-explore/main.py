import time
from transformers import pipeline

start = time.perf_counter()
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
print(f"Model loaded in {time.perf_counter() - start:.1f} seconds\n")

labels = ["completed", "in progress", "not started", "blocked"]

updates = [
    "I finished the literature review and added all the citations.",
    "Haven't had time to start the slides yet, will do it this weekend.",
    "I'm stuck on the data analysis because I can't access the dataset.",
]

for update in updates:
    start = time.perf_counter()
    result = classifier(update, candidate_labels=labels)
    elapsed = time.perf_counter() - start
    top_label = result["labels"][0]
    top_score = result["scores"][0]
    print(f"Update: {update}")
    print(f"  -> {top_label} ({top_score:.0%}) in {elapsed:.2f}s\n")