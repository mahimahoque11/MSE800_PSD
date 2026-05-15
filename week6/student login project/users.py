from decorators import log_activity


# @log_activity adds timestamped debugging output whenever a student logs in.
@log_activity
def student_login(username):
    print(f"{username} logged into the system.")


# @log_activity records when a student submits an assignment and when the action finishes.
@log_activity
def submit_assignment(username, assignment):
    print(f"{username} submitted {assignment}.")


# @log_activity records the grade-viewing activity without repeating logging code here.
@log_activity
def view_grades(username):
    print(f"{username} is viewing grades.")
