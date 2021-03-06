from db.run_sql import run_sql

from models.vet import Vet
from models.pet import Pet
from models.treatment import Treatment

import repositories.pet_repository as pet_repository
import repositories.treatment_repository as treatment_repository

def save(vet):
    sql = "INSERT INTO vets (vet_name, speciality, email) VALUES (%s, %s, %s) RETURNING id"
    values = [vet.vet_name, vet.speciality, vet.email]
    results = run_sql (sql, values)
    id = results[0]['id']
    vet.id = id 


def select_all():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    
    for result in results:
        vet = Vet(result['vet_name'], result['speciality'], result['email'], result['id'])
        vets.append(vet)
    return vets 

def select(id):
    sql = "SELECT * FROM vets WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    vet = Vet(result['vet_name'], result['speciality'], result['email'], result['id'])
    return vet 


def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(vet):
    sql = "UPDATE vets SET (vet_name, speciality, email) = (%s, %s, %s) WHERE id = %s"
    values = [vet.vet_name, vet.speciality, vet.email, vet.id]
    run_sql(sql, values)


# find all pets belonging to a vet

