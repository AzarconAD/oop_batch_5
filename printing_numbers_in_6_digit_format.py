#ask user to input number
num = int(input("Enter a number from 0 to 1000: "))

#create conditions (only 0 to 1000)
if 0 <= num <= 1000:
    print(f"{num:06d}") #display output
else:
    print("Invalid input!")