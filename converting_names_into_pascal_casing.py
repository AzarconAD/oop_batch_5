#ask user for full name in incorrect casing
full_name = str(input("Enter your full name in incorrect casing: ")).lower() #convert casing into lowercase

#convert 1st letter of each word to caps by using title()
proper_full_name = full_name.title() 

#take out spaces
PascalCased = proper_full_name.replace(" ", "")

#display 
print(PascalCased)