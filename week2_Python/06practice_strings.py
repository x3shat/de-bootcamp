# Parse the CSV line " Priya , Bengaluru , 75000 " into a clean dict (strip every part, int the salary).

# s= " Priya , Bengaluru , 75000 "
# parts=s.split(",")

# result={
#     "name":parts[0].strip(),
#     "city":parts[1].strip(),
#     "salary":int(parts[2].strip())
# }

# print(result)


# One comprehension: from [12, 7, 99, 4, 50, 31] keep values > 20, doubled.
# nums=[12, 7, 99, 4, 50, 31]
# result= [n*2 for n in nums if n >20]
# print(result)


# From sal above, build a dict of only those earning ≥ 60000, values converted to LPA.
# sal = {"Amit": 60000, "Priya": 75000, "Rahul": 55000}
# rich={n:s/100000  for n,s in sal.items() if s>=60000}
# print(rich)


# Days between '2026-01-05' and '2026-04-15'?
# from datetime import datetime
# d1=datetime.strptime("2026-01-05","%Y-%m-%d")
# d2=datetime.strptime("2026-04-15","%Y-%m-%d")
# print((d2-d1).days)


# Sort [('Pen',20),('Bag',900),('Book',150)] cheapest first and print "Pen costs Rs 20" style lines.
items=[('Pen',20),('Bag',900),('Book',150)] 
items.sort(key=lambda x :x[1])
for name, price in items:
    print(f"{name} costs Rs {price}")