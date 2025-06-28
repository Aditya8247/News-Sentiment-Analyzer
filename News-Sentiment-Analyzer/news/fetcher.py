import requests

API_KEY = '3ba9ded73b514da49524ab0e0d89f2ca'  # Replace with your key
BASE_URL = 'https://newsapi.org/v2/everything'


def fetch_news(query='technology',  page_size=20):
    params = {
        'apiKey': API_KEY,
        'q': query,
        'pageSize': page_size,
        'sortBy': 'publishedAt',
        'language': 'en'
    }

    response = requests.get(BASE_URL, params=params)
    articles = response.json().get('articles', [])

    headlines = []
    for article in articles:
        headlines.append({
            'date': article['publishedAt'][:10],
            'source': article['source']['name'],
            'title': article['title']
        })
    return headlines
