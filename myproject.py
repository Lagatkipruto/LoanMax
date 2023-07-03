from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('loan.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    return render_template('login.html')

@app.route('/register_form', methods=['POST', 'GET'])
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
