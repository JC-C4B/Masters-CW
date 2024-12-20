document.getElementById('weather-form').addEventListener('submit', handleClick);


function handleClick(event) {
    event.preventDefault();
    var city = document.getElementById('city').value;
    if (city == "New York") {
        getWeather("OKX", 33, 35);
    } else if (city == "Boston") {
        getWeather("BOX", 71, 90);
    } else if (city == "Orlando") {
        getWeather("MLB", 26, 68);
    } else if (city == "Chicago") {
        getWeather("LOT", 76, 73);
    } else if (city == "Washington") {
        getWeather("LWX", 96, 72);
    } else if (city == "Atlanta") {
        getWeather("FFC", 51, 87);
    } else if (city == "Seattle") {
        getWeather("SEW", 125, 68);
    } else if (city == "San Francisco") {
        getWeather("MTR", 85, 105);
    } else if (city == "Los Angeles") {
        getWeather("LOX", 155, 45);
    } 
    // Added the functionality of our Current Location button below:
    else if (city == "Current Location") {

        // Using our new function to find the longitude and latitude
        getLatLong(function(latitude, longitude) {
            console.log("Latitude:", latitude);
            console.log("Longitude:", longitude);

            // Plugging in the Longitude and latitude to find the office, gridX, and gridY
            getLocation(latitude, longitude, function(cwa, gridX, gridY) {
                console.log('CWA:', cwa);
                console.log('gridX:', gridX);
                console.log('gridY:', gridY);

                // Finally getting the weather using the information previously retrieved!
                getWeather(cwa, gridX, gridY);
            });
        });
    }
}

// Our function to find the Latitude and Longitude of the current location
// And return it afterward (through callback)
function getLatLong(callback){
    navigator.geolocation.getCurrentPosition(
        function(position) {
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;
            callback(latitude, longitude);
        }
    );
}

// Remodeling our function from Module 3 to JS in order to get the office, gridX, and gridY 
function getLocation(latitude, longitude, callback) {
    fetch('https://api.weather.gov/points/' + latitude + ',' + longitude)
        .then(function(response) {
            return response.json();
        })
        .then(function(data){
            const properties = data.properties;
            if (properties) {
                const cwa = properties.cwa;
                const gridX = properties.gridX;
                const gridY = properties.gridY;
                callback(cwa, gridX, gridY);
            }
        });
}

function getWeather(office,gridX,gridY) {
    var url = 'https://api.weather.gov/gridpoints/' + office + '/' + gridX + "," + gridY + "/forecast";
    fetch(url)
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            displayWeather(data);
        })
        .catch(function(error) {
            console.log(error);
        });
}

function displayWeather(data) {
    var weatherInfo = document.getElementById('weather-info');
    weatherInfo.innerHTML = '';
    if (data.type === "Feature") {
        var period = data.properties.periods[0].name;
        var temperature = data.properties.periods[0].temperature;
        var trend = data.properties.periods[0].temperatureTrend;
        var humidity = data.properties.periods[0].relativeHumidity.value;
        var windSpeed = data.properties.periods[0].windSpeed;
        var direction = data.properties.periods[0].windDirection;
        var forecast = data.properties.periods[0].detailedForecast;
        // Wanted to try returning an image based off of weather conditions
        var weatherCondition = forecast.toLowerCase();
        var pictureUrl = getPicture(weatherCondition);
        var weatherHtml = '<h2>Weather Forecast for ' + period + '</h2>' +
            '<p>Temperature: ' + temperature + ' &#8451;</p>' +
            '<p>Humidity: ' + humidity + '%</p>' +
            '<p>Wind Speed: ' + windSpeed + ' m/s ' + direction + '</p>' +
            '<h3> Forecast </h3>' +
            '<p>' + forecast + '</p>' +
            '<img src="' + pictureUrl + '"alt="Current Weather Image">';
        weatherInfo.innerHTML = weatherHtml;
    } else {
        weatherInfo.innerHTML = '<p>Failed to retrieve weather information.</p>';
    }
}

// Function to get our picture URLs for display
function getPicture(condition) {
    var PictureUrls = {
        'rain': 'P6/images/rainy.jpg',
        'cloudy': 'P6/images/cloudy.jpg',
        'sunny': 'P6/images/sunny.jpg'
    };

    // Placeholder image if none of the conditions are matched
    var PlaceholderPicture = 'P6/images/sky.jpg';

    return PictureUrls[condition] || PlaceholderPicture;
}