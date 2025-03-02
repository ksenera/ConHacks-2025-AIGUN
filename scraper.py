"""import requests
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
import json
from json import dumps, load
from flask import Flask, jsonify
import yesg
import time

# Load environment variables
#app = Flask(__name__)

#@app.route('/News')
#def sendNewsData():

    #load_dotenv()

    # Get API key
    #KEY = os.getenv('NEWS_API_KEY')

    # Initialize API client
    #api = NewsApiClient(api_key=KEY)

    # Fetch top headlines from BBC News
    #response = api.get_top_headlines(q='wells fargo', language="en")


    # Print the first article if available

#app = Flask(__name__)
#@app.route('/ESG')
def get_esg_scores():
    try:
        # Add a delay before making the request
        time.sleep(1)

        # Get ESG data for 'BA' (Boeing)
        esg_data = yesg.get_esg_full('BA').to_string()

        # Print or log the ESG data for debugging purposes
        print(esg_data)

        # Return the ESG data as a JSON response
        return jsonify({"esg_data": esg_data})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    #app.run()
    get_esg_scores()"""

import time
from newsapi import NewsApiClient
from bs4 import BeautifulSoup
import requests
from flask import Blueprint
import os
from dotenv import load_dotenv
import newsapi
    
load_dotenv()
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
scraper_page = Blueprint(name='scraper_page', import_name=__name__)

def scrapeProductData(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    brand_info = soup.find('a', {'id': 'bylineInfo'})
    brand_name = brand_info.text.strip()
    if brand_name[0] == 'V':
        brand_name = brand_name[10:]
        brand_name = brand_name[:5]
        print(f"{brand_name}")
        time.sleep(1)
    else:
        print(f"{brand_name}")


@scraper_page.route('/api/news/<company_name>')
def get_news_data(company_name: str):
    keywords = ['environmental', 'environment', 'sustainability', 'sustainable', 'governance', 'esg']
    client = NewsApiClient(api_key=NEWS_API_KEY)

    # Fetch headlines and sort by relevancy
    response = client.get_everything(q=f'{company_name} AND {f" OR ".join(keywords)}', language="en", sort_by=newsapi.const.sort_method[2])
    
    return response

    