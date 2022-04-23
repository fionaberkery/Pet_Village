from flask import Blueprint, Flask, redirect, render_template, request

from models.vet import Vet

import repositories.pet_repository as pet_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository

vets_blueprint = Blueprint("vets",__name__)
