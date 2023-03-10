import shelve

from flask import Blueprint, render_template
from flask import flash, render_template, redirect, url_for, request

from classes.Enquiry import Enquiry
from forms import createEnquiryForm

north = Blueprint('north', __name__)

@north.route('/north')
def viewNorth():
    return render_template("north/north.html")

@north.route('/north/KranjiMarshes')
def viewKranjiMarshes():
    return render_template("north/Kranji_Marshes.html")


@north.route('/north/HampsteadWetlandPark')
def viewHampsteadWetlandPark():
    return render_template("north/Hampstead_Wetlands_Park.html")
