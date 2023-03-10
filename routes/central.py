import shelve

from flask import Blueprint, render_template
from flask import flash, render_template, redirect, url_for, request

from classes.Enquiry import Enquiry
from forms import createEnquiryForm

central = Blueprint('central', __name__)

@central.route('/central')
def viewCentral():
    return render_template("central/central.html")

@central.route('/central/DragonPlayground')
def viewDragonPlayground():
    return render_template("central/Dragon_Playground.html")


@central.route('/central/NationalOrchidGarden')
def viewNationalOrchidGarden():
    return render_template("central/National_Orchid_Garden.html")