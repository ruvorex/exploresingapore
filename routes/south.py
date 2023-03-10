import shelve

from flask import Blueprint, render_template
from flask import flash, render_template, redirect, url_for, request

from classes.Enquiry import Enquiry
from forms import createEnquiryForm

south = Blueprint('south', __name__)

@south.route('/south')
def viewSouth():
    return render_template("south/south.html")

@south.route('/south/LazarusIsland')
def viewLazarusIsland():
    return render_template("south/Lazarus_Island.html")


@south.route('/south/BerlayerCreekBoardwalk')
def viewBerlayerCreekBoardwalk():
    return render_template("south/Berlayer_Creek_Boardwalk.html")


@south.route('/south/StJamesPowerStation')
def viewStJamesPowerStation():
    return render_template("south/St_James_Power_Station.html")


@south.route('/south/VintageCameraMuseum')
def viewVintageCameraMuseum():
    return render_template("south/Vintage_Camera_Museum.html")


@south.route('/south/WoodInTheBooks')
def viewWoodInTheBooks():
    return render_template("south/Wood_In_The_Books.html")


@south.route('/south/RotundaLibraryArchive')
def viewRotundaLibraryArchive():
    return render_template("south/Rotunda_Library_Archive.html")
