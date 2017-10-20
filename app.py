from flask import Flask, render_template, request, session, redirect, url_for, logging, flash 
from wtforms import Form, StringField, PasswordField, TextAreaField, validators
from passlib.hash import sha256_crypt
from os import urandom
from yumRecipes import Recipe, Users

app = Flask(__name__)

users = Users()
user_info = {}

# This is the index route that connects to the home view
@app.route('/', methods=['POST','GET'])
def index(): 
  return render_template("index.html", )

# Define form attributes for signup using WTForms to allow easy validation
class SignupForm(Form):
  uname = StringField('Username', [validators.Length(min=3, max=50), validators.DataRequired()])
  password = PasswordField('Password', [
    validators.DataRequired(),
    validators.Length(min=6),
    validators.EqualTo('password_rep', message='Passwords do not match'),
  ] )
  password_rep = PasswordField('Repeat Password', [validators.DataRequired()])

@app.route('/signup' , methods=['POST','GET'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
      uname = form.uname.data
      password = sha256_crypt.encrypt(str(form.password.data))

      user_info[uname] = password      
      
      users.user_list.append(user_info)

      flash('You have successfuly signed up!', 'success')

      return redirect(url_for('login'))
    return render_template('signup.html', form=form)


# This is the login route that connects to the login view
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
      uname = request.form['uname']
      password_candidate = request.form['password']
      
      for item in users.user_list:
        if item[uname] == uname:
          password_real = item.get[uname]                  
          if sha256_crypt.verify(password_candidate, password_real):
            app.logger.info("Login Success")

      app.logger.info("Username doesn't exist")
          
    return render_template("login.html")



my_recipes = Recipe()
nu_recipes = my_recipes.add_recipes()
@app.route('/recipes', methods = ['POST', 'GET'])
def recipes():
  return render_template("recipes.html", nu_recipes = nu_recipes)

@app.route('/recipe/<title>', methods = ['POST', 'GET'])
def recipe(title):
  return render_template("recipes.html", title = title)


if __name__ == "__main__":
    app.secret_key = urandom(32)
    app.run(debug=True)