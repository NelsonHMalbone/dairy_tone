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

date = [name.strip(".txt").strip("diary/") for name in filepaths]

st.title("Diary Tone")
st.subheader("Positivity")
pos_graph = px.line(x=date,
                    y=pos,
                    labels={"x": "Date", "y": "positivity"})
st.plotly_chart(pos_graph)

st.subheader("Negativity")
neg_graph = px.line(x=date,
                    y=neg,
                    labels={"x": "Date", "y": "negativity"})
st.plotly_chart(neg_graph)