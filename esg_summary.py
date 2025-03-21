import requests
import yfinance as yf
import json
from dotenv import load_dotenv
import os
from openai import OpenAI
from flask import Blueprint
from flask import jsonify

esg_summary_page = Blueprint(name='esg_summary_page', import_name=__name__)

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
    
    try:
        symbol_series = data['esgChart']['result'][0]['symbolSeries']
        peer_series = data['esgChart']['result'][0]['peerSeries']
    except:
        return None
    
    symbol_series.pop('timestamp')
    peer_series.pop('timestamp')
    
    return (symbol_series, peer_series)


@esg_summary_page.route('/api/summary/<company_name>')
def get_summary(company_name: str):
    esg_data = get_esg_raw(company_name)
    if esg_data is None:
        return f"An ESG score couldn't be found for {company_name}"
    
    series_data = get_esg_series(esg_data)
    if series_data is None:
        return f"ESG score for {company_name} was not complete"
    
    client = OpenAI(api_key=OPEN_AI_KEY)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant that must output ONLY valid JSON. No extra text or markdown. Just JSON with the keys: environmental.score, environmental.description, social.score, social.description, governance.score, governance.description, overall.score, overall.description."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Provide a short summary of the esg data for {company_name} in the JSON structure described. Do NOT include symbol or peer series data. Historical esg data in JSON format below:\n. Symbol Series: {series_data[0]} Peer Series: {series_data[1]}\n. Again, output ONLY valid JSON, no extra text, no markdown."
                )
            }
        ]
    )
    
    raw_json = completion.choices[0].message.content.strip()
    try:
        data = json.loads(raw_json)
        return jsonify(data)
    except json.JSONDecodeError:
        return raw_json
    

    