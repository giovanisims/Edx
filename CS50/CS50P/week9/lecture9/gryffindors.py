# students = [
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"}
# ]

# # List comprehension

# # gryffindors = [
# #     student["name"] for student in students if student["house"] == "Gryffindor"
# #     ]

# # for gryffindor in sorted(gryffindors):
# #     print(gryffindor)

###

# # Using filter

# # def is_gryffindor(s):
# #     return s["house"] == "Gryffindor"

# # gryffindors = filter(is_gryffindor, students)

# # for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
# #     print(gryffindor["name"])

###

students = ["Harry", "Ron", "Hermione"]

# Dictionary comprehension

# gryffindors = {student: "Gryffindor" for student in students}

# print(gryffindors)

###

# Using enumerate

# for i, student in enumerate(students, 1):
#     print(f"{i} {student}")
