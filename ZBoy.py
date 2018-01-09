# != means 'is not equal to'
# == is used when comparing two values
# = is used when assigning a value to a variable
'''
print("Welcome to Gmail!")
myUsername = input("Enter your username and then press return.")

if myUsername == "johndoe":
    print("Username successful")
else:
    print("Username incorrect")

'''          

print("Welcome to Gmail!")
myUsername =input("Enter your username, then press Return: ")

if myUsername == "johndoe":
    print("Username successful")
    myPassword = input("Enter your password, then press Return: ")
    if myPassword == "sof123@":
        print("Success")
    else:
        print("Unable to log in. Incorrect password")
else:
    print("Incorrect. Try again.")
    
