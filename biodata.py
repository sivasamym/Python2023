#This python code captures your information and stores in a file with biodata format.
import re
biodata = {}
biodata['fname'] = input("Enter your first name: ").strip()
biodata['lname'] = input("Enter your last name: ").strip()
biodata['age'] = input("Enter your age: ").strip()
biodata['gender'] = input("Enter your gender: ").strip()
biodata['education'] = input("Enter your education: ").strip()
biodata['experience'] = input("Enter your experience in years : ").strip()
biodata['specilization'] = input("Specialized in : ").strip()
biodata['address'] = input("Enter your address: ").strip()
#biodata['phone'] =
while True:
    phone = input("Enter your Mobile Phone Number: ").strip()
    if re.match(r"^\d{3}-\d{3}-\d{4}$", phone):
        biodata['phone'] = phone
        break
    else:
        print("Invalid phone number in XXX-XXX-XXXX format and try again")

while True:
    email = input("Enter your email: ").strip()
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        biodata['email'] = email
        break
    else:
        print("Invalid email format try again")

fieldmap = {}
fieldmap['fname'] = "First Name:"
fieldmap['lname'] = "Last Name:"
fieldmap['age'] = "Age:"
fieldmap['gender'] = "Gender:"
fieldmap['education'] = "Highest Education:"
fieldmap['experience'] =  "Years of Experience:"
fieldmap['specilization'] = "Specilization:"
fieldmap['address'] = "Address:"
fieldmap['email'] = "Email:"
fieldmap['phone'] = "Mobile Number:"


# Write biodata to a file
i = 0
filename = "biodata.txt"
with open(filename, 'w') as file:
    file.write("                   Bio Data                             \n")
    for key, value in biodata.items():
        fieldcode = key
        if fieldcode in fieldmap:
            fieldname = fieldmap[fieldcode]
        file.write(f"{fieldname}{value}             ")
        i = i+1
        if (i % 2) == 0:
            file.write(f"\n")

print(f"Biodata has been saved to {filename}")
