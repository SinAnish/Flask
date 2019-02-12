from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'The Index!'

@app.route('/hello')
def hello():
    return "Hellllllllllo Warld!"

@app.route('/members')
def members():
    return "On the url please add /(your name) to be a member!"

@app.route("/members/<string:name>/")
def getMember(name):
    return name+ "Congrats, you are now a member!"



if __name__ == "__main__":
    app.run()