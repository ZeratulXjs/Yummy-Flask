from flask import Flask, render_template, request
from yumRecipes import *

app = Flask(__name__)
#users = users(uname, password)

@app.route('/', methods=['POST','GET'])
def index():
    return render_template("index.html")

@app.route('/signup' , methods=['POST','GET'])
def signup_success():
    uname = request.form['uname']
    password = request.form['password']
    user = users(uname, password)
    
    return render_template("signup_success.html")

@app.route('/dash', methods=['POST','GET'])
def dash():
    return render_template("dashboard.html")

# @app.route('/dash/<str:usr')
# def user_dash(usr):
#   users.get(usr)
#   return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)