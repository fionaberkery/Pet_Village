from db.run_sql import run_sql

from models.pet import Pet
from models.owner import Owner
from models.vet import Vet
from models.treatment import Treatment

import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository

def save(pet):
    sql = "INSERT INTO pets (pet_name, dob, pet_type, owner_id, vet_id) VALUES (%s, %s, %s, %s, %s) RETURNING id "
    values = [pet.pet_name, pet.dob, pet.pet_type, pet.owner.id, pet.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id

def select_all():
    pets = []
    sql = "SELECT * FROM pets"
    results = run_sql(sql)
    for result in results:
        owner = owner_repository.select(result ['owner_id']) 
        vet = vet_repository.select(result['vet_id'])
        pet = Pet(result['pet_name'], result['dob'], result['pet_type'], owner, vet, result['id'])
        pets.append(pet)
    return pets 

def select(id):
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    owner = owner_repository.select(result ['owner_id']) 
    vet = vet_repository.select(result['vet_id'])
    pet = Pet(result['pet_name'], result['dob'], result['pet_type'], owner, vet, result['id'])
    return pet

def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(pet):
    sql = "UPDATE pets SET (pet_name, dob, pet_type, owner_id, vet_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [pet.pet_name, pet.dob, pet.pet_type, pet.owner.id, pet.vet.id, pet.id]
    run_sql(sql, values)



def find_by_vet(vet):
    pets = []
    sql = "SELECT * FROM pets WHERE vet_id=%s "
    values = [vet.id]
    results = run_sql(sql, values)
    for result in results:
        owner = owner_repository.select(result ['owner_id']) 
        pet = Pet(result['pet_name'], result['dob'], result['pet_type'], owner, vet, result['id'])
        pets.append(pet)
    return pets 