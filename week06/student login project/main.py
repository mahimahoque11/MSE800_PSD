from users import (
    student_login,
    submit_assignment,
    view_grades
)


# Main driver used to test each decorated student activity.
def main():

    # Calls student_login through the log_activity wrapper.
    student_login("Mohammad")

    # Calls submit_assignment through the log_activity wrapper with two arguments.
    submit_assignment(
        "Mohammad",
        "Python Decorator Project"
    )

    # Calls view_grades through the log_activity wrapper but the return is for Alex not Mohammad.
    view_grades("Alex")


# Only run the debugging demo when this file is executed directly.
if __name__ == "__main__":
    main()
