# synopsis-generator

## Überblick

Der Synopsis-Generator ist eine OpenAPI-basierte Anwendung, die speziell entwickelt wurde, um auf alle Gesetzesbücher des Bundes zuzugreifen. 
Diese API ermöglicht es Benutzern, spezifische Informationen aus einer Vielzahl von Gesetzestexten abzurufen, indem sie Anfragen an den Synopsis-Generator stellen.

## Funktionsweise

Die API verwendet FastAPI. Es gibt noch einige weitere skripte, die aber nur verwendet wurden um die Datenbank zu erstellen.
An dieser Stelle möchte ich mich bei [@nfelger](https://github.com/nfelger) bedanken für die Bereitstellung der Gestzestexte.
Bitte besucht seine Webseite: https://gadi.netlify.app/
Ihr könnt anschließend mein Script crawler.py verwenden um euch alle Gesetzestexte herunterzuladen.

## Endpunkte

- `GET /law-text`: Dieser Endpunkt ermöglicht es Benutzern, spezifische Absätze aus einem Artikel in einem deutschen Gesetzestext abzurufen. 
Die Benutzer müssen den Namen des Gesetzbuches, den Artikel und den Absatz angeben.

## Nutzung

Um die API zu nutzen, senden Sie eine HTTP-Anfrage an den entsprechenden Endpunkt. Hier ist ein Beispiel, wie Sie den `/law-text` Endpunkt verwenden können:
GET /law-text?book=BGB&article=241&paragraph=2


Diese Anfrage würde den Text des zweiten Absatzes des Artikels 241 im Bürgerlichen Gesetzbuch (BGB) zurückgeben.

## Installation und Einrichtung

Zur Installation und Einrichtung der Synopsis-Generator API folgen Sie bitte diesen Schritten:

1. Klonen Sie das Repository.
2. Installieren Sie die erforderlichen Abhängigkeiten.
3. Führen Sie die API mit einem geeigneten ASGI-Server aus.

## Logging

Die API protokolliert Anfragen und Antworten, um die Überwachung und Fehlersuche zu erleichtern. Die Protokolle werden in eine Datei `app.log` geschrieben.

## Sicherheit und Datenschutz

Es werden keine persönlichen Daten der Benutzer gespeichert oder verarbeitet.

## Beitrag und Unterstützung

Für Beiträge zum Projekt oder Unterstützungsanfragen öffnen Sie bitte ein Issue im GitHub-Repository oder senden Sie eine Pull-Anfrage.

---

Hinweis: Dieses Dokument ist eine grundlegende Anleitung zur Verwendung der Synopsis-Generator API und erhebt keinen Anspruch auf Vollständigkeit. 



