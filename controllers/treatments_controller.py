from flask import Blueprint, Flask, redirect, render_template, request

from models.treatment import Treatment

import repositories.pet_repository as pet_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository

treatments_blueprint = Blueprint("treatments",__name__)
