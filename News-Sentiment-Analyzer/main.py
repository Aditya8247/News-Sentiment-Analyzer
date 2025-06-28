import os
from news.fetcher import fetch_news
from analysis.sentiment import process_news_data
from visualize.dashboard import plot_sentiment_distribution, plot_polarity_trend



# Step 1: Fetch News
news_data = fetch_news(query='stock')


# Step 2: Analyze Sentiment
df = process_news_data(news_data)

# Step 3: Save to CSV
os.makedirs('data', exist_ok=True)
df.to_csv('data/news_sentiment.csv', index=False)
print("Data saved to 'data/news_sentiment.csv'")

# Step 4: Visualize
plot_sentiment_distribution(df)
plot_polarity_trend(df)



