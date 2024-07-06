from flask import Flask,render_template, request
import flask
import firebase_admin
from firebase_admin import firestore

# Application Default credentials are automatically created.
# app = firebase_admin.initialize_app()
# db = firestore.client()
# doc_ref = db.collection("users").document("alovelace")
# doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

app = Flask(__name__)
@app.route('/')
def index():
    res = flask.make_response()
    res.set_cookie("name", value="I am cookie")

@app.route("/")
def Home():
    return render_template("home_page.html")
@app.route("/teams")
def Teams():
    return render_template("teams.html")
@app.route("/choose")
def Choose():
    return render_template("choose.html")
@app.route("/choose",methods=["POST"])
def sport_select():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route("/cricket")
def Cricket():
    return render_template("cricket.html")



if "__main__" == __name__:
    app.run(debug=True)



