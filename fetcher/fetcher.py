import requests

PRICE_AREA_TAG = "SN"

def get_price_blob(price_source, start_date, end_date, price_area):
    url = get_price_url(price_source, start_date, end_date, price_area)
    return fetch_json(url)


def get_price_url(price_source, start_date, end_date, price_zone):
    return f"{price_source}/{start_date}/{end_date}/{PRICE_AREA_TAG}{price_zone}"


def fetch_json(url):
    try:
        headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
