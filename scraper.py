#from newsapi import NewsApiClient
from bs4 import BeautifulSoup
import requests
from flask import Blueprint
import os
from dotenv import load_dotenv
#import newsapi
import re
    
load_dotenv()
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
scraper_page = Blueprint(name='scraper_page', import_name=__name__)


@scraper_page.route('/api/get_manufacturer/<url>')
def get_product_manufacturer(url: str):
    response = requests.get(url)
    
    if response.status_code != 200:
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # get anything on page that refers to manufacturer
    # this might be more Amazon specific but it could be set up to work
    # on many other websites once formats are analyzed 
    manufacturer_info = soup.find_all(string=re.compile('Manufacturer'))
    for item in manufacturer_info:
        parent = item.parent
        next_sibling = parent.find_next_sibling()
        if next_sibling:
            company = next_sibling.string.strip()
            break
    return company


@scraper_page.route('/api/news/<company_name>')
def get_news_data(company_name: str):
    keywords = ['environmental', 'environment', 'sustainability', 'sustainable', 'governance', 'esg']
    client = NewsApiClient(api_key=NEWS_API_KEY)

    # Fetch headlines and sort by relevancy
    response = client.get_everything(q=f'{company_name} AND {f" OR ".join(keywords)}', language="en", sort_by=newsapi.const.sort_method[2])
    
    return response


if __name__ == '__main__':
    get_product_manufacturer('https://www.amazon.ca/BLACK-DECKER-HG1300-Dual-Temperature/dp/B004NDX7O6/ref=pd_ci_mcx_mh_mcx_views_0_image?pd_rd_w=UjJ8e&content-id=amzn1.sym.40e66fa0-07fe-4f96-a189-672cdabaab3c%3Aamzn1.symc.1065d246-0415-4243-928d-c7025bdd9a27&pf_rd_p=40e66fa0-07fe-4f96-a189-672cdabaab3c&pf_rd_r=AHP8B35TX72KJQTGJCDJ&pd_rd_wg=mSVzc&pd_rd_r=70b31443-0072-4973-ad5a-654a86fe111e&pd_rd_i=B004NDX7O6&th=1')
    get_product_manufacturer('https://www.amazon.ca/Hello-Kitty-Island-Adventure-Nintendo/dp/B0DSQXNZQR?crid=3E2C9JOKE3BL0&dib=eyJ2IjoiMSJ9.m4N-eg7UrvO3hb_E--QZNfJl5uJ2OrevBZ2wV4PHlUM59F4AodLJ1TnP7mn-IpQLrPoBQNtbZ2sLWSl8lewSJ5v_efqc_GWFi1MnUDJY1lafKmOzdmTrdhoUjx_9WjZVFFlPrnYZSOmrflRfB-kduRb49ZT2ojiYqB06nK7iMrNQdUrja7yfJ2elhqM9UvoWFIWVagx23WQ2ynwuB9jFoKVZnpwucJqH3gVuvKv9jj2P4NsDAEHIC8UxdHkcKZjHTWq-iLxlIrdaPyuBf0Dlw9y8_JlR9xeXZIwXxzN6X6Q.fZVR0fFeVvzw3eqaXCZfeVeVx8mNas0XlyQC2SATTSM&dib_tag=se&keywords=hello+kitty+game&qid=1740864384&sprefix=hello+kitty+gam%2Caps%2C103&sr=8-4')
    