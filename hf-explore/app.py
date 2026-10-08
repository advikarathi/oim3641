import streamlit as st
from transformers import pipeline

LABELS = ["completed", "in progress", "not started", "blocked"]
ICONS = {"completed": "✅", "in progress": "🔄", "not started": "⏳", "blocked": "🚧"}


@st.cache_resource
def load_classifier():
    return pipeline("zero-shot-classification", model="facebook/bart-large-mnli")


st.title("Project Pulse")
st.write("Paste a teammate's status update, and Project Pulse will sort it by progress.")

classifier = load_classifier()

update = st.text_input("Status update", placeholder="e.g. I'm halfway through the slides")

if st.button("Check status"):
    if not update.strip():
        st.warning("Please enter a status update first.")
    else:
        try:
            with st.spinner("Classifying..."):
                result = classifier(update, candidate_labels=LABELS)
            top_label = result["labels"][0]
            top_score = result["scores"][0]

            st.subheader(f"{ICONS[top_label]} {top_label.title()}")
            st.write(f"Confidence: {top_score:.0%}")

            if top_score < 0.6:
                st.info("Low confidence. You may want to check in with this teammate.")

            st.write("All labels:")
            for label, score in zip(result["labels"], result["scores"]):
                st.progress(score, text=f"{label}: {score:.0%}")
        except Exception as e:
            st.error(f"Something went wrong while classifying: {e}")