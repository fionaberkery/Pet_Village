from flask import Blueprint, Flask, redirect, render_template, request

from models.price import Price

import repositories.price_repository as price_repository


prices_blueprint = Blueprint("/prices",__name__)

#INDEX 
@prices_blueprint.route("/prices/")
def prices():
    prices = price_repository.select_all()
    return render_template("/prices/index.html", prices=prices)

# SHOW
@prices_blueprint.route("/prices/<id>")
def select_price(id):
    price = price_repository.select(id)
    return render_template("/prices/show.html", price=price)


#NEW
@prices_blueprint.route("/prices/new")
def new_price():
    return render_template("/prices/new.html")

#CREATE
@prices_blueprint.route("/prices", methods=["POST"])
def create_price():
    treatment_type = request.form["treatment_type"]
    price = request.form["price"]
    time_req = request.form["time_req"]
    vet_req = request.form["vet_req"]
    nurses_req = request.form["nurses_req"]
    new_price = Price(treatment_type, price, time_req, vet_req, nurses_req)
    price_repository.save(new_price)
    return redirect("/prices")

# EDIT
@prices_blueprint.route("/prices/<id>/edit")
def edit_price(id):
    price = price_repository.select(id)
    return render_template("/prices/edit.html", price=price)

# UPDATE
@prices_blueprint.route("/prices/<id>", methods=["POST"])
def update_price(id):
    treatment_type = request.form["treatment_type"]
    price = request.form["price"]
    time_req = request.form["time_req"]
    vet_req = request.form["vet_req"]
    nurses_req = request.form["nurses_req"]
    new_price = Price(treatment_type, price, time_req, vet_req, nurses_req, id)
    price_repository.update(new_price)
    return redirect("/prices")

#DELETE
@prices_blueprint.route("/prices/<id>/delete", methods=["POST"])
def delete_price(id):
    price_repository.delete(id)
    return redirect("/prices")