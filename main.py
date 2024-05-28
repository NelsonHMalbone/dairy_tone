import streamlit as st
import glob
import plotly.express as px
import regex as re
from nltk.sentiment import SentimentIntensityAnalyzer
def main():


    # importing data using glob
    filepaths = glob.glob('diary/*.txt')

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