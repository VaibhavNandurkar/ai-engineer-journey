                                                #First get request
import requests

url = "https://restcountries.com/v3.1/name/india"

response = requests.get(url)
print("Status:", response.status_code)
print("Content-Type:", response.headers["Content-Type"])

data = response.json()
print("Country:", data[0]["name"]["common"])

                                                #Error handling for request

import requests

def fetch_country(name):
    url = f"https://restcountries.com/v3.1/name/{name}"
    try:
        response = requests.get(url, timeout =5)
        if response.status_code != 200:
            raise ValueError(
                 f"Country not found: {name}"
            )
        return response.json()[0]
    except requests.exceptions.ConnectionError:
        print("No internet connection.")
        return None
    except requests.exceptions.Timeout:
        print("Request timed out after 5 seconds.")
        return None
    except ValueError as e:
        print(e)
        return None
    
print(fetch_country("japan"))
print(fetch_country("xyzabc"))

                                                #Country Info explorer

import requests
import json

def country_info_explorer(country_name):
    url = f"https://restcountries.com/v3.1/name/{"germany"}"
    try:
        resopnse = requests.get(url, timeout = 5)
        if response.status_code != 200:
            raise ValueError(
                f"Country not found: {country_name}"
            )
        
        data = response.json()[0]
        currencies = ",".join(
            v["name"] for v in data["currencies"].values()
        )

        result = {
            "name":        data["name"]["common"],
            "capital":     data["capital"][0],
            "population":  data["population"],
            "region":      data["region"],
            "currencies":  currencies
        }

        filename = f"{country_name}_info.json"
        with open(filename, 'w') as f:
            json.dump(result,f ,indent = 2)

        print(f"\n🌍 {result['name']}")
        print(f"   Capital:       {result['capital']}")    
        print(f"   Population:    {result['population']} ")
        print(f"   Region:        {result['region']}")
        print(f"   Currencies:    {result['currencies']}")
        print(f"   Saved →        {filename}")

    except requests.exceptions.ConnectionError:    
        print("Error: No internet connection.")
    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
    except ValueError as e:
        print(f"Error: {e}")

country_info_explorer("india")

country_info_explorer("abcxyz")