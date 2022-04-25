from db.run_sql import run_sql

from models.treatment import Treatment
from models.pet import Pet
from models.vet import Vet

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

def save(treatment):
    sql = "INSERT INTO treatments (treatment_date, procedure_type, pet_id, vet_id) VALUES (%s, %s, %s, %s) RETURNING id "
    values = [treatment.treatment_date, treatment.procedure_type, treatment.pet.id, treatment.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    treatment.id = id

def select_all():
    treatments = []

    sql = "SELECT * FROM treatments"
    results = run_sql(sql)
    for result in results:
        pet = pet_repository.select(result ['pet_id']) 
        vet = vet_repository.select(result['vet_id'])
        treatment = Treatment(result['treatment_date'], result['procedure_type'], pet, vet, result['id'])
        treatments.append(treatment)
    return treatments 

def select(id):
    sql = "SELECT * FROM treatments WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    pet = pet_repository.select(result ['pet_id']) 
    vet = vet_repository.select(result['vet_id'])
    treatment = Treatment(result['treatment_date'], result['procedure_type'], pet, vet, result['id'])
    return treatment

def update(treatment):
    sql = "UPDATE treatments SET (treatment_date, procedure_type, pet_id, vet_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [treatment.treatment_date, treatment.procedure_type, treatment.pet.id, treatment.vet.id, treatment.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM treamtents"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM treatments WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def find_by_vet(vet):
    treatments = []
    sql = "SELECT * FROM treatments WHERE vet_id=%s "
    values = [vet.id]
    results = run_sql(sql, values)
    for result in results:
        pet = pet_repository.select(result ['pet_id']) 
        treatment = Treatment(result['treatment_date'], result['procedure_type'], pet, vet, result['id'])
        treatments.append(treatment)
    return treatments 


def find_by_pet(pet):
    treatments = []
    sql = "SELECT * FROM treatments WHERE pet_id=%s "
    values = [pet.id]
    results = run_sql(sql, values)
    for result in results:
        vet = vet_repository.select(result ['vet_id']) 
        treatment = Treatment(result['treatment_date'], result['procedure_type'], pet, vet, result['id'])
        treatments.append(treatment)
    return treatments 