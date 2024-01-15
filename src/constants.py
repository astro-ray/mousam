import os
icon_loc = "/app/share/icons/hicolor/scalable/weather_icons/" if not os.getenv('SNAP') else f"{os.getenv('SNAP')}/usr/share/icons/hicolor/scalable/weather_icons/"

icons = {
    "0": icon_loc + "clear-day.svg",
    "1": icon_loc + "clear-day.svg",
    "2": icon_loc + "overcast-day.svg",
    "3": icon_loc + "overcast.svg",
    "51": icon_loc + "partly-cloudy-day-drizzle.svg",
    "53": icon_loc + "drizzle.svg",
    "55": icon_loc + "overcast-drizzle.svg",
    "56": icon_loc + "partly-cloudy-day-snow.svg",
    "57": icon_loc + "overcast-snow.svg",
    "61": icon_loc + "partly-cloudy-day-rain.svg",
    "63": icon_loc + "rain.svg",
    "65": icon_loc + "thunderstorms-rain.svg",
    "66": icon_loc + "overcast-snow.svg",
    "67": icon_loc + "thunderstorms-rain.svg",
    "45": icon_loc + "fog.svg",
    "48": icon_loc + "fog.svg",
    "71": icon_loc + "partly-cloudy-day-snow.svg",
    "73": icon_loc + "snow.svg",
    "75": icon_loc + "snowflake.svg",
    "77": icon_loc + "snowflake.svg",
    "80": icon_loc + "overcast-day-rain.svg",
    "81": icon_loc + "rain.svg",
    "82": icon_loc + "thunderstorms-rain.svg",
    "85": icon_loc + "snow.svg",
    "86": icon_loc + "snowflake.svg",
    "95": icon_loc + "thunderstorms-rain.svg",
    "96": icon_loc + "thunderstorms-day-overcast-snow.svg",
    "99": icon_loc + "snowflake.svg",
    
    "0n": icon_loc + "clear-night.svg",
    "1n": icon_loc + "clear-night.svg",
    "2n": icon_loc + "overcast-night.svg",
    "3n": icon_loc + "overcast.svg",
    "51n": icon_loc + "partly-cloudy-night-drizzle.svg",
    "53n": icon_loc + "drizzle.svg",
    "55n": icon_loc + "overcast-drizzle.svg",
    "56n": icon_loc + "partly-cloudy-night-snow.svg",
    "57n": icon_loc + "overcast-snow.svg",
    "61n": icon_loc + "partly-cloudy-night-rain.svg",
    "63n": icon_loc + "rain.svg",
    "65n": icon_loc + "thunderstorms-rain.svg",
    "66n": icon_loc + "overcast-snow.svg",
    "67n": icon_loc + "thunderstorms-rain.svg",
    "45n": icon_loc + "fog.svg",
    "48n": icon_loc + "fog.svg",
    "71n": icon_loc + "partly-cloudy-night-snow.svg",
    "73n": icon_loc + "snow.svg",
    "75n": icon_loc + "snowflake.svg",
    "77n": icon_loc + "snowflake.svg",
    "80n": icon_loc + "overcast-night-rain.svg",
    "81n": icon_loc + "rain.svg",
    "82n": icon_loc + "thunderstorms-rain.svg",
    "85n": icon_loc + "snow.svg",
    "86n": icon_loc + "snowflake.svg",
    "95n": icon_loc + "thunderstorms-rain.svg",
    "96n": icon_loc + "thunderstorms-night-overcast-snow.svg",
    "99n": icon_loc + "snowflake.svg",
    "arrow": icon_loc + "arrow.svg",
}

bg_css = {
    "01d": "clear_sky",
    "02d": "few_clouds",
    "03d": "overcast",
    "04d": "overcast",
    "09d": "showers_scattered",
    "10d": "showers_large",
    "11d": "storm",
    "13d": "snow",
    "50d": "fog",
    "01n": "clear_sky_night",
    "02n": "few_clouds_night",
    "03n": "overcast_night",
    "04n": "showers_scattered_night",
    "09n": "showers_large_night",
    "10n": "showers_large_night",
    "11n": "storm_night",
    "13n": "snow_night",
    "50n": "fog_night",
}
# 1 ->   indicates day
# 1n ->  indicates night

conditon = {
    "0": "Clear sky",
    "1": "Few Clouds",
    "2": "Partly Cloudy",
    "3": "Overcast",
    "45": "Fog",
    "48": "Mist",
    "51": "Light Drizzle",
    "53": "Moderate Drizzle",
    "55": "Heavy Intensity Drizzle ",
    "56": "Light Freezing Drizzle",
    "57": "Heavy Freezing Drizzle",
    "61": "Light Rain",
    "63": "Moderate Rain",
    "65": "Heavy Rain",
    "66": "Light Freezing Rain",
    "67": "Heavy Freezing Rain",
    "71": "Light Snow Fall",
    "73": "Moderate Snow Fall",
    "75": "Heavy Snow Fall	",
    "77": "Snow grains",
    "80": "Light Rain Showers",
    "81": "Moderate Rain Showers",
    "82": "Heavy Rain Showers",
    "85": "Light Snow Showers",
    "86": "Heavy Snow Showers ",
    "95": "Thunderstorm",
    "96": "Thunderstorm with Hail",
}
