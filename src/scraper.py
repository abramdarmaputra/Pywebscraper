import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def build_session():
    s = requests.Session()
    retry = Retry(total=5, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
    s.mount("http://", HTTPAdapter(max_retries=retry))
    s.mount("https://", HTTPAdapter(max_retries=retry))
    return s

def fetch_html(session, url):
    r = session.get(url)
    r.raise_for_status()
    return r.text
    