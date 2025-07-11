"""
Haupt-Einstiegspunkt für das Buchanalyse-Programm.

Dieses Skript führt folgende Aufgaben aus:
- Lädt Buchinhalte und Metadaten mithilfe des Moduls `load_file`.
- Startet den Analyseprozess über das Modul `Analyesewunsch`, insbesondere die Klasse `Count`.

Dieses Skript wird nur ausgeführt, wenn es direkt gestartet wird (nicht beim Import).

Module:
    - load_file: Enthält Funktionen zum Einlesen der Buchinhalte und Extrahieren von Titel/Autor.
    - Analyesewunsch: Enthält die Klasse `Count` für interaktive Wort- und Textstatistiken.

Fehlerbehandlung:
    Gibt eine formatierte Fehlermeldung aus, falls beim Laden oder bei der Analyse ein unerwarteter Fehler auftritt.
"""
import load_file as load
import Analyesewunsch as Analyes

if __name__ == "__main__":  # Nur ausführen, wenn dieses Skript direkt gestartet wird.
    try:
        dic_book = load.read_file()        # Bücher und Metadaten einlesen
        Analyes.Count(dic_book)            # Analyse starten
    except Exception as e:
        print(f"[Fehler] Es ist ein Fehler aufgetreten: {e}")
