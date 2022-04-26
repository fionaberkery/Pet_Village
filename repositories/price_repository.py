from db.run_sql import run_sql

from models.price import Price


def save(price):
    sql = "INSERT INTO prices (treatment_type, price, time_req, vet_req, nurses_req) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [price.treatment_type, price.price, price.time_req, price.vet_req, price.nurses_req]
    results = run_sql (sql, values)
    id = results[0]['id']
    price.id = id 


def select_all():
    prices = []

    sql = "SELECT * FROM prices"
    results = run_sql(sql)
    
    for result in results:
        price = Price(result['treatment_type'], result['price'], result['time_req'], result['vet_req'], result['nurses_req'], result['id'])
        prices.append(price)
    return prices

def select(id):
    sql = "SELECT * FROM prices WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    price = Price(result['treatment_type'], result['price'], result['time_req'], result['vet_req'], result['nurses_req'], result['id'])
    return price




def update(price):
    sql = "UPDATE prices SET (treatment_type, price, time_req, vet_req, nurses_req) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [price.treatment_type, price.price, price.time_req, price.vet_req, price.nurses_req, price.id]
    run_sql(sql, values)



def delete_all():
    sql = "DELETE FROM prices"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM prices WHERE id = %s"
    values = [id]
    run_sql(sql, values)