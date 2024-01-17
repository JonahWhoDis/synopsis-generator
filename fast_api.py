from fastapi import FastAPI, HTTPException
from typing import Dict, Any
import json

app = FastAPI()

@app.get("/law-text")
def get_law_text(book: str, paragraph: str, article: str) -> dict:
    """
    API endpoint to retrieve a specific section of a German law text.

    :param book: Name of the law book.
    :param paragraph: The specific paragraph within the book.
    :param article: The specific article within the paragraph.
    :return: A dictionary containing the requested law text.
    """
    try:
        law_book = read_law_book(book)
        law_text = extract_law_text(law_book, paragraph, article)
        return {"text": law_text}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))

# Note: The extract_law_text function assumes a specific structure of the JSON data.
# If your JSON structure is different, you'll need to adjust the logic accordingly.


def read_law_book(book_name: str, file_path: str = "path/to/law_books/") -> Dict[str, Any]:
    """
    Reads and parses a JSON file for a specified law book.

    :param book_name: Name of the law book to read.
    :param file_path: Path to the directory containing the law book JSON files.
    :return: Parsed JSON content of the law book.
    """
    try:
        with open(f"{file_path}{book_name}.json", 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Book '{book_name}' not found in the specified path.")
    except json.JSONDecodeError:
        raise ValueError(f"File for '{book_name}' is not a valid JSON.")


def extract_law_text(law_book: Dict[str, Any], paragraph: str, article: str) -> str:
    """
    Extracts and returns the law text corresponding to the specified paragraph and article
    from the provided law book data.

    :param law_book: The dictionary representation of the law book content.
    :param paragraph: The specific paragraph to search for.
    :param article: The specific article to search for.
    :return: The extracted law text.
    :raises KeyError: If the paragraph or article is not found.
    """
    # Adjusting the logic to match the new structure of the law book
    for content in law_book.get("data", {}).get("contents", []):
        if content.get("type") == "heading" and paragraph in content.get("title", ""):
            for sub_content in law_book.get("data", {}).get("contents", []):
                if sub_content.get("type") == "article" and sub_content.get("name") == article:
                    return sub_content.get("body", "No text available.")
    raise KeyError("Specified paragraph or article not found in the book.")



