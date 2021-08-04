import requests
import time

url = 'https://api.ix-index.com/v1/index/ixci'
token = '<your api token>';
headers = {
  'Authorization': 'Bearer '+token
}

while True:
	response = requests.request("GET", url, headers=headers)
	data = response.json()
	index_value = data['data']['value']
	print(index_value)
	timestamp = int(time.time())
	time.sleep((15 - timestamp % 15))