class AdresEmail:
    def __init__(self, user):
        self.user = user
        self.emails = []
        self.datebase = {}

    def prawidlowy(self, adres):
        if ' ' in adres or '\t' in adres or '\n' in adres:
            return False
        if adres.count('@') != 1:
            return False
        elif adres.startswith('@') or adres.endswith('@'):
            return False
        elif '.' not in adres.split('@')[-1]:
            return False
        elif adres.endswith('.'):
            return False
        return True

    def addAddress(self, adres):
        if not self.prawidlowy(adres):
            raise ValueError('Nieprawidlowy email, nie spelnia warunkow')
        if adres not in self.emails:
            self.emails.append(adres)
            self.datebase[self.user] = adres
            return True
        else:
            return False

    def removeAddress(self, adres):
        if adres in self.emails:
            self.emails.remove(adres)
            return True
        else:
            return False

    def sortAddresses(self):
        self.emails.sort()
        return True
