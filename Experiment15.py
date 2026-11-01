#  Develop a Python program for an input validation system used in online registration 
# portals where the program validates user email addresses, detects valid phone numbers, 
# and extracts transaction IDs from logs using regular expressions. The system should 
# ensure proper data format validation for secure and clean data entry. 


import re

# Function to validate email address
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        print("Valid Email Address")
    else:
        print("Invalid Email Address")


# Function to validate phone number
def validate_phone(phone):
    pattern = r'^[6-9][0-9]{9}$'

    if re.match(pattern, phone):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")


# Function to extract transaction IDs from logs
def extract_transaction(log):
    pattern = r'TXN[0-9]+'

    ids = re.findall(pattern, log)

    print("Transaction IDs:", ids)


# Main program
email = input("Enter Email Address: ")
phone = input("Enter Phone Number: ")
log = input("Enter Log Message: ")

print("\n----- VALIDATION RESULTS -----")

validate_email(email)
validate_phone(phone)
extract_transaction(log)
