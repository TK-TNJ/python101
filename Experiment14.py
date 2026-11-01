# Develop a Python program to process weather information obtained in sample JSON 
# dataset or public weather API. The program should parse JSON data to extract 
# temperature, humidity, and location details, convert nested JSON structures into a 
# tabular format using Python, and display summarized weather reports for multiple 
# cities.


import json
import pandas as pd

# Sample JSON weather dataset
weather_data = '''
{
    "weather": [
        {
            "location": {
                "city": "Thrissur",
                "country": "India"
            },
            "temperature": 32,
            "humidity": 70
        },
        {
            "location": {
                "city": "Kochi",
                "country": "India"
            },
            "temperature": 30,
            "humidity": 80
        },
        {
            "location": {
                "city": "Calicut",
                "country": "India"
            },
            "temperature": 28,
            "humidity": 65
        }
    ]
}
'''

# Parse JSON data
data = json.loads(weather_data)

# Convert JSON into tabular format
df = pd.json_normalize(data['weather'])

# Display weather information
print("----- WEATHER INFORMATION -----")
print(df)

# Extract weather details
print("\n----- WEATHER REPORT -----")

for city in data['weather']:
    name = city['location']['city']
    country = city['location']['country']
    temp = city['temperature']
    humidity = city['humidity']

    print("\nCity:", name)
    print("Country:", country)
    print("Temperature:", temp, "°C")
    print("Humidity:", humidity, "%")

# Generate summary report
print("\n----- WEATHER SUMMARY -----")

print("Total Cities:", len(data['weather']))
print("Average Temperature:", df['temperature'].mean(), "°C")
print("Average Humidity:", df['humidity'].mean(), "%")

# Find hottest city
hottest = df.loc[df['temperature'].idxmax()]
print("Hottest City:", hottest['location.city'])

# Find coldest city
coldest = df.loc[df['temperature'].idxmin()]
print("Coldest City:", coldest['location.city'])
