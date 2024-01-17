import requests
from bs4 import BeautifulSoup

url = "https://gadi.netlify.app/"

def count_json_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        json_links = [a_tag['href'] for a_tag in soup.find_all('a', href=True) if a_tag['href'].endswith('.json')]
        return len(json_links)
    return 0

if __name__ == "__main__":
    json_count = count_json_links(url)
    print(f"Anzahl der JSON-Links auf der Seite: {json_count}")
