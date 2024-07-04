from flask import Flask,render_template
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
if "__main__" == __name__:
    app.run(debug=True)