import shelve

from flask import Blueprint, render_template
from flask import flash, render_template, redirect, url_for, request

from classes.Enquiry import Enquiry
from forms import createEnquiryForm

east = Blueprint('east', __name__)

@east.route('/east')
def viewEast():
    return render_template("east/east.html")

@east.route('/east/ChangiBayPoint')
def viewLazarusIsland():
    return render_template("east/Changi_Bay_Point.html")


@east.route('/east/JapaneseCemeteryPark')
def viewJapaneseCemeteryPark():
    return render_template("east/Japanese_Cemetery_Park.html")

