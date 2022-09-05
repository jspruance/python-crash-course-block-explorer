employee = {
    "name": "Bob",
    "dob": "2/3/1965",
    "skills": ["html", "css", "Javascript"]
}

employee["isManager"] = True

for key, value in employee.items():
    print(f"Key: {key}, Value: {value}")