from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        location = request.form.get("location")
        if location:
            api_key = "c4b8c1d942d94f64a15173515251903"
            url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=yes"
            try:
                response = requests.get(url)
                data = response.json()
                weather_data = {
                    "location": f"{data['location']['name']}, {data['location']['country']}",
                    "temp": f"{data['current']['temp_c']}°C",
                    "condition": data["current"]["condition"]["text"],
                    "icon": data["current"]["condition"]["icon"]
                }
            except:
                weather_data = {"error": "Could not fetch weather data."}
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)

