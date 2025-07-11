import os  # Zum Arbeiten mit Dateipfaden und Dateien

# Dynamischer Pfad zum Ordner „books“
BASE_PATH = os.path.dirname(__file__)
BOOKS_PATH = os.path.join(BASE_PATH, "books")


def read_file():
    """
    Liest alle Textdateien im Verzeichnis „books“ ein, extrahiert Titel- und Autoreninformationen
    und gibt die verfügbaren Bücher mit ihren Metadaten aus.

    Rückgabe:
        dict: Ein Wörterbuch, in dem die Dateinamen als Schlüssel und eine Liste mit Titel und Autor/Übersetzer
              als Werte gespeichert sind.
              Beispiel: {'buch1.txt': ['Buchtitel', 'Autorenname']}

    Ausgabe:
        - Liste der verfügbaren Bücher mit den extrahierten Metadaten.
        - Fehlermeldungen, wenn der Ordner „books“ nicht gefunden wird oder eine Datei nicht gelesen werden kann.
    """
    try:
        all_files = os.listdir(BOOKS_PATH)
    except FileNotFoundError:
        print(f"[❌ Fehler] Der Bücherordner wurde nicht gefunden: {BOOKS_PATH}")
        return {}

    print(" 👉 Verfügbare Bücher:\n", "-" * 100)
    dic_n_t_book = {}

    for filename in all_files:
        file_path = os.path.join(BOOKS_PATH, filename)
        try:
            with open(file_path, mode="r", encoding='utf-8') as book:
                content = book.read()
                info = extract_title_author(content)
                dic_n_t_book[filename] = info
                print("-" * 100)
        except Exception as e:
            print(f"[❗ Fehler beim Lesen der Datei {filename}]: {e}")

    return dic_n_t_book


def extract_title_author(text):
    """
    Extrahiert den Titel und den Autor (bzw. den Übersetzer, falls kein Autor angegeben ist) aus dem Textinhalt eines Buchs.

    Parameter:
        text (str): Der vollständige Textinhalt eines Buchs.

    Rückgabe:
        list: Eine Liste mit dem extrahierten Titel und Autor oder Übersetzer.
              Format: [Titel, Autor_Oder_Übersetzer]

    Ausgabe:
        - Der extrahierte Titel und Autor (oder Übersetzer) wird auf der Konsole angezeigt.
    """
    title = ""
    author = ""

    for line in text.splitlines():
        line = line.strip()

        if line.startswith("Title:"):
            title = line.replace("Title:", "").strip()
            print(f"\t📗 Titel: {title}")

        elif line.startswith("Author:"):
            author = line.replace("Author:", "").strip()
            print(f"\t👤 Autor: {author}")

        elif line.startswith("Translator:") and not author:
            author = line.replace("Translator:", "").strip()
            print(f"\t👤 Übersetzer: {author}")

    return [title, author]
