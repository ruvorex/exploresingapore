import shelve

from flask import Blueprint, render_template
from flask import flash, render_template, redirect, url_for, request

from classes.Enquiry import Enquiry
from forms import createEnquiryForm

west = Blueprint('west', __name__)

@west.route('/west')
def viewWest():
    return render_template("west/west.html")

@west.route('/west/JunkiesCorner')
def viewJunkiesCorner():
    return render_template("west/Junkies_Corner.html")


@west.route('/west/MajuForest')
def viewMajuForest():
    return render_template("west/Maju_Forest.html")

