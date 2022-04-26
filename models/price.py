class Price:
    def __init__(self, treatment_type, price, time_req, vet_req, nurses_req, id=None):
        self.treatment_type = treatment_type
        self.price = price
        self.time_req = time_req
        self.vet_req = vet_req
        self.nurses_req = nurses_req
        self.id = id