import requests
from bs4 import BeautifulSoup
import os

# URL der Webseite
url = "https://gadi.netlify.app/"

def download_json(link, count):
    response = requests.get(link)
    if response.status_code == 200:
        json_content = response.content
        filename = link.split("/")[-1]
        with open(filename, 'wb') as file:
            file.write(json_content)
        print(f"Downloaded ({count}): {filename}")

def main(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        count = 0
        print("Downloading JSON files number ${count}")
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if href.endswith('.json'):
                json_link = url + href
                count += 1
                download_json(json_link, count)

if __name__ == "__main__":
    os.makedirs('downloaded_jsons', exist_ok=True)
    os.chdir('downloaded_jsons')
    main(url)
