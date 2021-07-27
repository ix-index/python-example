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
url = 'https://api.ix-index.com/v1/index/ixci'
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
print(data['value'])
```

## Complete Example

```
import requests

url = 'https://api.ix-index.com/v1/index/ixci'
token = '<your api token>'
headers = {
  'Authorization': 'Bearer '+token
}

response = requests.request("GET", url, headers=headers)
data = response.json()
index_value = data['data']['value']
print(index_value)
```
