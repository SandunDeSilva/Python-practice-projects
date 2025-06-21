import requests
from win10toast import ToastNotifier
import json
import time

def update():
    # Send a GET request to the COVID-19 API to get global data
    request = requests.get("https://disease.sh/v3/covid-19/all")

    # Parse the response into JSON format (a Python dictionary)
    data = request.json()

    # Create a text string with confirmed cases, deaths, and recovered numbers
    text = f'Confirmed Cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'

    # Start an infinite loop to repeatedly show the notification
    while True:
        try:
            # Create an instance of the ToastNotifier class to show notifications
            toast = ToastNotifier()

            # Show a toast notification with the COVID-19 update and a duration of 20 seconds
            toast.show_toast("COVID-19 Update", text, duration=20) 

        except Exception as e:
            print(f"Error fetching data: {e}")

        # Wait for 60 seconds before showing the next notification
        time.sleep(60)


update()