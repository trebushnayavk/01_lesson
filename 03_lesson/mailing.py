from adress import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        track_str = ", ".join([str(track) for track in self.track])
        return f"Стоимость письма отправленого из {self.to_address} в {self.from_address} с номером ({self.track}) составляет {self.cost}"




