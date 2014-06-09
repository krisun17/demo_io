class Base:
    lst = {}

    def __str__(self):
        return self.__class__.__name__

    def get_score(self, scores):
        sum = 0.0
        for key in self.lst:
            sum += self.lst[key] * scores[key]
        return sum


class Algorytmik(Base):
    lst = {
        'ASD': 0.5, 'MD': 0.1, 'GAL': 0.1, 'RPiS': 0.1, 'JAO': 0.1, 'PMAT': 0.05, 'AM1': 0.025, 'AM2': 0.025,
    }

    def desc(self):
        return """
        Algorytmik:
*podstawowe:
- algorytmika
- algorytmy tekstowe
- kompresja danych
*poboczne:
- sztuczna inteligencja
- teoria informacji"""

class Koder(Base):
    lst = {
        'IPP' : 0.15, 'JNP1' : 0.15, 'JNP2' : 0.125, 'WPI' : 0.1, 'ASD' : 0.1, 'WWW' : 0.1, 'IO' : 0.075, 'PO' : 0.05, 'SIK' : 0.05, 'SO' : 0.05, 'BD' : 0.05,
    }
    def desc(self):
        return """
            Koder:
            *podstawowe:
- ZSO (SO >= 4)
- prolog (PMAT >= 3.5)
- weryfikacja wpomagana kompueterowo
*poboczne:
- wnioskowanie
- sztuczna inteligencja
- algorytmy tekstowe
- algorytmika
"""

class AnalitykDanych(Base):
    lst= {
        'BD':0.4,'RPiS' : 0.35, 'MD' : 0.1, 'ASD' : 0.05, 'PO' : 0.02, 'AM1' : 0.02, 'AM2' : 0.02, 'GAL' : 0.02, 'PMAT' : 0.02,
    }
    def desc(self):
        return """
        Analityk danych:

*podstawowe:
-ZBD
-systemy uczace sie

-opcjonalne:
-teoria informacji (MD>=4)
-kompresja danych
"""

class ProgramistaNiskopoziomowy(Base):
    lst= {
        'SO':0.5, 'SIK' : 0.30, 'AKS' : 0.10, 'JNP1' : 0.05, 'JNP2' : 0.01, 'WPI' : 0.01, 'WWW' : 0.01, 'PO' : 0.01, 'IO' : 0.01,
    }
    def desc(self):
        return """
        Programista niskopoziomowy:

podstawowe
-ZSO

-opcjonalne
?? (cos w stylu programowania mikrokontorlerów ale to nie jest obieralny stały)"""

archetypes = [Algorytmik(), Koder(), AnalitykDanych(), ProgramistaNiskopoziomowy(),]

