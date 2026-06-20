from datetime import datetime


# Decorator used to add reusable debugging/logging output around another function.
def log_activity(func):

    # Wrapper receives any arguments meant for the original function.
    def wrapper(*args, **kwargs):
        print("===================================")
        print(f"Function: {func.__name__}")
        print(f"Time: {datetime.now()}")
        print("Activity started...")

        # Run the original decorated function and keep its return value.
        result = func(*args, **kwargs)

        print("Activity completed.")
        print("===================================\n")

        # Return the original function's result so the decorator does not change behavior.
        return result

    # Replace the original function with the wrapper when @log_activity is applied.
    return wrapper
