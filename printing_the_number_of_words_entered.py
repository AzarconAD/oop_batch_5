#ask user to input a statement
statement = str(input("Enter a statement: "))

#use split() method to break down statement into words
word_count = len(statement.split()) #using len() to count the words

#display number of words
print(word_count)