from mailbox import FormatError

from M21.Inhaber import Inhaber
from M21.Konto import Konto


class Kontoverwaltung:

    def __init__(self):
        print('[Buch]:constructor')
        self.__konto_nummer_counter:int = 0
        self.__inhaber_nummer_counter:int = 0
        self.__konten_liste:list[Konto] = []
        self.__inhaber_liste:list[Inhaber] = []

        self.__ERSTELLE_KONTO:int = 1
        self.__ERSTELLE_INHABER:int = 2
        self.__GELD_ABHEBEN:int = 3
        self.__GELD_EINZAHLEN:int = 4
        self.__BEENDEN:int = 5
        self.main_loop()

    def get_konto_by_id(self, id:int, inhaber:Inhaber) -> Konto|None:
        for konto in self.__konten_liste:
            if konto.get_id() == id:
                if konto.get_inhaber().get_id() == inhaber.get_id():
                    return konto

    def get_konto_by_inhaber(self, inhaber:Inhaber) -> Konto|None:
        for konto in self.__konten_liste:
            if konto.get_inhaber() == inhaber:
                return konto

    def get_inhaber_by_id(self, id:int) -> Inhaber | None:
        for inhaber in self.__inhaber_liste:
            if inhaber.id == id:
                return inhaber

    def erstelle_inhaber(self, inhaber_name:str) -> Inhaber:
        self.__inhaber_nummer_counter+=1
        inhaber:Inhaber = Inhaber(
            inhaber_name,
            self.__inhaber_nummer_counter
        )
        self.__inhaber_liste.append(
            inhaber
        )
        return inhaber

    def erstelle_konto(self, kontoinhaber:Inhaber) -> Konto:
        self.__konto_nummer_counter+=1
        konto:Konto = Konto(
            kontoinhaber,
            self.__konto_nummer_counter,
            0
        )
        self.__konten_liste.append(
            konto
        )
        return konto

    def get_inhaber_from_input(self) -> Inhaber|None:
        input_string:str = input('gebe die id eines Inhabers ein:')
        try:
            inhaber_id: int = int(input_string)
            inhaber: Inhaber = self.get_inhaber_by_id(inhaber_id)
            if inhaber is None:
                print(f'es existiert kein kontoinhaber mit der id {inhaber_id}')
            return inhaber
        except FormatError:
            print(f'\'{input_string}\' ist keine gültige id')

    def get_konto_from_input(self, inhaber:Inhaber) -> Konto|None:
        input_string:str = input('gebe die id des Kontos ein:')
        try:
            konto_id: int = int(input_string)
            konto:Konto|None = self.get_konto_by_id(konto_id, inhaber)
            if konto is None:
                print(f'es existiert kein konto mit der id {input_string}')
            return konto
        except FormatError:
            print(f'\'{input_string}\' ist keine gültige id')


    def main_loop(self):
        while True:
            print('gebe eine Zahl ein')
            input_string:str = input('1: Konto erstellen\n2: Inhaber erstellen\n3: Geld einzahlen\n4: Geld abheben\n5: Beenden\n')
            input_action_number:int = 0

            try:
                input_action_number = int(input_string)
            except FormatError:
                print(f'\'{input_string}\' ist keine gültige Aktion')

            if input_action_number == self.__ERSTELLE_KONTO:
                try:
                    inhaber:Inhaber = self.get_inhaber_from_input()
                    if inhaber is None:
                        continue
                    konto:Konto = self.erstelle_konto(inhaber)
                    print(f'deine neue kontonummer ist {konto.get_id()}')
                except FormatError:
                    print(f'\'{input_string}\' ist keine gültige id')
                continue

            if input_action_number == self.__ERSTELLE_INHABER:
                inhaber_name:str = input('gebe deinen Namen ein:')
                inhaber:Inhaber = self.erstelle_inhaber(inhaber_name)
                print(f'deine neue Inhaber id ist {inhaber.get_id()}')
                continue

            if input_action_number == self.__GELD_ABHEBEN:
                try:
                    inhaber:Inhaber = self.get_inhaber_from_input()
                    if inhaber is None:
                        continue
                    konto:Konto = self.get_konto_from_input(inhaber)
                    if konto is None:
                        continue
                    betrag = float(input('gebe den auszuzahlenden Betrag ein\n'))
                    konto.auszahlen(betrag)
                    print(f'der kontostand ist jetzt {konto.get_kontostand()}')
                except FormatError:
                    print(f'\'{input_string}\' ist keine gültige id')
                continue

            if input_action_number == self.__GELD_EINZAHLEN:
                try:
                    inhaber:Inhaber = self.get_inhaber_from_input()
                    if inhaber is None:
                        continue
                    konto:Konto = self.get_konto_from_input(inhaber)
                    if konto is None:
                        continue
                    betrag = float('gebe den einzuzahlenden Betrag ein')
                    konto.einzahlen(betrag)
                    print(f'der kontostand ist jetzt {konto.get_kontostand()}')
                except FormatError:
                    print(f'\'{input_string}\' ist keine gültige id')
                continue
            if input_action_number == self.__BEENDEN:
                break