import streamlit as st
import glob
from pathlib import Path
import plotly.express as px
import regex as re
from nltk.sentiment.vader import SentimentIntensityAnalyzer



# importing data using glob
filepaths = glob.glob('diary/*.txt')
corpus = []

for nr, filepath in enumerate(filepaths):

    with open(filepath, "r") as file:
        content = file.read()
        corpus.append(content)
print(nr + 1, corpus)