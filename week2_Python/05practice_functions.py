# raw = [
#     {"name": "Amit ", "city": "kolkata", "salary": 60000},  # Good
#     {"name": "Priya", "city": "Bengaluru", "salary": 0},    # Bad (salary 0)
#     {"name": "ern", "city": "kolkata", "salary": 50000}          # Bad (empty name)
# ]

#1. Write is_valid(row) returning True if salary > 0 and name isn't empty.
# Test on both a good and bad dict.

#function to check if its valid
# def is_valid(row):
#     if row["salary"] >0 and row["name"].strip() !="" :
#         return True
#     else:
#         return False

# #test    
# for r in raw:
#     result =is_valid(r)
#     print(f"Name: {r['name']} | Valid ? {result} ")

#----------------------------------------------------------------

#2.Write apply_hike(salary, pct=10) returning the raised salary.
# Test with default and pct=20.
# def apply_hike(salary, pct=10):
#     return int(salary +(salary * (pct/100)))


# # Test 1: Using the default 10%
# print(apply_hike(60000))           # Output: 66000.0

# # Test 2: Overriding the default to use 20%
# print(apply_hike(60000, pct=20))   # Output: 72000.0

# for r in raw:
#     r['salary']=apply_hike(r['salary'],pct=20)

# for r in raw:
#     print(r)

#----------------------------------------------------------------

# 3 Write total_by_city(employees, city) returning the 
# sum of salaries for that city (reuse Lesson 2.4 data).


def total_by_city(employees, city):
    total=0
    for e in employees:
        if e["city"].lower() ==city.lower():
            total+=e["salary"]
    return total

employees = [
    {"name": "Amit",  "city": "Kolkata",   "salary": 60000},
    {"name": "Priya", "city": "Bengaluru", "salary": 75000},
    {"name": "Rahul", "city": "Kolkata",   "salary": 55000},
]

print(total_by_city(employees,'Kolkata'))

#-----------------------------------------------------
# Combine: loop over raw above, clean each row, keep only valid ones, print
#  the result.


raw = [{"name": " amit ", "city": "kolkata ", "salary": "60000"},
       {"name": "PRIYA",  "city": " bengaluru", "salary": "75000"}]

def clean_row(row):
    return {
        "name" :row["name"].strip().title(),
        "city" :row["city"].strip().title(),
        "salary":int(row["salary"]),
    }
clean=[]
for r in raw:
    clean.append(clean_row(r))
print(clean[0]) 