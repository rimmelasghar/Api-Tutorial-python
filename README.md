# Pull Data from an API in Python

Hello, programmers! In this article, we will be focusing on How to Pull data from an API in Python.

## 🚀 Steps to pull data from an API using Python
Let us now focus on the steps that we need to follow in order to pull out the particular data from an API.

### Example 1: Pulling data from an Open source COVID API.

In this example, we would be connecting to an Open source COVID API just to extract and parse the json information in an customized manner.

 - 1. Connect to an API
    At first, we need to connect to an API and make a secure connection as shown below

```bash
import requests
import json
response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
print(response_API.status_code)
```
As we are pulling the data from an API, we have used the get() function to get the information from the API.

 - 2. Get the data from API
    After making a healthy connection with the API, the next task is to pull the data from the API. Look at the below code!

```bash
data = response_API.text
```

The requests.get(api_path).text helps us pull the data from the mentioned API.

 - 3. Parse the data into JSON format
    Having extracted the data, its now the time to convert and decode the data into proper JSON format as shown below.

```bash
json.loads(data)
```
The json.loads() function parses the data into a JSON format.

 - 4. Extract the data and print it
    The JSON format contains data into a key-value format which resembles a Python dict. Thus, we can pull out and print the data using the key values as shown.

```bash
parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
```

You can Find whole code in Api.py.

 - Api.py
```bash
import requests
import json
response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
print("Active cases in South Andaman:", active_case)
```
## Output:

```bash
Active cases in South Andaman: 19
```