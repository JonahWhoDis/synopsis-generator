import requests

def test_get_law_text(book, article, paragraph):
    base_url = "http://127.0.0.1:8000"  # Change to the URL API when deployed TODO
    response = requests.get(f"{base_url}/law-text", params={"book": book, "paragraph": paragraph, "article": article})
    if response.status_code == 200:
        print(f"Success: {response.json()}")
    else:
        print(f"Error: {response.status_code}")

# Test cases
test_get_law_text("1_dm_goldmuenzg", "2", "1")
test_get_law_text("1_dm_goldmuenzg", "18", "2")
