from os import urandom
from flask import Flask, render_template, request, redirect, url_for, session, flash
from passlib.hash import sha256_crypt
from functools import wraps
from yumRecipes import RecipeForm, SignupForm

app = Flask(__name__)

# These lists will hold dictionary data and serve as the db's
users = []
recipe_list = []

# This is the index route that connects to the home view
@app.route('/', methods=['POST','GET'])
def index():
  return render_template("index.html")

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


# Login after signing up
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
      uname = request.form['uname']
      password_candidate = request.form['password']
      
      for item in users:
        if item['user'] == uname:
          password_real = item['pwd']                  
          if sha256_crypt.verify(password_candidate, password_real):
            session['logged_in'] = True
            session['username'] = uname
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
          else: 
            flash('Password incorrect', 'danger')
        break
      else:
        flash('User not found. Please Sign up', 'warning')   
          
    return render_template("login.html")

# Define authorisation to access restricted parts of the app
def user_logged_in(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      flash ('Unauthorised. Please login or signup', 'danger')
      return redirect(url_for('signup'))
  return wrap 


# Log out of session 
@app.route('/logout')
@user_logged_in
def logout():
  session.clear()
  flash('You are logged out', 'danger')
  return redirect(url_for('login'))

# User dashboard
@app.route('/dashboard', methods = ['POST', 'GET'])
@user_logged_in
def dashboard():
  if not recipe_list:
    flash('No recipes yet, add one!', 'warning')
    return render_template("dashboard.html")
  else:
    return render_template("dashboard.html", recipe_list=recipe_list)

# Add a recipe 
@app.route('/add_recipe', methods = ['POST', 'GET'])
@user_logged_in
def add_recipe():
  form = RecipeForm(request.form)
  if request.method == 'POST' and form.validate():
    title = form.title.data
    steps = form.steps.data

    recipe_list.append(dict({'Title':title,'Steps':steps, 'Author':session['username']}))

    flash('Recipe added!', 'success')
    app.logger.info('Recipe list : %s', recipe_list)
    return redirect(url_for('dashboard'))
  return render_template("add_recipe.html", form=form)

# List of recipes
@app.route('/recipe/<title>', methods = ['POST', 'GET'])
def recipe(title):
  return render_template("recipes.html", title=title) 


if __name__ == "__main__":
    app.secret_key = urandom(32)
    app.run(debug=True)
