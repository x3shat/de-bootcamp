# Build a dict of yourself (name, city, 3 skills); save me.json; load it; print the 2nd skill.--------------
# import json
# me={"name" :"raj", "city":"kolkata", "3_skills": ["python","c++","sql"]}

# # Save to file
# with open("me.json", "w") as f :
#     json.dump(me,f,indent=2)

# # Load from file
# with open("me.json") as f:
#     data=json.load(f)

# print(data["3_skills"][1])

# Call open-meteo for Mumbai (lat 19.07, lon 72.87); print temperature; wrap in try/except so no-internet doesn't crash.-------------
# import requests
# import json

# try :
#     url = "https://api.open-meteo.com/v1/forecast"
#     params = {"latitude": 19.07, "longitude": 72.87, "current_weather": "true"}
#     resp = requests.get(url, params=params, timeout=10)

#     data=resp.json()
#     # print(json.dumps(data,indent=2))
#     print(data["current_weather"]["temperature"])
# except requests.exceptions.RequestException as  e:
#     print("Network error:", e) 


# From the string '[{"name":"A","age":25},{"name":"B","age":30}]' print each name.----------------------------
# import json

# text='[{"name":"A","age":25},{"name":"B","age":30}]'

# back=json.loads(text) #str > dict


# for d in back :
#     print(d["name"])

# From resp above: print ids of orders that have at least one item.--------------------
import json

# nested dict
resp = {
  "status": "ok",
  "data": {
    "orders": [
      {"id": 1, "amount": 5000, "items": [{"sku": "A1"}, {"sku": "B2"}]},
      {"id": 2, "amount": 3000, "items": []},
      {"id": 3, "amount": 3000, "items": [{"sku": "A1"}]}
    ]
  }
}


for order in resp["data"]["orders"]:
    if len(order["items"]) >=1 :
        print (order["id"])