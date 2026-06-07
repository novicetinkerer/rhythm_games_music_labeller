import requests
from bs4 import BeautifulSoup

def fetch_metadata(url: str) -> dict:
    """Fetch metadata from Remy.

    This assumes Remy exposes JSON data at the given URL or an API endpoint.
    """

    fetch_status = 69

    response = requests.get(url)
    return_info = {}
    if response.status_code != 200:
        fetch_status = -1
        return_info = response.status_code
        
    else:
        fetch_status = 0
        soup = BeautifulSoup(response.text, 'html.parser')

        title_unicode = soup.find('span', class_='mw-page-title-main').text.strip()
        title_romanized = soup.find('div', class_='mw-heading mw-heading1').text.strip()

        return_info = {
            'title': title_unicode,
            'title_romanized': title_romanized,
        }

    return { fetch_status: return_info }
