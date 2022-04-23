from flask import Blueprint, Flask, redirect, render_template, request

from models.owner import Owner

import repositories.pet_repository as pet_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository

owners_blueprint = Blueprint("owners",__name__)
