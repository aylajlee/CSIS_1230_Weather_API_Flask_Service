import requests
import psycopg2

# 1
# 데이터베이스 연결 설정
db_connection_params = {
    "host": "localhost",
    "database": "weather_db", # DB Name
    "user": "postgres", # PostgreSQL User
    "password": "Juyeon7347!", # PostgreSQL Password
    "port": "5432"
}

# 2
# 날씨 관측 대상: 도시 리스트 
cities = ["Seoul", "Chicago", "New York", 
          "Bern", "Rome", "Bogota", 
          "Kigali", "New Delhi", "Islamabad", "Stockholm"]

def populate_weather_data():
    try:
        connection = psycopg2.connect(**db_connection_params)
        cursor = connection.cursor()
        print("PostgreSQL Database is successfully connected.")

        for city_name in cities:
            # Geocoding API call
            # 도시의 위도와 경도 
            geocoding_api_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"
            geo_response = requests.get(geocoding_api_url).json()
            
            if 'results' in geo_response:
                location_data = geo_response['results'][0]
                latitude = location_data['latitude']
                longitude = location_data['longitude']
                country_code = location_data.get('country_code', 'Unknown')
                # Weather API call
                # 현재 날씨 정보
                weather_api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
                weather_response = requests.get(weather_api_url).json()
                current_weather_info = weather_response['current_weather']

                temperature_c = current_weather_info['temperature']
                windspeed_kmh = current_weather_info['windspeed']
                observation_time = current_weather_info['time']

                # SQL
                # insert data on observations table
                insert_statement = """
                    INSERT into observations (city, country, latitude, longitude, temperature_c, windspeed_kmh, observation_time)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                
                cursor.execute(insert_statement, (
                    city_name, 
                    country_code,
                    latitude, 
                    longitude, 
                    temperature_c, 
                    windspeed_kmh, 
                    observation_time
                ))
                print(f"Successfully saved observation for: {city_name}")
            
            else:
                print(f"It couldn't find coordinates for {city_name}")
        
        connection.commit()
        
        print(f"All {len(cities)} records have been populated into the database.")
        
        cursor.close()
        
        connection.close()

    except Exception as error:
        print(f"ERROR Database operation: {error}")

if __name__ == "__main__":
    populate_weather_data()
    