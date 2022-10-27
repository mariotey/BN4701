from flask import Flask, Response, render_template, request

user_stuff = {
    "name": "",
    "date": "",
    "day_of_week": "",
    "weather": "",
    "location": "",
    "region": ""
}

app = Flask(__name__)

#################################################################################################

@app.route("/")
def main_page():
    return render_template("main.html")

#################################################################################################

@app.route("/MMSE")
def mmse():
    return render_template("mmse.html")
#################################################################################################

@app.route("/Game", methods=["GET", "POST"])
def start_page():
    user_stuff["name"] = request.form.get("name")
    user_stuff["date"] = request.form.get("date")
    user_stuff["day_of_week"] = request.form.get("day_of_week")
    user_stuff["weather"] = request.form.get("weather")
    user_stuff["region"] = request.form.get("region")
    
    return render_template("game.html")

@app.route("/GameNew")
def restart_page():
    return render_template("game.html")

@app.route("/Instructions")
def instruction_page():
   return render_template("instruct.html")

#################################################################################################

@app.route("/VoidDeck")
def voiddeck_page():
    return render_template("map.html")

@app.route("/WetMarket")
def wetmarket_page():
    return render_template("map.html")

@app.route("/Park")
def park_page():
    return render_template("map.html")

@app.route("/HawkerCentre")
def hawkercentre_page():
    return render_template("map.html")

#################################################################################################
if __name__ == "__main__":
    app.run(debug=True)

# .\venv\Scripts\python.exe -m pylint .\Walk-E\main.py