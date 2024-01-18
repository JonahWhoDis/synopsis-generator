import os
import json

def list_files_in_directory_to_json(directory_path, output_file):
    """
    Listet alle Dateien in einem Verzeichnis auf und speichert die Liste in einer JSON-Datei.

    Args:
    directory_path (str): Pfad zum Verzeichnis.
    output_file (str): Pfad zur JSON-Datei, in der die Liste gespeichert wird.
    """
    # Liste aller Dateien im Verzeichnis
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # Speichern der Liste in einer JSON-Datei
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(files, file, ensure_ascii=False, indent=4)

# Verwendung des Skripts
list_files_in_directory_to_json("/Users/jonah/Documents/GitHub/synopsis-generator/downloaded_jsons", "file_names.json")
