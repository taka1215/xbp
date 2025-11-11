# weather_app.py
# 天気予報アプリ（Python × OpenWeatherMap API）

import requests


API_KEY = "a637e60beb6a39de5431225e026949fa"

# ======================================================

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    """指定した都市の天気情報を取得して表示"""
    params = {
        "q": city_name,
        "appid": API_KEY,
        "lang": "ja",       # 日本語で出力
        "units": "metric"   # 摂氏（℃）で表示
    }

    response = requests.get(BASE_URL, params=params)

    # ステータスコード200なら成功
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]

        print(f"\n🌤 {city_name}の現在の天気情報")
        print("------------------------------")
        print(f"天気：{weather}")
        print(f"気温：{temp}℃")
        print("------------------------------\n")

    else:
        print("❌ 都市名が見つかりませんでした。")


if __name__ == "__main__":
    print("=== 天気予報アプリ (OpenWeatherMap API) ===")
    city = input("甲府市 ")
    get_weather(city)