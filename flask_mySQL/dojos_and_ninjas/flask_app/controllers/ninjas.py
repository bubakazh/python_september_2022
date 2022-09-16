
from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/ninja")
def ninja_new():
    dojos = Dojo.get_all()
    return render_template('addNinja.html', all_dojos = dojos)

@app.route("/add_ninja", methods=['post'])
def ninja_create():
    Ninja.create(request.form)
    return redirect(f"/dojo/{request.form['dojo_id']}")