students = [
    {
        "name": "John",
        "address": "usa",
        "subject": "CSE"
    },
    {
        "name": "ruhul",
        "address": "bd",
        "subject": "Math"
    },
    {
        "name": "Ahmad",
        "address": "bd",
        "subject": "CSE"
    },
    {
        "name": "Rahim",
        "address": "ind",
        "subject": "law"
    },
    {
        "name": "Reza",
        "address": "bd",
        "subject": "Math"
    },

]

# houses = []
# for student in students:
#     if student["address"] not in houses:
#         houses.append(student["address"])

houses = set()
for student in students:
    houses.add(student["address"])

for house in sorted(houses):
    print(house)
