import requests

api_key = 'yDxqGkvLDzB%2BDh5x5ai%2FyXDJbTEbRO8v3HQVC1lTGbXGAK%2BvHL%2BDRMxpETjBicOH8Jjk5mPTfKYnSeAuK%2Btwcw%3D%3D'

API_KEY = 'yDxqGkvLDzB+Dh5x5ai/yXDJbTEbRO8v3HQVC1lTGbXGAK+vHL+DRMxpETjBicOH8Jjk5mPTfKYnSeAuK+twcw=='



url = 'http://apis.data.go.kr/6260000/FoodService/getFoodKr'
params ={'serviceKey' : API_KEY, 'pageNo' : '1', 'numOfRows' : '10', 'resultType' : 'json', 'UC_SEQ' : '' }

response = requests.get(url, params=params)

print(response.content)