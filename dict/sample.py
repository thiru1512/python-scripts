student_list    =   {
    "Name"  : "Thirumal",
    "age": "30",
    "city": "Pondicherry"
    }

student_list["country"] = "India"
student_list["age"] = 35

print(student_list)
print(student_list["Name"])

for i,y in student_list.items():
    print(i,y)

