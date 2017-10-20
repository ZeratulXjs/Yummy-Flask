from flask import Flask, render_template, request, session, redirect, url_for, logging, flash 
from passlib.hash import sha256_crypt
from os import urandom
from yumRecipes import Recipe, SignupForm

app = Flask(__name__)

users = []

# This is the index route that connects to the home view
@app.route('/', methods=['POST','GET'])
def index(): 
  return render_template("index.html", )

# Signing up without a database
@app.route('/signup' , methods=['POST','GET'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'GET':
      app.logger.info("Signed up users : %s", users)
    if request.method == 'POST' and form.validate():
      uname = form.uname.data
      password = sha256_crypt.encrypt(str(form.password.data))

      users.append(dict({'user':uname,'pwd':password}))

      app.logger.info("Signed up users : %s", users)
      flash('You have successfuly signed up!', 'success')

      return redirect(url_for('login'))
    return render_template('signup.html', form=form)


# This is the login route that connects to the login view
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
      uname = request.form['uname']
      password_candidate = request.form['password']
      
      for item in users:
        if item['user'] == uname:
          password_real = item['pwd']                  
          if sha256_crypt.verify(password_candidate, password_real):
            flash('Login successful!', 'success')
            return redirect (url_for('dashboard'))
          else: 
            flash('Password incorrect', 'danger')
        else:
          flash('User not found. Please Sign up', 'warning')   
          
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