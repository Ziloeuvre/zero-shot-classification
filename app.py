# app.py

import streamlit as st
from transformers import pipeline

class ZeroShotClassifier:
    def __init__(self, task, model):
        self.model = model
        self.task = task
        self.pipe = pipeline(task=self.task, model=self.model)
    
    def classify_topic(self, text, topics):
        topic_labels = [f'This text is about {topic}.' for topic in topics.split(",")]
        result = self.pipe(text, topic_labels)
        return result


if __name__ == "__main__":
    st.sidebar.title("Model")
    st.sidebar.write("BART Multi Natural Language Inference (MNLI)")
    st.sidebar.title("Model Description")
    st.sidebar.write("BART with a classification head trained on MNLI.")
    st.sidebar.write("\n")
    st.sidebar.write("Enter text and possible topics to classify the text.")

    st.title("Zero-Shot Text Classification 😍")
    st.selectbox(
        "Choose an example", [
            "One day I will see the world",
            "I love to play video games"
        ])

    text_input = st.text_area("Text")
    topics_input = st.text_input("Possible topics (comma-separated)", max_chars=1000)

    task = "zero-shot-classification"
    model = "facebook/bart-large-mnli"
    classifier = ZeroShotClassifier(task, model)
    
    if st.button("Classify"):
        if text_input and topics_input:
            predictions = classifier.classify_topic(text_input, topics_input)
            for i, pred in enumerate(predictions['labels']):
                st.write(f"{pred}: {predictions['scores'][i]*100:.2f}%")

            st.bar_chart(predictions['scores'])
        else:
            st.warning("Please enter both text and topics.")