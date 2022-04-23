from models.owner import Owner
import repositories.owner_repository as owner_repository

from models.pet import Pet
import repositories.pet_repository as pet_repository

from models.treatment import Treatment
import repositories.treatment_repository as treatment_repository

from models.vet import Vet
import repositories.vet_repository as vet_repository

# treatment_repository.delete_all()
# pet_repository.delete_all()
# owner_repository.delete_all()
# vet_repository.delete_all()


vet_1 = Vet("Dr DoAlot")
vet_repository.save(vet_1)
vet_2 = Vet("Dr Pawsitive")
vet_repository.save(vet_2)
vet_3 = Vet("Dr Meowgaret")
vet_repository.save(vet_3)
vet_4 = Vet("Dr Trotter")
vet_repository.save(vet_4)
vet_5 = Vet("Dr Bunderful")
vet_repository.save(vet_5)
vet_6 = Vet("Dr Dory")
vet_repository.save(vet_6)

# vet_repository.save(vet_6)
# vet_repository.select_all()
# vet_repository.select(1)
# vet_repository.delete_all()
# vet_repository.delete(10)

owner_1 = Owner("Scarlet", "Skittles", "tastetherainbow@mail.com", "07711111111")
owner_repository.save(owner_1)
owner_2 = Owner("Janet", "Jelly", "wobbly@mail.com", "07711221122")
owner_repository.save(owner_2)
owner_3 = Owner("Kelly", "Kinder", "eggs@mail.com", "07711331133")
owner_repository.save(owner_3)
owner_4 = Owner("Mandy", "Marshmallow", "squidgy@mail.com", "07711441144")
owner_repository.save(owner_4)
owner_5 = Owner("Andy", "Allsorts", "sweeties@mail.com", "07711551155")
owner_repository.save(owner_5)
owner_6 = Owner("Buzz", "BonBon", "strawberry@mail.com", "07711661166")
owner_repository.save(owner_6)
owner_7 = Owner("Mike", "Mars", "yum@mail.com", "07711771177")
owner_repository.save(owner_7)
owner_8 = Owner("Carl", "Cookie", "chocchips@mail.com", "07711881188")
owner_repository.save(owner_8)

# owner_repository.select_all()
# owner_repository.select(16)
# owner_repository.delete_all()
# owner_repository.delete(20)

pet_1 = Pet("Snuffles", "1st May 2021", "Hamster", owner_1, vet_1)
pet_repository.save(pet_1)
pet_2 = Pet("Fergus", "14th Dec 2022", "Rabbit", owner_2, vet_2)
pet_repository.save(pet_2)
pet_3 = Pet("Poppins", "21st June 2015", "Cat", owner_3, vet_4)
pet_repository.save(pet_3)
pet_4 = Pet("Harry", "19th Oct 2013", "Dog", owner_4, vet_5)
pet_repository.save(pet_4)
pet_5 = Pet("Archie", "16th Feb 2011", "Dog", owner_5, vet_6)
pet_repository.save(pet_5)
pet_6 = Pet("Jake", "9th Aug 2014", "Guinea Pig", owner_6, vet_5)
pet_repository.save(pet_6)
pet_7 = Pet("Sally", "31st Jan 2016", "Snake", owner_7, vet_3)
pet_repository.save(pet_7)
pet_8 = Pet("Roxy", "7th July 2018", "Bearded Dragon", owner_8, vet_1)
pet_repository.save(pet_8)
pet_9 = Pet("Rupert", "15th May 2020", "Rat", owner_3, vet_4)
pet_repository.save(pet_9)
pet_10 = Pet("Coco", "15th March 2020", "Dog", owner_7, vet_3)
pet_repository.save(pet_10)

# pet_repository.select_all()
# pet_repository.select(7)
# pet_repository.delete(19)

treatment_1 = Treatment("26th May 2021", "MRI Scan", pet_2, vet_1)
treatment_repository.save(treatment_1)
treatment_2 = Treatment("3rd Aug 2021", "CT Scan", pet_3, vet_6)
treatment_repository.save(treatment_2)
treatment_3 = Treatment("19th Jan 2021", "US Scan", pet_4, vet_2)
treatment_repository.save(treatment_3)
treatment_4 = Treatment("17th Nov 2021", "MRI Scan", pet_7, vet_3)
treatment_repository.save(treatment_4)
treatment_5 = Treatment("14th Feb 2022", "CT Scan", pet_8, vet_5)
treatment_repository.save(treatment_5)



# treatment_repository.select_all()
# treatment_repository.select(10)
# treatment_repository.delete(10)