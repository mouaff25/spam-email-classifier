import gradio as gr
from joblib import load
import numpy as np
from sklearn.pipeline import Pipeline
import pandas as pd

spam_classifier: Pipeline = load("./models/spam_classifier.joblib")

def greet(email_body: str) -> float:
    model_input = pd.DataFrame([email_body], columns=["Message"])
    prediction = spam_classifier.predict_proba(model_input)[0][1]
    return prediction

demo = gr.Interface(fn=greet, inputs="text", outputs="number")
    
demo.launch()