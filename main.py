import requests
import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.11.1')


class OilApp(App):
    def build(self):
        url = 'https://api.oilpriceapi.com/v1/prices/latest'
        headers = {
            'Authorization': 'Token b7ed054ba6e6d513af611db4e0b0e7f2',
            'Content-Type': 'application/json'
        }
        response = requests.get(url=url, headers=headers)
        data = response.json()
        return Label(text=f'current oil price: {str(data["data"]["formatted"])}')


if __name__ == '__main__':
    OilApp().run()
