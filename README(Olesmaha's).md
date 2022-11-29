Hello everyone. It's simple weather bot based on this project https://github.com/lesskop/shtosh-weather-bot
Advantage of this bot is that for getting information about weather, wind speed and sunrise/sunset, this bot takes 
geolocation of user, not server. Also, I changed some buttons and add simple tuple for users data (it actually
better transform to SQL database in future).
Anyway.
Full and simple instructions you will find inside the original readme file, but here is peculiarities:
1. You have to put token of your bot to BOT_TOKEN = '*HERE*' field, inside .env file.
2. You have to put your API key to WEATHER_API_KEY = '*HERE*' field, inside .env file.
3. You have to put your API call to WEATHER_API_CALL_1 = '*HERE*' and WEATHER_API_CALL_2 = '*HERE*' fields.
The reason why I separate weather API call for two parts is feature of my own call that is API key is between
two parts of characteristic of call. If your call is different you don't need that option, but don't forget to
change CURRENT_WEATHER_API_CALL in config.py file. 
