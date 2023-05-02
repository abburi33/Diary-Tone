import streamlit as st
import plotly.express as px
import glob
from pathlib import Path

from nltk.sentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

files = sorted(glob.glob("diary/*.txt"))
dates = [Path(file).stem for file in files]
pos_scores=[]
neg_scores=[]
for file in files:
    with open(file, "r") as f:
        content = f.read()
    mood = analyzer.polarity_scores(content)
    pos_scores.append(mood['pos'])
    neg_scores.append(mood['neg'])

st.title("Diary Tone")

st.subheader("Positivity")
pos_graph = px.line(x=dates, y=pos_scores, labels={"x":"Date", "y":"Positivity"})
st.plotly_chart(pos_graph)

st.subheader("Negativity")
neg_graph = px.line(x=dates, y=neg_scores, labels={"x":"Date", "y":"Negativity"})
st.plotly_chart(neg_graph)

