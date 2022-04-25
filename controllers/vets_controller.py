from flask import Blueprint, Flask, redirect, render_template, request

from models.vet import Vet

import repositories.pet_repository as pet_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository

vets_blueprint = Blueprint("vets",__name__)

# home page for vets
@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", vets=vets)

# # profile page for one vet
@vets_blueprint.route("/vets/<id>")
def vet(id):
    vet = vet_repository.select(id)
    pets = pet_repository.select_all()
    return render_template("vets/profile.html", vet=vet, pets=pets)



# get a list of all pets belonging to one vet 
@vets_blueprint.route("/vets/<id>/pets")
def get_pets(id):
    vet = vet_repository.select(id)
    pets = pet_repository.find_by_vet(vet)
    return render_template("/vets/pets.html", pets=pets, vet=vet)

# get a list of all treatment notes to one vet
@vets_blueprint.route("/vets/<id>/treatments")
def get_treatments(id):
    vet = vet_repository.select(id)
    treatments = treatment_repository.find_by_vet(vet)
    return render_template("/vets/treatments.html", treatments=treatments, vet=vet)

