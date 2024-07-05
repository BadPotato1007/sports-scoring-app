from flask import Flask,render_template, request
app = Flask(__name__)
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



if "__main__" == __name__:
    app.run(debug=True)



