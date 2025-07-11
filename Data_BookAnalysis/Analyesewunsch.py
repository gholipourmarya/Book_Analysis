import load_file as load
from colorama import Fore, Style


class Count:
    """
    Führt Textanalysen für eine Sammlung von Büchern durch.
    Ermöglicht die Zählung von Leerzeichen, Wörtern, Zeilen und eines bestimmten Suchworts.
    """

    def __init__(self, file_book):
        """
        Initialisiert die Count-Klasse mit Buchdaten und startet das Auswahlmenü.

        Args:
            file_book (dict): Ein Wörterbuch mit Buchnamen als Schlüssel und Metadaten als Wert.
        """
        self.file_book = file_book
        self.count_book = {}
        self.count_all_book = []
        self.pattern_word = ""
        self.select_wert()

    def select_wert(self):
        """Startet ein interaktives Menü zur Auswahl der Analyseart."""

        while True:
            not_found = "none"
            s_wert = input(Fore.LIGHTYELLOW_EX + Style.BRIGHT +
                           "Bitte wählen Sie eine der folgenden Optionen:\n"
                           "\t🔳 1 - Ein bestimmtes Buch analysieren\n"
                           "\t🔳 2 - Alle Bücher gemeinsam analysieren\n"
                           "\t🔳 3 - Jedes Buch einzeln analysieren\n"
                           "📍 Eingabe (oder 'e' zum Beenden): ")

            print("-" * 100)

            if s_wert.lower() in ("e", "beenden"):
                break
            elif s_wert in ("1", "2", "3"):
                while True:
                    self.pattern_word = input("Bitte geben Sie das gesuchte Wort ein: ").strip()
                    if not self.pattern_word:
                        print("❌ Das Suchwort darf nicht leer sein.")
                        print("-" * 100)
                        continue
                    print("-" * 100)
                    self.count_s_l_w()

                    if s_wert == "1":
                        select_name = input("Geben Sie den Namen des gewünschten Buches ein: ").strip()
                        for key, value in self.count_book.items():
                            if select_name in key:
                                print(f"\n📚 {key}:\n")
                                print(f"\t🟡 Leerzeichen: {value['Leerzeichen']}")
                                print(f"\t🟢 Wörter:     {value['Wörtern']}")
                                print(f"\t🔴 Zeilen:     {value['Zeilen']}")
                                if value.get(self.pattern_word, 0) > 0:
                                    print(f"\t🔵 Das Wort '{self.pattern_word}' wurde {value[self.pattern_word]} Mal gefunden.")
                                else:
                                    print(f"\t🔵 Das Wort '{self.pattern_word}' wurde im Text nicht gefunden.")
                                print("-" * 100)
                                not_found = "found"
                        if not_found == "none":
                            print("❌ Buch nicht gefunden. Bitte erneut versuchen.")
                        break

                    elif s_wert == "2":
                        print(f"\t🟡 Leerzeichen (alle Bücher): {self.count_all_book[0]}")
                        print(f"\t🟢 Wörter (alle Bücher):     {self.count_all_book[1]}")
                        print(f"\t🔴 Zeilen (alle Bücher):     {self.count_all_book[2]}")
                        if self.count_all_book[3] > 0:
                            print(f"\t🔵 Das Wort '{self.pattern_word}' wurde {self.count_all_book[3]} Mal gefunden.")
                        else:
                            print(f"\t🔵 Das Wort '{self.pattern_word}' wurde nicht gefunden.")
                        print("-" * 100)
                        break

                    elif s_wert == "3":
                        for key, value in self.count_book.items():
                            print(f"\n📚 {key}:\n")
                            print(f"\t🟡 Leerzeichen: {value['Leerzeichen']}")
                            print(f"\t🟢 Wörter:     {value['Wörtern']}")
                            print(f"\t🔴 Zeilen:     {value['Zeilen']}")
                            if value.get(self.pattern_word, 0) > 0:
                                print(f"\t🔵 Das Wort '{self.pattern_word}' wurde {value[self.pattern_word]} Mal gefunden.")
                            else:
                                print(f"\t🔵 Das Wort '{self.pattern_word}' wurde im Text nicht gefunden.")
                            print("-" * 100)
                        break
            else:
                print("❌ Ungültige Eingabe. Bitte nur 1, 2, 3 oder 'e' eingeben.")
                print("-" * 100)

    def count_s_l_w(self):
        """Zählt Leerzeichen, Wörter, Zeilen und das gesuchte Wort in allen Büchern."""

        all_pattern, all_word, all_space, all_line = 0, 0, 0, 0
        for key, value in self.file_book.items():
            path_book = load.BOOKS_PATH + "\\" + key
            with open(path_book, mode="r", encoding='utf-8') as book:
                all_book = book.read()
                word = all_book.split()
                c_spaces = all_book.count(" ")
                line = all_book.splitlines()
                lower_text = all_book.lower()
                count_pattern = lower_text.count(self.pattern_word.lower())

                self.count_book[key] = {
                    "Leerzeichen": c_spaces,
                    "Wörtern": len(word),
                    "Zeilen": len(line),
                    self.pattern_word: count_pattern
                }

                all_word += len(word)
                all_line += len(line)
                all_space += c_spaces
                all_pattern += count_pattern

        self.count_all_book = [all_space, all_word, all_line, all_pattern]
