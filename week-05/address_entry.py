# Contact information
contact_info = {
    "name": "Lulia Aman",
    "address": "123 Main Street",
    "city": "Charlotte",
    "state": "NC",
    "zip": "28213"
}

# Print mailing address
print(f"{contact_info['name']}\n{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")

# Remove the name
contact_info:("name")

# Create full name dictionary
full_name = {
    "first name": "Lulia",
    "last name": "Aman"
}

# Add honorific
full_name.update({"honorific": "Ms."})

# Add full_name to contact_info
contact_info.update({"full_name": full_name})

# Print updated address
print(f"\n{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}")
print(f"{contact_info['address']}")
print(f"{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")


      

