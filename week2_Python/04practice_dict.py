# profiles = [
#     {"name":"Pavan" , "city" : "Patna", "skills":"canva,designing"},
#     {"name":"Rev" , "city" : "Indore", "skills":"python,c++"},
#     {"name":"Kidhar" , "city" : "jaipur", "skills":"pythpn,sql"},
# ]
# print(profiles[0]["skills"].split(",")[1]); # print desigining



# employees = [
#     {"name": "Amit",  "city": "Kolkata",   "salary": 60000},
#     {"name": "Priya", "city": "Bengaluru", "salary": 75000},
#     {"name": "Rahul", "city": "Kolkata",   "salary": 55000},
# ]
# # print the name of the highest paid employee
# big_salary=0
# top_name = ""
# for e in employees :
#     if e["salary"] >big_salary:
#         big_salary =e["salary"]
#         top_name=e["name"]
# print (top_name)


# employees = [
#     {"name": "Amit",  "city": "Kolkata",   "salary": 60000},
#     {"name": "Priya", "city": "Bengaluru", "salary": 75000},
#     {"name": "Rahul", "city": "Kolkata",   "salary": 55000},
# ]
# freq={}
# for e in employees :
#     city=e["city"]                     #1. Grab the city name 
#     freq[city] =freq.get(city,0)+1     #2. Count it safely
# print (freq)

words="to be or not to be".split()
freq={}
for w in words :
    freq[w]= freq.get(w,0)+1
print(freq) 
print(max(freq)) # wrong : gives alphabatically highest value . 
print(max(freq ,key=freq.get))#Adding key=freq.get forces Python to look at the values