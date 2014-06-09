class Base:
    lst = {}
    def __str__(self):
        return self.__class__.__name__
    def get_score(self, scores):
        sum = 0.0;
        for key in self.lst:
            sum += self.lst[key] * scores[key]


class Algorytmik(Base):
    lst = {
        'ASD' : 0.5
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


archetypes=[Algorytmik(),]

