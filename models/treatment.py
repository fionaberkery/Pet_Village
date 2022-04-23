class Treatment:
    def __init__(self, treatment_date, procedure_type, pet, vet, id=None):
        self.treatment_date = treatment_date
        self.procedure_type = procedure_type
        self.pet = pet
        self.vet = vet
        self.id = id