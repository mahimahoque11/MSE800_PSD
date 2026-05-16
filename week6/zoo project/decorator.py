# This decorator checks if the user is admin

def admin_only(function):

    def check_admin(username):

        if username == "admin":
            function(username)

        else:
            print("Access Denied")

    return check_admin