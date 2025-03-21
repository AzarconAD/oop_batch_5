#ask for full name with incorrect casing
full_name = str(input("Enter you full name in incorrect casing: "))

#reverse the casing
reversed_casing = ""
for char in full_name:
    if char.islower():
        reversed_casing += char.upper()
    else:
        reversed_casing += char.lower()

#display
print(reversed_casing)
