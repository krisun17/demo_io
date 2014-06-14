class Base:
    lst = {}

    def __str__(self):
        return self.__class__.__name__

    def get_score(self, scores):
        sum = 0.0
        for key in self.lst:
            sum += self.lst[key] * scores[key]
        return sum
    def get_context_data(self):
        return {}


class Algorytmik(Base):
    lst = {
        'ASD': 0.5, 'MD': 0.1, 'GAL': 0.1, 'RPiS': 0.1, 'JAO': 0.1, 'PMAT': 0.05, 'AM1': 0.025, 'AM2': 0.025,
    }

    def get_context_data(self):
        x = {}
        x['name'] = 'Algorytmik'
        x['primary'] = [
            'algorytmika',
            'algorytmy tekstowe',
            'kompresja danych',
        ]
        x['secondary'] = [
            'teoria informacji',
            'sztuczna inteligencja',
        ]
        return x

class Koder(Base):
    lst = {
        'IPP' : 0.15, 'JNP1' : 0.15, 'JNP2' : 0.125, 'WPI' : 0.1, 'ASD' : 0.1, 'WWW' : 0.1, 'IO' : 0.075, 'PO' : 0.05, 'SIK' : 0.05, 'SO' : 0.05, 'BD' : 0.05,
    }
    def get_context_data(self):
        x = {}
        x['name'] = 'Koder'
        x['primary'] = [
            'ZSO',
            'prolog',
            'weryfikacja wpomagana kompueterowo',
        ]
        x['secondary'] = [
            'wnioskowanie',
            'sztuczna inteligencja',
            'algorytmy tekstowe',
            'algorytmika',
        ]
        return x

class AnalitykDanych(Base):
    lst= {
        'BD':0.4,'RPiS' : 0.35, 'MD' : 0.1, 'ASD' : 0.05, 'PO' : 0.02, 'AM1' : 0.02, 'AM2' : 0.02, 'GAL' : 0.02, 'PMAT' : 0.02,
    }


    def get_context_data(self):
        x = {}
        x['name'] = 'Analityk danych'
        x['primary'] = [
            'ZBD',
            'systemy uczące się',
        ]
        x['secondary'] = [
            'teoria informacji',
            'kompresja danych',
        ]
        return x

class ProgramistaNiskopoziomowy(Base):
    lst= {
        'SO':0.5, 'SIK' : 0.30, 'AKS' : 0.10, 'JNP1' : 0.05, 'JNP2' : 0.01, 'WPI' : 0.01, 'WWW' : 0.01, 'PO' : 0.01, 'IO' : 0.01,
    }

    def get_context_data(self):
        x = {}
        x['name'] = 'Programista niskopoziomowy'
        x['primary'] = [
            'ZSO',
        ]
        x['secondary'] = [
            'Programowanie mikrokontrolerów',
        ]
        return x

archetypes = [Algorytmik(), Koder(), AnalitykDanych(), ProgramistaNiskopoziomowy(),]

