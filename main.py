
import requests
from OpenSSL import SSL



print("hello sam")
payload = {'limit': "1", "api_key": "0t24jH6Rn6s5XKRFQFDolcFRRZsk9D1YQlZoh5xG", "postedFrom": "01/01/2018", "postedTo": "05/10/2018"}

x = requests.get("https://api.sam.gov/prod/opportunities/v2/search?",params=payload)

print(x.text)