from colect_data import Person
from generate_data_json import GenerateDataJson
from show_data import show_main

if __name__ == '__main__':
    p: Person() = Person()
    p.collect_data()
    p.collect_location()
    p.show_data_collected()

    data_json = GenerateDataJson()
    data_json.add_data(p.name, p.prename, p.age, p.city, p.country)
    data_json.save_to_json()
    show_main()
