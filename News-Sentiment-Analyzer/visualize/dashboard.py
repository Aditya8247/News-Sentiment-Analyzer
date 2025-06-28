import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_sentiment_distribution(df):
    plt.figure(figsize=(6, 4))
    sns.countplot(x='Sentiment', hue='Sentiment', data=df, palette='coolwarm', legend=False)
    plt.title("Sentiment Distribution of News Headlines")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

def plot_polarity_trend(df):
    df['date'] = pd.to_datetime(df['date'])
    daily_avg = df.groupby('date')['Polarity'].mean()
    daily_avg.plot(marker='o', figsize=(8,4), title="Average Sentiment Over Time")
    plt.ylabel("Avg Polarity")
    plt.xlabel("Date")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
