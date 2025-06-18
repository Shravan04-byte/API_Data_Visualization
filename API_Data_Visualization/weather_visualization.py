import requests
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os

# ✅ Your API key
API_KEY = '43eed0894f5c766ff9901e3c3e89c180'

# ✅ List of cities you want to visualize
cities = ['Pune', 'Mumbai', 'Delhi', 'Chennai', 'Kolkata']

# ✅ OpenWeatherMap Forecast API base URL
base_url = 'http://api.openweathermap.org/data/2.5/forecast'

# ✅ Create output directory for graphs (optional)
os.makedirs('graphs', exist_ok=True)

for city in cities:
    print(f"\nFetching data for {city}...")

    # 📥 API request
    url = f"{base_url}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    # ❌ Error handling
    if 'list' not in data:
        print(f"❌ API ERROR for {city}:", data)
        continue

    # ✅ Save JSON data to file
    with open(f"{city}_forecast.json", "w") as f:
        json.dump(data, f, indent=4)

    # 📊 Extract date-time and temperature
    dates = [item['dt_txt'] for item in data['list']]
    temps = [item['main']['temp'] for item in data['list']]

    # 📈 Plot graph
    plt.figure(figsize=(12, 5))
    sns.lineplot(x=dates[:10], y=temps[:10], marker='o', color='blue')
    plt.xticks(rotation=45)
    plt.title(f"Temperature Forecast for {city}")
    plt.xlabel("Date-Time")
    plt.ylabel("Temperature (°C)")

    # ✅ Save each plot as PNG
    plt.tight_layout()
    plt.savefig(f"graphs/{city}_forecast.png")
    plt.close()

    print(f"✅ Graph saved: graphs/{city}_forecast.png")
    print(f"✅ JSON saved: {city}_forecast.json")

print("\n🎉 All cities processed successfully.")
