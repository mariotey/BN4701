from datetime import datetime 
from flask import Flask, Response, render_template, request

app = Flask(__name__)

#################################################################################################

@app.route("/")
def main_page():
    return render_template("main.html")

#################################################################################################

@app.route("/Game")
def start_page():
    return render_template("game.html")

@app.route("/Instructions")
def instruction_page():
   return render_template("instruct.html")

# @app.route("/Edit")
# def edit_page():
#    return render_template("edit.html")

#################################################################################################

@app.route("/VoidDeck")
def voiddeck_page():
    return "VoidDeck"

@app.route("/WetMarket")
def wetmarket_page():
    return "WetMarket"

@app.route("/Park")
def park_page():
    return "Park"

@app.route("/HawkerCentre")
def hawkercentre_page():
    return "HawkerCentre"

#################################################################################################
if __name__ == "__main__":
    app.run(debug=True)

# .\venv\Scripts\python.exe -m pylint .\Walk-E\main.py