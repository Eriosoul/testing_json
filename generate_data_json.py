import json


class GenerateDataJson:
    def __init__(self):
        try:
            with open("personal.json", 'r') as file:
                existing_data = json.load(file)
                self.data = existing_data
        except FileNotFoundError:
            self.data = []

    def add_data(self, name, prename, age, city, country):
        if len(self.data) == 0:
            _id = 1
        else:
            _id = self.data[-1]["personal_data"]["_Id"] + 1

        data = {
            "personal_data": {
                "_Id": _id,
                "Name": name,
                "PreName": prename,
                "Ages": age,
            },
            "location_data": {
                "city": city,
                "country": country
            }
        }
        self.data.append(data)

    def save_to_json(self):
        with open("personal.json", 'w') as file:
            json.dump(self.data, file, indent=2)

    # def __init__(self):
    #     self.data = [
    #         {
    #             "personal_data": {
    #                 "_Id": "",
    #                 "Name": "",
    #                 "PreName": "",
    #                 "Ages": "",
    #             },
    #             "location_data": {
    #                 "city": "",
    #                 "country": ""
    #             }
    #         }
    #     ]
    #
    # def set_personal_data(self, _id, name, prename, age):
    #     self.data[0]["personal_data"]["_Id"] = _id
    #     self.data[0]["personal_data"]["Name"] = name
    #     self.data[0]["personal_data"]["PreName"] = prename
    #     self.data[0]["personal_data"]["Ages"] = age
    #
    # def set_location_data(self, city, country):
    #     self.data[0]["location_data"]["city"] = city
    #     self.data[0]["location_data"]["country"] = country
    #
    # def save_to_json(self):
    #     with open("personal.json", 'a') as file:
    #         self.data[0]["personal_data"]["_Id"] += 1
    #         json.dump(self.data, file)
