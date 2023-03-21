from flask import Flask, render_template

Pyfit = Flask(__name__)

@Pyfit.route('/')
def index():
    return render_template("index.html")

@Pyfit.route('/login')
def login():
    return render_template("login.html")

@Pyfit.route('/registro')
def registro():
    return render_template("registro.html")


if __name__ == '__main__':
    Pyfit.run(debug = True)