# import required modules.
import requests
import json


# A get request
def Get_example():
    response_API = requests.get("https://api.covid19india.org/state_district_wise.json") # Establishing a connection to the API

    print(response_API.status_code) # Printing the status code. A status code is the indication whether the "request" was successful or not
    data = response_API.text # Convert the response into readable text ouput
    parse_json = json.loads(data) #Parse the data
    active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active'] # Get specified data. This is basically like a directory.
    print("Active cases in South Andaman:", active_case) # Print the output

Get_example()
