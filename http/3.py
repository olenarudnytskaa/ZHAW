from os import times_result

import numpy as np
import pandas
import pandas as pd
import json
import requests
import time
import os
import matplotlib.pyplot as plt

from gitdb.util import close

api_url = "https://api.open-meteo.com/v1/forecast?latitude=47.37&longitude=8.54&hourly=temperature_2m"


class WeatherDownloader():
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    def process_data(self):
        try:
            # Wir prüfen: Gibt es die Datei, und ist sie jünger als 10 Minuten (600 Sekunden)?
            if os.path.exists(self.filename) and (time.time() - os.stat(self.filename).st_mtime < 600):
                print("--- Data sind aus Cache ---")
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return data

            # Wenn die Datei nicht vorhanden ist ODER veraltet ist, laden wir sie aus dem Internet herunter
            else:
                print("--- Data sind aus Netz ---")
                response = requests.get(self.url)
                data = response.json()

                # Wir speichern die aktuellen Daten
                with open(self.filename, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)

                return data

        except Exception as e:
            print(f"Fehler im Downloader: {e}")
            return None


class WeatherApp():
    def __init__(self,url, filename):
        self.df = pd.DataFrame()
        self.loader = WeatherDownloader(url, filename)

    def load_data(self):

        json_data = self.loader.process_data()


        if json_data is not None:

            self.df = pd.DataFrame(json_data['hourly'])

            # Zeitumrechnung
            self.df['time'] = pd.to_datetime(self.df['time'])

            # check
            print("--- Die Tabelle wurde erstellt  ---")
            print("Spalten:", self.df.columns)
            print(self.df.head())
        else:
            print("Fehler: Keine Daten vom Downloader!")

    def calculate_statistics(self):
        # 1. Arithmetisches Mittel
        print("\n--- DEBAG: Was steht in der Tabelle? ---")
        print("Spalten:", self.df.columns.tolist())
        print("Erste Zeile der Daten:", self.df.iloc[0].to_dict() if not self.df.empty else "Die Tabelle ist leer!")
        avg_temp = round(self.df['temperature_2m'].mean(), 2)
        print(f"Mittelwert: {avg_temp} °C")

        # 2. Varianz
        var = round(self.df['temperature_2m'].var(), 2)
        print(f"Varianz: {var}")

        # 3. Schiefe
        skew = round(self.df['temperature_2m'].skew(), 2)
        print(f"Schiefe: {skew}")

        # 4. Wölbung
        kurt = round(self.df['temperature_2m'].kurt(), 2)
        print(f"Wölbung (Kurtosis): {kurt}")


    def process_data(self):
        try:


            if os.path.exists(filename) and (time.time() - os.stat(filename).st_mtime < 600):
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    print("Data sind aus Cache")
                    return data

            else:
                print("Data sind aus Netz")
                # Используем self.url, который сохранили в __init__
                response = requests.get(self.url)
                data = response.json()

                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)

                return data
        except Exception as e:
                print(f"Fehler: {e}")

    def visualize_data(self):
        print("")

        self.df['temperature_2m'].hist(bins=15, color='skyblue', edgecolor='black')


        plt.title("Temperaturverteilung (Zürich)")  # titel
        plt.xlabel("Temperatur (°C)")  # x Temperatur
        plt.ylabel("Häufigkeit (Stunden)")  #  Y (heufig/Stunden)


        plt.show()


if __name__ == "__main__":

    api_url = "https://api.open-meteo.com/v1/forecast?latitude=47.37&longitude=8.54&hourly=temperature_2m"
    cache_file = "weather_cache.json"


    app = WeatherApp(api_url, cache_file)


    print("--- Launch App ---")
    app.load_data()
    app.calculate_statistics()
    app.visualize_data()