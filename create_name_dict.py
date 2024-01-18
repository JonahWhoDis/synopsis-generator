import os
import json
import unicodedata
import re

def normalize_law_name(name):
    """
    Normalizes law names by converting German umlauts and special characters,
    and making the name lowercase.

    Args:
    name (str): The law name to normalize.

    Returns:
    str: The normalized law name.
    """
    # Convert to NFKD form which represents characters as their decomposed form
    name = unicodedata.normalize('NFKD', name)
    # Convert German umlauts and special characters
    name = name.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
    # Remove all non-alphanumeric characters except for spaces
    name = re.sub(r'[^a-zA-Z0-9\s]', '', name)
    # Convert to lowercase
    name = name.lower()
    return name


def read_law_json_files_with_normalization(directory_path):
    """
    Reads all JSON files in the given directory, extracts relevant information, and normalizes law names.
    
    Args:
    directory_path (str): The path to the directory containing JSON files.

    Returns:
    dict: A dictionary containing the extracted and normalized information from the JSON files.
    """
    law_data = {}
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
                # Extract relevant data from JSON
                law_id = json_data.get("data", {}).get("id", "")
                title_long = json_data.get("data", {}).get("titleLong", "")
                abbreviation = json_data.get("data", {}).get("abbreviation", "")
                # Normalize titles and abbreviation
                normalized_title_long = normalize_law_name(title_long)
                normalized_abbreviation = normalize_law_name(abbreviation)
                # Add to dictionary
                law_data[law_id] = {
                    "title_long": title_long,
                    "abbreviation": abbreviation,
                    "normalized_title_long": normalized_title_long,
                    "normalized_abbreviation": normalized_abbreviation,
                    "filename": filename
                }
    return law_data


def build_lookup_dictionary(law_data):
    """
    Builds a lookup dictionary from the law data, mapping various name variations to the filename.

    Args:
    law_data (dict): The dictionary containing the law data.

    Returns:
    dict: A lookup dictionary for law names.
    """
    lookup_dict = {}
    for law_id, data in law_data.items():
        # Original and normalized long title
        original_long_title = data['title_long']
        normalized_long_title = data['normalized_title_long']
        lookup_dict[original_long_title] = data['filename']
        lookup_dict[normalized_long_title] = data['filename']

        # Original and normalized abbreviation
        original_abbreviation = data['abbreviation']
        normalized_abbreviation = data['normalized_abbreviation']
        lookup_dict[original_abbreviation] = data['filename']
        lookup_dict[normalized_abbreviation] = data['filename']

    return lookup_dict


def find_law_file(lookup_dict, search_term):
    """
    Finds the file name of a law based on the search term.

    Args:
    lookup_dict (dict): The lookup dictionary for law names.
    search_term (str): The search term to find the law file.

    Returns:
    str: The filename of the law if found, otherwise an empty string.
    """
    search_term = search_term.strip()  # Remove leading/trailing whitespaces
    normalized_search_term = normalize_law_name(search_term)
    return lookup_dict.get(normalized_search_term, "")



law_data_normalized = read_law_json_files_with_normalization("/Users/jonah/Documents/GitHub/synopsis-generator/downloaded_jsons")
lookup_dict = build_lookup_dictionary(law_data_normalized)

# Beispiel, wie man die 'find_law_file' Funktion verwendet:
file_name = find_law_file(lookup_dict, " BEEG")
print(file_name)
