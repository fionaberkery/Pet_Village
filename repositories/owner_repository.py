from db.run_sql import run_sql

from models.owner import Owner
from models.pet import Pet

import repositories.pet_repository as pet_repository

def save(owner):
    sql = "INSERT INTO owners (first_name, last_name, email, mobile) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [owner.first_name, owner.last_name, owner.email, owner.mobile]
    results = run_sql (sql, values)
    id = results[0]['id']
    owner.id = id 


def select_all():
    owners = []

    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    
    for result in results:
        owner = Owner(result['first_name'], result['last_name'], result['email'], result['mobile'], result['id'])
        owners.append(owner)
    return owners

def select(id):
    sql = "SELECT * FROM owners WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    owner = Owner(result["first_name"], result["last_name"], result["email"], result["mobile"], result["id"])
    return owner


def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(owner):
    sql = "UPDATE owners SET (first_name, last_name, email, mobile) = (%s, %s, %s, %s) WHERE id = %s"
    values = [owner.first_name, owner.last_name, owner.email, owner.mobile, owner.id]
    run_sql(sql, values)