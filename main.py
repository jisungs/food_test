import requests
import csv
from decouple import config

API_KEY = config('API_KEY')


url = 'http://apis.data.go.kr/6260000/FoodService/getFoodKr'
params = {'serviceKey': API_KEY, 'pageNo': '1', 'numOfRows': '400', 'resultType': 'json'}

response = requests.get(url, params=params)

data = response.json()

items = data['getFoodKr']['item']
print(items)

with open('/Users/jisungs/Documents/dev/sideprojects/food_test/food_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = items[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for item in items:
        writer.writerow(item)

# if response.status_code == 200:

#     print(response.content)
# else:
#     print(f"Error {response.status_code}: {response.content}")


# url = 'http://apis.data.go.kr/6260000/BusanTblFnrstrnStusService/getTblFnrstrnStusInfo'
# params ={'serviceKey' : API_KEY, 'pageNo' : '1', 'numOfRows' : '10', 'bsnsNm' : '', 'resultType' : 'json' }

# response = requests.get(url, params=params)
# print(response.text)
