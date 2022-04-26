from flask import Blueprint, Flask, redirect, render_template, request
from controllers.vets_controller import vet

from models.booking import Booking

import repositories.pet_repository as pet_repository
import repositories.booking_repository as booking_repository
import repositories.price_repository as price_repository
import repositories.vet_repository as vet_repository

bookings_blueprint = Blueprint("booking",__name__)

# INDEX
@bookings_blueprint.route('/bookings')
def bookings():
    bookings = booking_repository.select_all()
    return render_template('bookings/index.html', bookings=bookings)

# SHOW
@bookings_blueprint.route('/bookings/<id>')
def select_booking(id):
    booking = booking_repository.select(id)
    return render_template('/bookings/show.html', booking=booking)

# NEW 
@bookings_blueprint.route('/bookings/new')
def new_booking():
    pets = pet_repository.select_all()
    prices = price_repository.select_all()
    vets = vet_repository.select_all()
    return render_template('/bookings/new.html', vets=vets, pets=pets, prices=prices)

# CREATE
@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    date = request.form["date"]
    time = request.form["time"]

    price_id = request.form["price_id"]
    pet_id = request.form["pet_id"]
    vet_id = request.form["vet_id"]
    
    price = price_repository.select(price_id)
    pet = pet_repository.select(pet_id)
    vet = vet_repository.select(vet_id)

    new_booking = Booking(date, time, pet, price, vet)
    booking_repository.save(new_booking)
    return redirect("/bookings")

# EDIT
@bookings_blueprint.route("/bookings/<id>/edit")
def edit_booking(id):
    booking = booking_repository.select(id)
    pets = pet_repository.select_all()
    prices = price_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("/bookings/edit.html", vets=vets, pets=pets, prices=prices, booking=booking)

# UPDATE
@bookings_blueprint.route("/bookings/<id>", methods=["POST"])
def update_booking(id):
    date = request.form["date"]
    time = request.form["time"]

    price_id = request.form["price_id"]
    pet_id = request.form["pet_id"]
    vet_id = request.form["vet_id"]
    
    price = price_repository.select(price_id)
    pet = pet_repository.select(pet_id)
    vet = vet_repository.select(vet_id)

    new_booking = Booking(date, time, pet, price, vet, id)
    booking_repository.update(new_booking)
    return redirect("/bookings")



# DELETE
@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")


# # get list of all treatment notes of one pet
# @pets_blueprint.route("/pets/<id>/treatments")
# def get_treatments(id):
#     pet = pet_repository.select(id)
#     treatments = treatment_repository.find_by_pet(pet)
#     return render_template("/pets/treatments.html", treatments=treatments, pet=pet)
