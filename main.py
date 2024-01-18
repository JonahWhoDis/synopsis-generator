from fastapi import FastAPI, HTTPException, Request
from typing import Dict, Any
import json
import re
import logging
from starlette.responses import Response

app = FastAPI()

logging.basicConfig(filename='app.log', level=logging.INFO)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    request_log = f"Request: {request.method} {request.url} Query Params: {request.query_params}"
    response_log = f"Response Status: {response.status_code}"
    logging.info(request_log)
    logging.info(response_log)
    return response


@app.get("/law-text")
def get_law_text(book: str, article: str, paragraph: str) -> dict:
    """
    API endpoint to retrieve a specific paragraph of an article in a German law text.

    :param book: Name of the law book.
    :param article: The specific article within the book.
    :param paragraph: The specific paragraph number within the article.
    :return: A dictionary containing the requested paragraph text.
    """
    try:
        law_book = read_law_book(book)
        paragraph_text = extract_law_text(law_book, article, paragraph)
        return {"text": paragraph_text}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
def read_law_book(book_name: str, file_path: str = "/synopsis-generator/synopsis-generator/downloaded_jsons/") -> Dict[str, Any]:
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


def extract_law_text(law_book: Dict[str, Any], article_name: str, paragraph_number: str) -> str:
    """
    Extracts and returns the specified paragraph of the law text corresponding to the specified article
    from the provided law book data.

    :param law_book: The dictionary representation of the law book content.
    :param article_name: The specific article name to search for.
    :param paragraph_number: The specific paragraph number within the article.
    :return: The extracted paragraph text.
    :raises KeyError: If the article or paragraph is not found.
    """
    for content in law_book.get("data", {}).get("contents", []):
        if content.get("type") == "article" and content.get("name") == '\u00a7 ' + article_name:
            paragraphs = re.findall(r"<P>\((\d+)\) (.*?)</P>", content.get("body", ""))
            for num, para_text in paragraphs:
                if num == paragraph_number:
                    return para_text
            raise KeyError(f"Paragraph '{paragraph_number}' not found in article '{article_name}'.")
    raise KeyError(f"Article '{article_name}' not found in the book.")