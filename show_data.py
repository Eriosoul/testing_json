import json


class ShowData:
    def __init__(self):
        self.data_json = "personal.json"

    def show(self):
        with open(self.data_json, 'r') as file:
            data = json.load(file)
            personal = data["Information"][1]
        return personal


def show_main():
    data_shower = ShowData()
    personal_data = data_shower.show()
    print(personal_data)
