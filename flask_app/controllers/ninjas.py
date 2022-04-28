from flask import render_template, redirect, request
from ..models import dojo
from flask_app.models.ninja import Ninja
from flask_app import app


@app.route('/ninja')
def add_ninja():
    dojos = dojo.Dojo.get_all()
    return render_template("form.html", all_dojos=dojos)


@app.route('/ninjas/create', methods=['post'])
def create_ninja():
    dojo_id = request.form['dojo_id']
    Ninja.add(request.form)
    return redirect(f'/dojos/{dojo_id}')
