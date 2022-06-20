# Implements a phone book

import sys

people = {
      "EMMA":"617-555-0100" ,
      "RODRIGO": "617-555-0101",
      "BRIAN": "617-555-0102",
      "DAVID": "617-555-0103"
}
phone = input("Plase, enter phone number:")
# Search for EMMA
if phone in people:
    print(f"Found {people.keys(phone)}")
    sys.exit(0)
print("Not found")
sys.exit(1)
