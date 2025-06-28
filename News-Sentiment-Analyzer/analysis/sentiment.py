from textblob import TextBlob
import pandas as pd

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.01:
        sentiment = 'Positive'
    elif polarity < -0.01:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    return sentiment, polarity

def process_news_data(news_data):
    df = pd.DataFrame(news_data)
    df[['Sentiment', 'Polarity']] = df['title'].apply(lambda x: pd.Series(analyze_sentiment(x)))
    return df
