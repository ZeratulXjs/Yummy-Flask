from flask import Flask, render_template, request
from yumRecipes import *

app = Flask(__name__)
#users = users(uname, password)

@app.route('/', methods=['POST','GET'])
@app.route('/<uname>', methods=['GET', 'POST'])
def userdash(uname=None): 
    return render_template("index.html", uname=uname)

@app.route('/signup' , methods=['POST','GET'])
def signup():
    if request.method==['POST']:
        
        uname = request.form['uname']
        password = request.form['password']
        user = users(uname, password)
    
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)