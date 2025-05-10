from smartphone import Smartphone
catalog = [
    Smartphone("Nissan", "Crew", "89004567898"),
    Smartphone("Nissan", "Fairlady Z", "89213456789"),
    Smartphone("Nissan", "Figaro", "89523645612"),
    Smartphone("Nissan", "Almera", "89525678904"),
    Smartphone("Nissan", "Altima", "89523452345")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")