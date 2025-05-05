import gspread
from google.oauth2.service_account import Credentials
import random
import time
from datetime import datetime

def get_dht11_data():
    # DHT11 realistic range
    temperature = round(random.uniform(20.0, 35.0), 1)
    humidity = round(random.uniform(30.0, 90.0), 1)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return timestamp, temperature, humidity

# Simulate reading every 5 seconds
if __name__ == "__main__":
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_file("./iot-data-logger-455504-88f91b725dd3.json", scopes=scope)
    client = gspread.authorize(creds)

    SHEET_ID = "1j5oDTNN7iMdsdLtNBjN8UH1e3-RfuOYtdNWHexgdKNI"
    sheet = client.open_by_key(SHEET_ID).sheet1
    print("✅ Google Sheets access confirmed!")

    while True:
        ts, temp, hum = get_dht11_data()
        print(f"[{ts}] 🌡 Temp: {temp}°C | 💧 Humidity: {hum}%")
        sheet.append_row([ts, temp, hum])
        time.sleep(5)

