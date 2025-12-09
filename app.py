import streamlit as st
# VADER sentiment Score
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
import nltk
nltk.download('vader_lexicon')

st.title('Sentiment Analysis Dashboard')
st.subheader('This Dashboard will provide you a sentiment score for a partucular text.')



text = st.text_input('Enter your text: ')
btn = st.button('Get Sentiment')


def get_sentiment(text):
    scores = sia.polarity_scores(text)
    return scores

if btn:
     scores = get_sentiment(text)

     if scores['compound'] >= 0.05:
        st.write('Positive Sentiment')
     elif scores['compound'] <= -0.05:
        st.write('Negative Sentiment')
     else:
        st.write('Neutral Sentiment')
     
    
       






