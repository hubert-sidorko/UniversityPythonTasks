class Koder:
    def __init__(self, dict_encode):
        self.dict_encode = dict_encode
        self.dict_decode = {pierwszy: drugi for drugi, pierwszy in dict_encode.items()}

    def zakoduj(self, tekst):
        zakodowany = []
        for litera in tekst:
            if litera in self.dict_encode:
                zakodowany.append(self.dict_encode[litera])
            else:
                raise KeyError(f"Nie można zakodować znaku: {litera}")
        return zakodowany

    def odkoduj(self, tekst):
        odkodowany = []
        for litera in tekst:
            if litera in self.dict_decode:
                odkodowany.append(self.dict_decode[litera])
            else:
                raise KeyError(f"Nie można odkodować znaku: {litera}")
        return odkodowany

    def statystyki(self, tekst):
        statystyki = {}
        for litera in tekst:
            statystyki[litera] = statystyki.get(litera, 0) + 1
        return statystyki
