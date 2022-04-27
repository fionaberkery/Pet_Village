from flask import Blueprint, Flask, redirect, render_template, request
from controllers.vets_controller import vet

from models.pet import Pet

import repositories.pet_repository as pet_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository
import repositories.booking_repository as booking_repository

pets_blueprint = Blueprint("pets",__name__)


#LOG IN PAGE
@pets_blueprint.route('/home')
def login():
    return render_template('index.html')

# HOME PAGE
@pets_blueprint.route('/pets')
def pets():
    pets = pet_repository.select_all()
    return render_template('pets/index.html', pets=pets)



# SHOW
@pets_blueprint.route('/pets/<id>')
def select_pet(id):
    pet = pet_repository.select(id)
    return render_template('/pets/profile.html', pet=pet)

# NEW 
@pets_blueprint.route('/pets/new')
def new_pet():
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    return render_template('/pets/new.html', owners=owners, vets=vets)

# CREATE
@pets_blueprint.route("/pets", methods=["POST"])
def create_pet():
    pet_name = request.form["pet_name"]
    dob = request.form["dob"]
    pet_type = request.form["pet_type"]
    owner_id = request.form["owner_id"]
    vet_id = request.form["vet_id"]
    owner = owner_repository.select(owner_id)
    vet = vet_repository.select(vet_id)
    new_pet = Pet(pet_name, dob, pet_type, owner, vet)
    pet_repository.save(new_pet)
    return redirect("/pets")

# EDIT
@pets_blueprint.route("/pets/<id>/edit")
def edit_pet(id):
    pet = pet_repository.select(id)
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("/pets/edit.html", pet=pet, owners=owners, vets=vets)

# UPDATE
@pets_blueprint.route("/pets/<id>", methods=["POST"])
def update_pet(id):
    pet_name = request.form["pet_name"]
    dob = request.form["dob"]
    pet_type = request.form["pet_type"]
    owner_id = request.form["owner_id"]
    vet_id = request.form["vet_id"]
    owner = owner_repository.select(owner_id)
    vet = vet_repository.select(vet_id)
    new_pet = Pet(pet_name, dob, pet_type, owner, vet, id)
    pet_repository.update(new_pet)
    return redirect("/pets")



# DELETE
@pets_blueprint.route("/pets/<id>/delete", methods=["POST"])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect("/pets")


# get list of all treatment notes of one pet
@pets_blueprint.route("/pets/<id>/treatments")
def get_treatments(id):
    pet = pet_repository.select(id)
    treatments = treatment_repository.find_by_pet(pet)
    return render_template("/pets/treatments.html", treatments=treatments, pet=pet)

# get list of all bookings of one pet 
@pets_blueprint.route("/pets/<id>/bookings")
def get_bookings(id):
    pet = pet_repository.select(id)
    bookings = booking_repository.find_by_pet(pet)
    return render_template("/pets/bookings.html", bookings=bookings, pet=pet)
