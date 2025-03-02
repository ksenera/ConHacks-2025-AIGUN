from newsapi import NewsApiClient
from bs4 import BeautifulSoup
import requests
from flask import Blueprint
import os
from dotenv import load_dotenv
import newsapi
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
    return company.strip('\u200e')


@scraper_page.route('/api/news/<company_name>')
def get_news_data(company_name: str):
    keywords = ['environmental', 'governence', 'score', 'sustainability', 'esg', 'esg score']
    client = NewsApiClient(api_key=NEWS_API_KEY)

    # Fetch headlines and sort by relevancy
    query = f'{company_name} AND ({f" OR ".join(keywords)})'
    response = client.get_everything(qintitle=query, language="en", sort_by=list(newsapi.const.sort_method)[2])
    
    recent = response['articles'][:5]
    
    return recent


if __name__ == '__main__':
    print(get_product_manufacturer('https://www.amazon.ca/BLACK-DECKER-HG1300-Dual-Temperature/dp/B004NDX7O6/ref=pd_ci_mcx_mh_mcx_views_0_image?pd_rd_w=UjJ8e&content-id=amzn1.sym.40e66fa0-07fe-4f96-a189-672cdabaab3c%3Aamzn1.symc.1065d246-0415-4243-928d-c7025bdd9a27&pf_rd_p=40e66fa0-07fe-4f96-a189-672cdabaab3c&pf_rd_r=AHP8B35TX72KJQTGJCDJ&pd_rd_wg=mSVzc&pd_rd_r=70b31443-0072-4973-ad5a-654a86fe111e&pd_rd_i=B004NDX7O6&th=1'))
    print(get_product_manufacturer('https://www.amazon.ca/Hello-Kitty-Island-Adventure-Nintendo/dp/B0DSQXNZQR?crid=3E2C9JOKE3BL0&dib=eyJ2IjoiMSJ9.m4N-eg7UrvO3hb_E--QZNfJl5uJ2OrevBZ2wV4PHlUM59F4AodLJ1TnP7mn-IpQLrPoBQNtbZ2sLWSl8lewSJ5v_efqc_GWFi1MnUDJY1lafKmOzdmTrdhoUjx_9WjZVFFlPrnYZSOmrflRfB-kduRb49ZT2ojiYqB06nK7iMrNQdUrja7yfJ2elhqM9UvoWFIWVagx23WQ2ynwuB9jFoKVZnpwucJqH3gVuvKv9jj2P4NsDAEHIC8UxdHkcKZjHTWq-iLxlIrdaPyuBf0Dlw9y8_JlR9xeXZIwXxzN6X6Q.fZVR0fFeVvzw3eqaXCZfeVeVx8mNas0XlyQC2SATTSM&dib_tag=se&keywords=hello+kitty+game&qid=1740864384&sprefix=hello+kitty+gam%2Caps%2C103&sr=8-4'))
    print(get_product_manufacturer("https://www.amazon.ca/dp/B07T3KCQ94/ref=syn_sd_onsite_desktop_0?ie=UTF8&pf_rd_p=1b46b9a6-7460-404c-a963-dcc870e8a6a7&pf_rd_r=MA6NZZKB81FZB59D2QV0&pd_rd_wg=NLLJZ&pd_rd_w=K0eb4&pd_rd_r=46ee66a9-6119-4b23-abb4-b3c3c0769a15&aref=9y7Ja79Wbm&th=1"))
    print(get_product_manufacturer('https://www.amazon.ca/HUANUO-Monitor-Screens-4-4-26-4lbs-Compatible/dp/B08CXG57ZX/ref=pd_ci_mcx_pspc_dp_2_t_2?pd_rd_w=Tt7Td&content-id=amzn1.sym.03d0a222-babc-4fe5-b7df-e90dd70bc007&pf_rd_p=03d0a222-babc-4fe5-b7df-e90dd70bc007&pf_rd_r=CY63J7G8WTT1Y7P2PX3S&pd_rd_wg=XrHqq&pd_rd_r=d6d50f49-1569-4c91-9dcd-3cb13640e322&pd_rd_i=B08CXG57ZX'))
    print(get_product_manufacturer('https://www.amazon.ca/Thrustmaster-Simulator-Feedback-Officially-Licensed/dp/B0BWFQN4WY?pd_rd_w=QlNFv&content-id=amzn1.sym.e0b5b8df-c7a3-4462-b3fb-639731524e88&pf_rd_p=e0b5b8df-c7a3-4462-b3fb-639731524e88&pf_rd_r=8JZG5JYN0EFXH22Y8408&pd_rd_wg=wOPiL&pd_rd_r=fcec66a5-54c4-40de-a5cd-30d2f32c32c5&pd_rd_i=B0BWFQN4WY&ref_=pd_hp_d_btf_unk_B0BWFQN4WY'))