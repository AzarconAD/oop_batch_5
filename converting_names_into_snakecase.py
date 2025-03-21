#ask user for full name in incorrect casing
full_name = str(input("Enter your full name in incorrect casing: ")).lower() #convert casing into lowercase

#replace spaces with underscore character
snakecased = full_name.replace(" ", "_")

#display 
print(snakecased)