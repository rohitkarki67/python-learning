"""
    ask the user for their age
    ask the user if they have a VIP pass (yes/no)
    if they don't have a VIP pass, then end the program with a message saying "Access denied. VIP pass required."
    
    if the user is under 13 :
        grant child access
    if the user is between 13 and 18:
        grant teen access
    if the user is older than 18 but younger than 60:
        grant adult access
    if the user is 60 or older:
        grant senior access
    display the appropriate access message

"""
print("Welcome to the Age Access System!")
vip_pass = input("Do you have a VIP pass? (yes/no): ")

if vip_pass == "yes":
    print("Now, let's check your age.")
    age = int(input("Please enter your age: "))
else:
    print("Access denied. VIP pass required.")
    exit()

if age < 13:
    print("Access granted. You have child access.")
elif age >= 13 and age <18:
    print("Access granted. You have teen access.")
elif age >= 18 and age < 60:
    print("Access granted. You have adult access.")
else:
    print("Access granted. You have senior access.")

print("Thank you for using the Age Access System!")