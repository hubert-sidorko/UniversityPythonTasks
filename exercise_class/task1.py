class PhoneBook:
    def __init__(self, id):
        self.id = id
        self.data = {}

    def add_record(self, user, number):
        if number.isnumeric():
            self.data[user] = number
        else:
            print(f"Numer telefonu może mieć tylko cyfry. Błędna wartość: {number}.")

    def show_records(self):
        if self.data:
            for user, number in self.data.items():
                print(f'{user}: {number}')
        else:
            print("Brak danych w książce.")

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        assert type(other) == type(self)
        if self.data == other.data:
            return True
        return False

    def __gt__(self, other):
        assert type(other) == type(self)
        if len(self.data) > len(other.data):
            return True
        return False
