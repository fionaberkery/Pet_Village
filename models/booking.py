class Booking:
    def __init__(self, date, time, pet, price, vet, id=None):
        self.date = date
        self.time = time
        self.pet = pet
        self.price = price
        self.vet = vet
        self.id = id