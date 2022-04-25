from flask import Blueprint, Flask, redirect, render_template, request

from models.treatment import Treatment

import repositories.pet_repository as pet_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository

treatments_blueprint = Blueprint("treatments",__name__)



#INDEX
@treatments_blueprint.route("/treatments")
def treatment_notes_all():
    treatments = treatment_repository.select_all()
    vets = vet_repository.select_all()
    pets = pet_repository.select_all()
    return render_template("/treatments/index.html", treatments=treatments, vets=vets, pets=pets)

# SHOW ONE TREATMENT
@treatments_blueprint.route("/treatments/<id>")
def select_one_treatment(id):
    treatment = treatment_repository.select(id)
    return render_template("treatments/show.html", treatment=treatment)

# NEW
@treatments_blueprint.route("/treatments/new")
def new_treatment():
    vets = vet_repository.select_all()
    pets = pet_repository.select_all()
    return render_template("/treatments/new.html", pets=pets, vets=vets)

# CREATE
@treatments_blueprint.route("/treatments", methods=["POST"])
def create_treatment():
    
    treatment_date = request.form["treatment_date"]
    procedure_type = request.form["procedure_type"]
    pet_id = request.form["pet_id"]
    vet_id = request.form["vet_id"]
    pet = pet_repository.select(pet_id)
    vet = vet_repository.select(vet_id)
    
    new_treatment = Treatment(treatment_date, procedure_type, pet, vet)
    treatment_repository.save(new_treatment)
    return redirect("/treatments")

# EDIT
@treatments_blueprint.route("/treatments/<id>/edit")
def edit_treatment(id):
    treatment = treatment_repository.select(id)
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("/treatments/edit.html", treatment=treatment, pets=pets, vets=vets)

# UPDATE
@treatments_blueprint.route("/treatments/<id>", methods=["POST"])
def update_treatment(id):
    treatment_date = request.form["treatment_date"]
    procedure_type = request.form["procedure_type"]
    pet_id = request.form["pet_id"]
    vet_id = request.form["vet_id"]
    pet = pet_repository.select(pet_id)
    vet = vet_repository.select(vet_id)
    
    new_treatment = Treatment(treatment_date, procedure_type, pet, vet, id)
    treatment_repository.update(new_treatment)
    return redirect("/treatments")


# DELETE
@treatments_blueprint.route("/treatments/<id>/delete", methods=["POST"])
def delete_treatment(id):
    treatment_repository.delete(id)
    return redirect("/treatments")