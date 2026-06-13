# Q >>>>>>> Write 5 city names to a file, one per line. Read it back; print only cities starting with 'K'.

# with open("cities.txt","w") as f:
#     f.write("Kolkata\nDelhi\nMumbai\nPune\nGurgaon\nKodaikanal")

# with open("cities.txt","r") as f:
#     for line in f :
#         if line.startswith("K"):
#             print(line.strip()) 

# Q >>>>>>> Create a CSV of 4 products (name, price). Read it; print products costing over 100.
# import csv
# rows = [
#     ["name", "price"],  # Row 1: Header
#     ["milk", 2.50],     # Row 2
#     ["bread", 1.80],    # Row 3
#     ["eggs", 3.20],     # Row 4
#     ["apples", 4.00]    # Row 5
# ]
# with open ("products.csv","w",newline="") as f:
#     csv.writer(f).writerows(rows)

# with open ("products.csv") as f:
#     for row in csv.DictReader(f):
#         if float(row["price"]) >3.00 :
#             print(row["name"],row["price"])

# # Q >>>>>>> Read emp.csv and print the total of all products.
# import csv
# with open("products.csv") as f :
#     total=0.0
#     for row in csv.DictReader(f):
#         total+=float(row["price"])
#     print(f"The total of all salaries is ${total}")

# # Q >>>>>>> Mini-pipeline: read emp.csv, add a 10% hike column, write products_hiked.csv.
# import csv
# new_rows=[["name","price","hiked_price"]]
# with open("products.csv","r") as f :
#     for row in csv.DictReader(f):
#         hiked_price=round(float(row["price"]) * 1.1,2)
#         new_rows.append([row["name"] ,row["price"],hiked_price])

# with open ("products_hiked.csv","w",newline="") as f:
#     csv.writer(f).writerows(new_rows)

# print("Pipeline complete! New file created.")
