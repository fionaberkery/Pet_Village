from db.run_sql import run_sql

from models.pet import Pet
from models.booking import Booking
from models.price import Price

import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.price_repository as price_repository
import repositories.pet_repository as pet_repository

def save(booking):
    sql = "INSERT INTO bookings (date, time, pet_id, price_id, vet_id) VALUES (%s, %s, %s, %s, %s) RETURNING id "
    values = [booking.date, booking.time, booking.pet.id, booking.price.id, booking.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id

def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results:
        pet = pet_repository.select(result ['pet_id']) 
        treatment = price_repository.select(result['price_id'])
        vet = vet_repository.select(result['vet_id'])
        booking = Booking(result['date'], result['time'], pet, treatment, vet, result['id'])
        bookings.append(booking)
    return bookings 

def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    pet = pet_repository.select(result ['pet_id']) 
    treatment = price_repository.select(result['price_id'])
    vet = vet_repository.select(result['vet_id'])
    booking = Booking(result['date'], result['time'], pet, treatment, vet, result['id'])
    return booking

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(booking):
    sql = "UPDATE bookings SET (date, time, pet_id, price_id, vet_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [booking.date, booking.time, booking.pet.id, booking.price.id, booking.vet.id, booking.id]
    run_sql(sql, values)





def find_by_pet(pet):
    bookings = []
    sql = "SELECT * FROM bookings WHERE pet_id=%s "
    values = [pet.id]
    results = run_sql(sql, values)
    for result in results:
        price = price_repository.select(result ['price_id']) 
        vet = vet_repository.select(result ['vet_id'])
        booking = Booking(result['date'], result['time'], pet, price, vet, result['id'])
        bookings.append(booking)
    return bookings 



def find_by_vet(vet):
    bookings = []
    sql = "SELECT * FROM bookings WHERE vet_id=%s "
    values = [vet.id]
    results = run_sql(sql, values)
    
    for result in results:
        price = price_repository.select(result ['price_id']) 
        pet = pet_repository.select(result ['pet_id'])
        
        booking = Booking(result['date'], result['time'], pet, price, vet, result['id'])
        bookings.append(booking)
    return bookings 




    