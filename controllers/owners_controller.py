from flask import Blueprint, Flask, redirect, render_template, request

from models.owner import Owner

import repositories.pet_repository as pet_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository

owners_blueprint = Blueprint("/owners",__name__)

#INDEX 
@owners_blueprint.route("/owners/")
def owners():
    owners = owner_repository.select_all()
    return render_template("/owners/index.html", owners=owners)

#SHOW
@owners_blueprint.route("/owners/<id>")
def select_owner(id):
    owner = owner_repository.select(id)
    return render_template("/owners/show.html", owner=owner)


#NEW
@owners_blueprint.route("/owners/new")
def new_owner():
    return render_template("/owners/new.html")

#CREATE
@owners_blueprint.route("/owners", methods=["POST"])
def create_owner():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    mobile = request.form["mobile"]
    new_owner = Owner(first_name, last_name, email, mobile)
    owner_repository.save(new_owner)
    return redirect("/owners")

    # EDIT
@owners_blueprint.route("/owners/<id>/edit")
def edit_owner(id):
    owner = owner_repository.select(id)
    return render_template("/owners/edit.html", owner=owner)

# UPDATE
@owners_blueprint.route("/owners/<id>", methods=["POST"])
def update_owner(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    mobile = request.form["mobile"]
    new_owner = Owner(first_name, last_name, email, mobile)
    owner_repository.update(new_owner)
    return redirect("/owners")

#DELETE
@owners_blueprint.route("/owners/<id>/delete", methods=["POST"])
def delete_owner(id):
    owner_repository.delete(id)
    return redirect("/owners")