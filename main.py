import streamlit as st
import glob
import plotly.express as px
from nltk.sentiment.vader import SentimentIntensityAnalyzer



# importing data using glob and sorting paths
filepaths = glob.glob('diary/*.txt')
filepaths_sorted = sorted(filepaths)

print(filepaths_sorted)
