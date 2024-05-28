# Importing necessary Libraries
import requests

# Defining our client side forecast function
def get_forecast(latitude, longitude):
    url = 'http://127.0.0.1:5000/forecast'
    params = {'latitude': latitude, 'longitude': longitude}

    try:
        response = requests.get(url, params=params)

        # Case if successful
        if response.status_code == 200:
            data = response.json()
            return data

        # Case if not successful
    except requests.RequestException:
        print("Sorry, an error occured.")

    return None

# Defining our main function
def main():

    try:
        # Asking for user input
        latitude = float(input("Enter the latitude: "))
        longitude = float(input("Enter the longitude: "))

        # Plugging it in
        forecast = get_forecast(latitude, longitude)

        # Cases for printing the response from the weather API
        for forecast_data in forecast:
                print(f"Detailed Forecast: {forecast_data['detailed_forecast']}\n")
        else:
            print("Couldn't find the forecast data!")
    except ValueError:
        print("Invalid input. Please try again!")

# Calling our main function
if __name__ == "__main__":
    main()
