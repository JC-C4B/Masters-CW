# For some help oustide of the provided content in class
# I referred to this website: 
# https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask

# Importing necessary libraries
from flask import Flask, request, jsonify
import requests

# Creating our app
app = Flask(__name__)

# Defining our function to get the necessary data using inputted latitude & longitude
def get_location(latitude, longitude):


    response = requests.get(f"https://api.weather.gov/points/{latitude},{longitude}")

    # I kept running into issues where my code wouldn't work properly even with valid 
    # Longitudes and latitudes, and implementing these case scenarios fixed that thankfully:

    # Case if the input was successfully accepted
    if response.status_code == 200:
        data = response.json()
        properties = data.get("properties")
        if properties:
            return properties.get("cwa"), properties.get("gridX"), properties.get("gridY")

    # Case if it was not accepted
    return None, None, None

# Defining our function to find the forecast using the data we got from the location function
def get_forecast(office, gridX, gridY):

    response = requests.get(f"https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast")

    # Case if the input was successfully accepted
    if response.status_code == 200:
        data = response.json()
        important_stuff = []

        # Only printing out a portion of the information to not make such a big mess
        for forecast in data['properties']['periods']:
            forecast_data = {
                'name': forecast['name'],
                'detailed_forecast': forecast['detailedForecast']
            }
            important_stuff.append(forecast_data)

        # Returning the edited list
        return important_stuff

    # Case if the input failed
    return None

# Defining our route, and the function to go along with it
@app.route('/forecast', methods=['GET'])
def forecast():

    # Asking for user input
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))

    # Plugging user input into our location function
    office, gridX, gridY = get_location(latitude, longitude)

    # If we get data, we plug it into our forecast function
    if office and gridX and gridY:
        forecast_data = get_forecast(office, gridX, gridY)
        if forecast_data:
            return jsonify(forecast_data), 200

    # Case if we didn't get data for the forecast
    return jsonify({"error": "Forecast data not found."}), 404

# Calling our main function
if __name__ == '__main__':
    app.run(debug=False)
