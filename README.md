# Zero-Shot Topic Classification using BART Transformer Model

## Overview
This project implements a zero-shot topic classification system using the BART (BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension) transformer model. The system allows users to input text and possible topics, and the model predicts whether the text belongs to any of the specified topics, even if those topics were not seen during training.

## Kaggle Training
The model has been trained on Kaggle using the provided dataset. The training process involved fine-tuning the BART transformer model on a custom dataset to adapt it for zero-shot classification tasks.

## Requirements
- Python 3.x
- Streamlit
- Transformers library (Hugging Face)

## Installation
1. Clone this repository to your local machine.
2. Install the required Python packages by running:

pip install -r requirements.txt


## Usage
1. Run the `app.py` file using Streamlit:

streamlit run app.py

2. Once the Streamlit app is running, you will see a sidebar with model information and description.
3. Enter the text you want to classify in the provided text area.
4. Input possible topics separated by commas into the corresponding text area.
5. Click on the "Classify" button to get the classification results.
6. The app will display the predicted labels along with their confidence scores.
7. If no text or topics are entered, a warning message will be displayed.

## Model Details
- **Model Name:** facebook/bart-large-mnli
- **Task:** Zero-shot classification
- **Description:** BART model pre-trained on the Multi-Genre Natural Language Inference (MNLI) dataset with a classification head.
- **Link to Model:** [facebook/bart-large-mnli](https://huggingface.co/facebook/bart-large-mnli)

## Examples
You can choose from predefined examples or input your own text and topics for classification.

## Author
[Zilwa Mumtaz/Ziloeuvre]


