from flask import Blueprint, Flask, redirect, render_template, request

from models.vet import Vet

import repositories.pet_repository as pet_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository

vets_blueprint = Blueprint("vets",__name__)

#INDEX
@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", vets=vets)

@vets_blueprint.route("/vets/<id>")
def vet(id):
    vet = vet_repository.select(id)
    pets = pet_repository.select_all()
    return render_template("vets/profile.html", vet=vet, pets=pets)


@vets_blueprint.route("/vets")
def find_all_pets():
    pets = []
    vet_repository.find_pets()
    return render_template("/vets/pets", )
#NEW


#CREATE


#EDIT


#UPDATE


#DELETE
