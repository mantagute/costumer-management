from flask import Blueprint, render_template, request
from data_base.models.costumer import Costumer

costumer_route = Blueprint("costumer", __name__)

@costumer_route.route("/")
def get_all_costumers():
    costumers = Costumer.select()
    return render_template("get_all_costumers.html", costumers = costumers)

@costumer_route.route("/", methods = ["POST"])
def insert_new_costumer():
    
    data = request.json

    new_user = Costumer.create(
        Name = data['Name'],
        Email = data['Email']
    )
    
    return render_template("item_costumer.html",costumer = new_user)

@costumer_route.route("/new")
def costumer_form():
    return render_template("costumer_form.html")

@costumer_route.route("/<int:costumer_id>")
def get_costumer(costumer_id):

    costumer = Costumer.get(Costumer.id == (costumer_id))
    return render_template("get_costumer.html", costumer=costumer)

@costumer_route.route("/<int:costumer_id>/edit")
def edit_costumer_form(costumer_id):
    costumer = Costumer.get(Costumer.id == (costumer_id))
    return render_template("costumer_form.html", costumer=costumer)

@costumer_route.route("/<int:costumer_id>/update", methods = ["PUT"])
def update_costumer_form(costumer_id):
    data = request.json
    costumer = Costumer.get(Costumer.id == (costumer_id))
    costumer.Name = data['Name']
    costumer.Email = data['Email']
    costumer.save()

    return render_template("item_costumer.html", costumer=costumer)

@costumer_route.route("/<int:costumer_id>/delete", methods = ["DELETE"])
def delete_costumer(costumer_id):
    costumer = Costumer.get(Costumer.id == (costumer_id))
    costumer.delete_instance()
    return {"deleted": "ok"}