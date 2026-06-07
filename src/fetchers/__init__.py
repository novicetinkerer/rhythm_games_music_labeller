from .remy_fetcher import fetch_metadata as fetch_remy_metadata


FETCHERS = {
    'remy': fetch_remy_metadata,
}


def get_fetcher_for_url(url: str):
    if 'remy' in url.lower():
        return fetch_remy_metadata
    raise ValueError(f'No fetcher available for URL: {url}')
