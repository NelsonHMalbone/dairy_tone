import streamlit as st
import glob
from pathlib import Path
import plotly.express as px
import regex as re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
def main():

    corpus = []
    # importing data using glob
    filepaths = glob.glob('diary/*.txt')


    for nr, filepath in enumerate(filepaths):
        with open(filepath, "r") as file:
            content = file.read()
            corpus.append(content)
            print(nr + 1, corpus)

    # looking at the pos and neg of each file
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(content)
    print()

    if scores ['pos'] > scores ['neg']:
        print("its positive")
    else:
        print("its negative")







    # setting up webpage
    st.title("Diary Tone")

    # Positivity Section
    # positivity header
    st.subheader("Positivity")

    # Negativity Section
    # negativity header
    st.subheader("Negativity")

if __name__ == "__main__":
    main()