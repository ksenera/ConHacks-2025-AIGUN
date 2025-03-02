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
from urllib.error import HTTPError
import yesg
from bs4 import BeautifulSoup
import requests


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

    


if __name__ == "__main__":
    scrapeProductData('https://www.amazon.ca/Blink-Outdoor-4th-Gen-1-Camera/dp/B0B1N7G2R1/ref=rvi_d_sccl_8/147-9657445-7161048?pd_rd_w=gdk1r&content-id=amzn1.sym.8b4d8c20-8e51-4634-a76f-c00a1995a502&pf_rd_p=8b4d8c20-8e51-4634-a76f-c00a1995a502&pf_rd_r=NQ895DA4GAHN0XX6CNRM&pd_rd_wg=oCbEj&pd_rd_r=e0687899-7ca3-498c-a8ca-f142564cb0cb&pd_rd_i=B0B1N7G2R1&th=1')
    
    time.sleep(1)