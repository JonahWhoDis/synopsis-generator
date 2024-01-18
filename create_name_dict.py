import os
import json

def read_law_json_files(directory_path):
    """
    Reads all JSON files in the given directory and extracts relevant information.
    
    Args:
    directory_path (str): The path to the directory containing JSON files.

    Returns:
    dict: A dictionary containing the extracted information from the JSON files.
    """
    law_data = {}
    count = 0
    for filename in os.listdir(directory_path):
        count += 1
        if count > 10:
            break
        if filename.endswith(".json"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
                # Extract relevant data from JSON
                law_id = json_data.get("data", {}).get("id", "")
                title_long = json_data.get("data", {}).get("titleLong", "")
                abbreviation = json_data.get("data", {}).get("abbreviation", "")
                # Add to dictionary
                law_data[law_id] = {
                    "title_long": title_long,
                    "abbreviation": abbreviation,
                    "filename": filename
                }
    return law_data


law_data = read_law_json_files("/Users/jonah/Documents/GitHub/synopsis-generator/downloaded_jsons")
print(law_data)
