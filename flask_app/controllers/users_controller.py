from flask_app import app
import os
from flask import render_template, request, redirect, session, flash, url_for
from flask_app.models import user
from authlib.integrations.flask_client import OAuth

oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    client_kwargs={'scope': 'email profile'},
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration'
)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    resp.raise_for_status()
    user_info = resp.json()
    print(user_info)
    user_data = {
        "name": user_info["name"],
        "email": user_info["email"]
    }
    if not user.User.get_user_by_email(user_data['email']):
        user.User.create_user(user_data)
    session["user"] = user.User.get_user_by_email(user_data["email"])
    session["email"] = user_info["email"]
    return redirect('/dashboard')


# @app.route('/register', methods=["POST"])
# def register():
#     if not user.User.validate_registration(request.form):
#         session["first_name"] = request.form["first_name"]
#         session["last_name"] = request.form["last_name"]
#         session["email"] = request.form["r_email"]
#         return redirect('/')
#     data = {
#         "first_name": request.form["first_name"],
#         "last_name": request.form["last_name"],
#         "email": request.form["r_email"],
#         "password": bcrypt.generate_password_hash(request.form["r_password"])
#     }
#     user_id = user.User.create_user(data)
#     session["user_id"] = user_id
#     session["first_name"] = data["first_name"]
#     return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    # all_users = user.User.get_all_users()
    # active_user = user.User.get_user_by_id(session["user_id"])
    return render_template("dashboard.html")

# @app.route('/delete_user/<int:user_id>', methods=["POST"])
# def delete_user(user_id):
#     if "user_id" in session:
#         user.User.delete_user(user_id)
#         session.clear()
#     return redirect('/')

@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')