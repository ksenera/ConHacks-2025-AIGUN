import requests
import yfinance as yf
import json
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")

def get_ticker(company_name: str):
    search_result = yf.Search(company_name)
    ticker = search_result.response['quotes'][0]['symbol']
    
    return ticker


def get_esg_raw(company_name: str):
    ticker = get_ticker(company_name)
    
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
    response = requests.get('https://query2.finance.yahoo.com/v1/finance/esgChart', params={"symbol": ticker}, headers=headers)
    
    if response.status_code != 200:
        return None
    
    return response.content


def get_esg_series(esg_raw: bytes):
    data = json.loads((esg_raw))
    symbol_series = data['esgChart']['result'][0]['symbolSeries']
    peer_series = data['esgChart']['result'][0]['peerSeries']
    
    symbol_series.pop('timestamp')
    peer_series.pop('timestamp')
    
    return (symbol_series, peer_series)


def get_summary(company_name: str, esg_raw_data: bytes = None):
    esg_data = get_esg_raw(company_name) if esg_raw_data is None else esg_raw_data
    
    if esg_data is None:
        return f"An ESG score couldn't be found for {company_name}"
    
    series_data = get_esg_series(esg_data)
    
    client = OpenAI(api_key=OPEN_AI_KEY)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": f"write a short summary of the esg data for {company_name} in point form informing the consumer if this product has a good or bad esg score and why. DO NOT INCLUDE symbol or peer series data. Only provide the summary in plain text NOT IN MARKDOWN and provide a breif score beside each main point, for example \"Environmental Score: Good\". Historical esg data in json format {company_name} attached below\n Symbol Series: {series_data[0]} Peer Series {series_data[1]}"}
        ]
    )
    
    return completion.choices[0].message.content

    