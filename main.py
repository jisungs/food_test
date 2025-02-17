import requests
from decouple import config

API_KEY = config('API_KEY')


url = 'http://apis.data.go.kr/6260000/FoodService/getFoodKr'
params ={'serviceKey' : API_KEY, 'pageNo' : '1', 'numOfRows' : '10', 'resultType' : 'json', 'UC_SEQ' : '' }

response = requests.get(url, params=params)

print(response.content)