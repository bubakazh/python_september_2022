
from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


# most likely some of these routes wont be used

@app.route("/dojos")
def dojo_new():
    dojos = Dojo.get_all()
    return render_template('addshowDojo.html', all_dojos = dojos)

@app.route("/add_dojo", methods=['post'])
def dojo_create():
    Dojo.create(request.form)
    return redirect('/dojos')

@app.route("/dojo/<int:id>") #why does this route work?
def dojo_show(id):
    data = {'id' : id }
    return render_template('dojoInfo.html', dojo = Dojo.get_one_w_ninjas(data))