#store
print("Enter your name with leading spaces.")
first_name = str(input("First Name: ")).strip()
surname = str(input("Surname: "))

#function
def whole_name():
    print(f"{first_name} {surname}")
    
#output
whole_name()