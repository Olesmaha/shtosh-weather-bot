  FROM python:3.11
  WORKDIR /shtosh-weather-bot
  COPY requirements.txt /shtosh-weather-bot
  RUN pip install -r requirements.txt
  COPY . /shtosh-weather-bot
  RUN bot.py