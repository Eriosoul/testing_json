import json


class Person:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.prename = ""
        self.age = ""
        self.city = ""
        self.country = ""

    def collect_data(self):
        self.name = input("Introduce el nombre: ").title()
        self.prename = input("Introduce el apellido: ").title()
        self.age = input("Introduce tu edad: ")

    def collect_location(self):
        self.city = input("Introduce la ciudad: ").title()
        self.country = input("Introduce el país: ").upper()

    def show_data_collected(self):
        user_data = [self.name, self.prename, self.age, self.city, self.country]
        print(f"Nombre: {self.name}, Apellido: {self.prename}")
        print(f"Edad: {self.age}")
        print(f"Ciudad: {self.city}")
        print(f"País: {self.country}")
        print(user_data)

    def check_json_data(self):
        try:
            with open("personal.json", 'r') as file:
                data = json.load(file)
                if data:  # Verifica si el archivo no está vacío
                    return True
                else:
                    return False
        except FileNotFoundError:
            return False


if __name__ == '__main__':
    p: Person() = Person()
    p.collect_data()
    p.collect_location()
    p.show_data_collected()
