
from flask import Flask, render_template, request, redirect, url_for, session, logging
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL,MySQLdb
import bcrypt

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("home2.html")
    
@app.route("/Acercade")
def Acercade():
   return render_template("Acerca2.html")

@app.route("/Trilladora")
def Trilladora():
    return render_template("Trilladoras2.html")

@app.route("/foro")
def foro():
    return render_template("Foro2.html")

@app.route("/login")
def Acerca():
    return render_template("login.html")

@app.route("/registro", methods = ["GET", "POST"])
def Trilladoras():
    if request.method == "GET":
        return render_template("registro.html")
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password , bcrypt.gensalt())


        cur = mysql.conection.cursor()
        cur.execute("INSERT INTO user ( name, email, password) VALUES (%s, %s, %s)", (name,email, hash_password,))
        mysql.conection.commit()
        session['name'] = name
        session['email'] = email
        return redirect(url_for("home"))


@app.route("/informate")
def Foro():
   return render_template("informate2.html")

if __name__ == '__main__':
    app.secret_key = "^A%DJAJU^JJ123"
    app.run(debug=True)