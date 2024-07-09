# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")
        
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students, key = get_name, reverse=True):
#     print(f"{student['name']} is in {student['house']}")

import csv

# students = []


# # with open("students.csv") as file:
#     # for line in file:
#     #     name, house = line.rstrip().split(",")
#     #     student = {"name": name, "house": house}
#     #     students.append(student)

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# for student in sorted(students, key = lambda student: student["name"], reverse=True):
#     print(f"{student['name']} is in {student['home']}")

name = input("Name: ")
home = input("Home: ")

with open("students.csv", "a",newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home}) # or just use (row) in this case