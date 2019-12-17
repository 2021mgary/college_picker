from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/results', methods = ["get", "post"])
def results():
    x = 0
    information = dict(request.form)
    print(information)
    gender = int(information["gender"])
    distance = int(information["distance"])
    size = int(information["size"])
    ownership = int(information["ownership"])
    enviornment = int(information["enviornment"])
    skilled = int(information["skilled"])
    type = int(information["type"])
    grades = int(information["grades"])
    x = gender + distance + size + ownership + enviornment + skilled + type + grades
    # if x in range(0,7):
    #     college = "city college of new york"
    # elif x in range(7,11):
    #     college = "fordham university"
    # elif x in range(11,15):
    #     college = "UCLA"
    # elif x in range(15,19):
    #     college = "amherst college"
    # elif x in range(19,24):
    #     college = "barnard college"
    # elif x in range(24,26):
    #     college = "morehouse college"
    # elif x in range(25,27):
    #     college = "stanford university"
    # elif x in range(27,28):
    #     college = "MIT"
    # else:
    #     college = "no college"
    output = model.college(x)
    print(output)
    return render_template("results.html", college = output)
