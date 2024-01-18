import requests
import subprocess

def ping_server(host):
    try:
        subprocess.check_output(["ping", "-c", "4", host])
        print(f"Success: Server {host} is reachable.")
    except subprocess.CalledProcessError:
        print(f"Error: Server {host} is not reachable.")

def test_get_law_text(book, article, paragraph):
    base_url = "https://synopsis-generator.de"  # Replace with your server IP and port
    try:
        response = requests.get(f"{base_url}/law-text", params={"book": book, "article": article, "paragraph": paragraph})
        if response.status_code == 200:
            print(f"Success: {response.json()}")
        else:
            print(f"Error: Status code {response.status_code}, Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")

# Check server accessibility
ping_server("https://synopsis-generator.de")

# Test API endpoint
test_get_law_text("1_dm_goldmuenzg", "2", "1")
test_get_law_text("1_dm_goldmuenzg", "18", "2")
