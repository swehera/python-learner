student = {
    "name": "Lutfor Rahman Hira",
    "age": 25,
    "id": "25205118",
    "department": "CSE",
    # nested dictionary 
    "subject": {
        "c++": 85,
        "python": 90,
        "java": 99,
        "JavaScript": 89
    },
    "passed": True,
    "result": 98.99
}

print(student["name"])
student["name"] = "Hira"
print(student["name"])

print("-------nested dictionary------")
print(student["subject"])
print(student["subject"]["c++"])
print(student["subject"]["java"])

print("-------dictionary methods------")
print(student.keys()) # show all the keys in dictionary
print(student.values()) # return all the values in dictionary
student.update({"city": "Dhaka", "name": "Lutfa"}) # update and add new key value in old dictionary
print(student)

