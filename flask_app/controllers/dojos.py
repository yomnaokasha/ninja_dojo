from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app import app


@app.route('/dojos')
def show():
    dojo = Dojo.get_all()
    return render_template("dojos.html", all_dojos=dojo)


@app.route('/dojos/create', methods=['post'])
def create_Dojo():
    Dojo.add(request.form)
    return redirect('/dojos')


@app.route('/dojos/<int:dojo_id>')
def show_one(dojo_id):
    dojo = Dojo.get_one(dojo_id)
    ninjas = Ninja.find_for_dojo(dojo_id)
    return render_template("dojo_show.html", ninjas=ninjas, dojo=dojo)
