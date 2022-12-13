import sqlite3 as sq


def put_user_data(user_id,
                  first_name,
                  user_coordinates_latitude,
                  user_coordinate_longitude):
    con = None

    try:
        con = sq.connect('user_data.db')
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users_data (
                user_id INTEGER PRIMARY KEY,
                first_name varchar(64),
                user_coordinates_latitude REAL,
                user_coordinate_longitude REAL
                )
                """)

        con.commit()

        cur.execute("""INSERT INTO users_data VALUES (?, ?, ?, ?) 
                ON CONFLICT(user_id) DO UPDATE SET
                    user_coordinates_latitude = ?,
                    user_coordinate_longitude = ?
                """, (user_id,
                      first_name,
                      user_coordinates_latitude,
                      user_coordinate_longitude,
                      user_coordinates_latitude,
                      user_coordinate_longitude))

        con.commit()

    except sq.Error as e:
        if con:
            con.rollback()
        print('Request error')
        print(e)
    finally:
        if con:
            con.close()


def get_coordinates(user_id):
    con = sq.connect('user_data.db')
    cur = con.cursor()
    cur.execute("SELECT user_coordinates_latitude, user_coordinate_longitude FROM users_data WHERE user_id = ?",
                (user_id,))
    coordinates = cur.fetchone()
    con.close()
    return coordinates


# Function which will take all returns from api_server.py and put it in one table in user_data_db

def put_weather_data(user_id,
                     location,
                     temperature_cel,
                     temperature_cel_feeling,
                     temperature_fah,
                     temperature_fah_feeling,
                     description,
                     sunrise,
                     sunset,
                     wind_speed,
                     wind_speed_mph,
                     wind_direction,
                     country):
    con = None

    try:
        con = sq.connect('user_data.db')
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS weather_data (
                    user_id INTEGER PRIMARY KEY,
                    location varchar(64),
                    temperature_cel REAL,
                    temperature_cel_feeling REAL,
                    temperature_fah REAL,
                    temperature_fah_feeling REAL,
                    description varchar(64),
                    sunrise varchar(64),
                    sunset varchar(64),
                    wind_speed REAL,
                    wind_speed_mph INTEGER,
                    wind_direction varchar(64),
                    country varchar(64)
                    )
                    """)

        con.commit()

        cur.execute("""INSERT INTO weather_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) 
                    ON CONFLICT(user_id) DO UPDATE SET
                        location = ?,
                        temperature_cel = ?,
                        temperature_cel_feeling = ?,
                        temperature_fah = ?,
                        temperature_fah_feeling = ?,
                        description = ?,
                        sunrise = ?,
                        sunset = ?,
                        wind_speed = ?,
                        wind_speed_mph = ?,
                        wind_direction = ?,
                        country = ?
                    """, (user_id,
                          location,
                          temperature_cel,
                          temperature_cel_feeling,
                          temperature_fah,
                          temperature_fah_feeling,
                          description,
                          sunrise,
                          sunset,
                          wind_speed,
                          wind_speed_mph,
                          wind_direction,
                          country,
                          location,
                          temperature_cel,
                          temperature_cel_feeling,
                          temperature_fah,
                          temperature_fah_feeling,
                          description,
                          sunrise,
                          sunset,
                          wind_speed,
                          wind_speed_mph,
                          wind_direction,
                          country
                          ))

        con.commit()

    except sq.Error as e:
        if con:
            con.rollback()
        print('Request error')
        print(e)
    finally:
        if con:
            con.close()


def get_weather_data(user_id):
    con = sq.connect('user_data.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM weather_data WHERE user_id = ?", (user_id,))
    weather_data = cur.fetchone()
    con.close()
    return weather_data
