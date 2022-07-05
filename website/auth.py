from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET", 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", user="None")


@auth.route('/logout')
def logout():
    return '<p>Logout</p>'


@auth.route('/sign-up', methods=["GET", 'POST'])
def sing_up():
    if request.method == 'POST':
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if (len(email) < 4):
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstName) < 5:
            flash('firstName must be greater than 2 characters', category='error')
        elif len(password1) < 2:
            flash('password1 must be greater than 2 characters', category='error')
        elif len(password2) < 2:
            flash('password2 must be greater than 2 characters', category='error')
        else:
            flash('Account created', category='success')

    return render_template("sign_up.html")
