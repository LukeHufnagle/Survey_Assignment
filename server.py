from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret survey"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def results():
    name = request.form['name']
    session['name'] = name
    location = request.form['location']
    session['location'] = location
    language = request.form['language']
    session['language'] = language
    comment = request.form['comment']
    session['comment'] = comment
    return redirect("/show")

@app.route('/show')
def showUser():
    return render_template("show.html")

@app.route('/return')
def goBack():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)