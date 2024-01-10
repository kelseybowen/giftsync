from flask_app import app
from flask_app.models import list, gift
from flask import render_template, session, redirect, request

# TODO is_public - always returns false even when checked  

@app.route('/list/new')
def new_list():
    return render_template('new_list.html')

@app.route('/list/save', methods=["POST"])
def save_list():
    data = {
        "name": request.form["list_name"],
        "description": request.form["description"],
        "is_public": request.form.get("is_public"),
        "owner_id": session["user"][0]["id"]
    }
    print(data["is_public"])
    list_id = list.List.create_list(data)
    return redirect(f'/list/{list_id}')

@app.route('/list/<int:list_id>')
def view_one_list(list_id):
    gift_list = gift.Gift.get_all_gifts_on_list(list_id)
    return render_template("list_detail.html", gift_list=gift_list)

# #update list
# @app.route('/list/update')

# # delete list
# @app.route('/list/delete')

