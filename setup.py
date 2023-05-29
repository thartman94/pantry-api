import requests
import json

food = [
    {
        "name": "Small Red Beans",
        "brand": "Goya",
        "size": 454,
        "serving_size": 45,
        "calories": 160,
        "fat": 1,
        "protien": 8,
        "carbs": 29,
        "exp_date": "2024-12-29",
    },
    {
        "name": "Small Red Beans",
        "brand": "Goya",
        "size": 454,
        "serving_size": 45,
        "calories": 160,
        "fat": 1,
        "protien": 8,
        "carbs": 29,
        "exp_date": "2024-12-29",
    },
    {
        "name": "Emergency Food Ration",
        "brand": "SOS Food Lab",
        "size": 756,
        "serving_size": 84,
        "calories": 410,
        "fat": 18,
        "protien": 6,
        "carbs": 53,
        "exp_date": "2026-01-01",
    },
    {
        "name": "Orange Drink Mix",
        "brand": "Tang",
        "size": 566,
        "serving_size": 38,
        "calories": 140,
        "fat": 0,
        "protien": 0,
        "carbs": 37,
        "exp_date": "2022-03-08",
    },
    {
        "name": "Beef Stew",
        "brand": "Dinty Moore",
        "size": 1007,
        "serving_size": 236,
        "calories": 200,
        "fat": 10,
        "protien": 10,
        "carbs": 17,
        "exp_date": "2024-09-01",
    },
]


reqUrl = "http://127.0.0.1:5000/food/"

headersList = {"Accept": "*/*", "Content-Type": "application/json"}

payload = json.dumps(food)
response = requests.request("POST", reqUrl, data=payload, headers=headersList)
print(response.text)
