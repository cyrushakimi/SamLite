import urllib.request

print("hello sam")
contents = urllib.request.urlopen("https://api.sam.gov/prod/opportunities/v2/search?limit=1&api_key=0t24jH6Rn6s5XKRFQFDolcFRRZsk9D1YQlZoh5xG&postedFrom=01/01/2018&postedTo=05/10/2018&ptype=a&deptname=general").read()
print(contents)