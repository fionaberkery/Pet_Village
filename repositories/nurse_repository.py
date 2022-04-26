from db.run_sql import run_sql

from models.nurse import Nurse


def save(nurse):
    sql = "INSERT INTO nurses (nurse_name, days_works, available_weekends, email) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [nurse.nurse_name, nurse.days_works, nurse.available_weekends, nurse.email]
    results = run_sql (sql, values)
    id = results[0]['id']
    nurse.id = id 


def select_all():
    nurses = []

    sql = "SELECT * FROM nurses"
    results = run_sql(sql)
    
    for result in results:
        nurse = Nurse(result['nurse_name'], result['days_works'], result['available_weekends'], result['email'], result['id'])
        nurses.append(nurse)
    return nurses

# def select(id):
#     sql = "SELECT * FROM owners WHERE id=%s"
#     values = [id]
#     result = run_sql(sql, values)[0]
#     owner = Owner(result["first_name"], result["last_name"], result["email"], result["mobile"], result["id"])
#     return owner


# def delete_all():
#     sql = "DELETE FROM owners"
#     run_sql(sql)


# def delete(id):
#     sql = "DELETE FROM owners WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)


# def update(owner):
#     sql = "UPDATE owners SET (first_name, last_name, email, mobile) = (%s, %s, %s, %s) WHERE id = %s"
#     values = [owner.first_name, owner.last_name, owner.email, owner.mobile, owner.id]
#     run_sql(sql, values)