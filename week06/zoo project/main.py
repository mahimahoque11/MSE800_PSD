from users import username, password
from decorator import admin_only


# Admin dashboard
@admin_only
def zoo_dashboard(user):

    print("\nWelcome to the Zoo Dashboard")
    print("You can manage animals here.")


print("=== Zoo Login System ===")

# User input
input_username = input("Enter username: ")
input_password = input("Enter password: ")


# Login check
if input_username == username and input_password == password:

    print("Login Successful")

    zoo_dashboard(input_username)

else:

    print("Wrong username or password")