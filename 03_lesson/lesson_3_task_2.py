from smartphone import Smartphone

catalog = [
    Smartphone("Huawei", "P60 Pro", "+79445666677"),
    Smartphone("Xiaomi", "13T Pro", "+79223331155"),
    Smartphone("Samsung", "Galaxy S23", "+79112553344"),
    Smartphone("Apple", "iPhone 17", "+79009912233"),
    Smartphone("Vivo", "V2109", "+79113458700")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
