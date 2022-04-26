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


# #NEW
# @nurses_blueprint.route("/nurses/new")
# def new_nurse():
#     return render_template("/nurses/new.html")

# #CREATE
# @nurses_blueprint.route("/nurses", methods=["POST"])
# def create_nurse():
#     nurse_name = request.form["nurse_name"]
#     days_works = request.form["days_works"]
#     available_weekends = request.form["available_weekends"]
#     email = request.form["email"]
#     new_nurse = Nurse(nurse_name, days_works, available_weekends, email)
#     nurse_repository.save(new_nurse)
#     return redirect("/nurses")

# # EDIT
# @nurses_blueprint.route("/nurses/<id>/edit")
# def edit_nurse(id):
#     nurse = nurse_repository.select(id)
#     return render_template("/nurses/edit.html", nurse=nurse)

# # UPDATE
# @nurses_blueprint.route("/nurses/<id>", methods=["POST"])
# def update_nurse(id):
#     nurse_name = request.form["nurse_name"]
#     days_works = request.form["days_works"]
#     available_weekends = request.form["available_weekends"]
#     email = request.form["email"]
#     new_nurse = Nurse(nurse_name, days_works, available_weekends, email, id)
#     nurse_repository.update(new_nurse)
#     return redirect("/nurses")

# #DELETE
# @nurses_blueprint.route("/nurses/<id>/delete", methods=["POST"])
# def delete_nurse(id):
#     nurse_repository.delete(id)
#     return redirect("/nurses")