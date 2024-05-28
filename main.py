import streamlit as st
import glob
import plotly.express as px
from nltk.sentiment.vader import SentimentIntensityAnalyzer



# importing data using glob and sorting paths
filepaths = sorted(glob.glob('diary/*.txt'))


anazyler = SentimentIntensityAnalyzer()

# creating empty list
neg = []
pos = []

for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
        scores = anazyler.polarity_scores(content)
        pos.append(scores["pos"])
        neg.append(scores["neg"])
