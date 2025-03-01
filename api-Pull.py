import requests
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
KEY = os.getenv('NEWS_API_KEY')

# Initialize API client
api = NewsApiClient(api_key=KEY)

# Fetch top headlines from BBC News
response = api.get_top_headlines(sources='bbc-news')

# Print the first article if available
if response and response.get('articles'):
    article = response['articles'][0]  # Get the first article
    print(f"Title: {article['title']}\nDescription: {article['description']}\nURL: {article['url']}\n")
else:
    print("No articles found.")
