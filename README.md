## Prerequisites

Before your program connects to the API, you should install the `requests` library.

To install `requests`, type in the below command in your terminal.

```
pip install requests
```

Now you are ready to start using Python to interact with the API, make sure you import the `requests` library into the script.

```
import requests
```

## Authentication

To authenticate, we have to add our API token into the header, so the server knows who we are.

```
url = 'https://api.ix-index.com/v1/real-time/ixci'
token = '<your api token>'
headers = {
  'Authorization': 'Bearer '+token
}

response = requests.request("GET", url, headers=headers)
```

## Result from the API
All the results from the API are in JSON format. So we have to decode it.
```
data = response.json()
print(data['data']['value'])
```

## Fetching Data with 15 seconds interval
The IX Index series updates their data every 15 seconds. To fetch the data from the API with 15 seconds interval, you can use the code below.
```
import time

...

while True:
	response = requests.request("GET", url, headers=headers)
	data = response.json()
	index_value = data['data']['value']
	print(index_value)
	timestamp = int(time.time())
	time.sleep((15 - timestamp % 15))
```

## Complete Example

```
import requests
import time

url = 'https://api.ix-index.com/v1/real-time/ixci'
token = '<your api token>'
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
```
