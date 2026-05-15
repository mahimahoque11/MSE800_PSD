## Findings

The decorator is working as a logging/debugging helper. It avoids repeating the same print statements inside every user activity function. The project demonstrates a good basic use of decorators because the login, assignment submission, and grade viewing functions can focus on their own tasks while `log_activity` handles shared debugging output.

No functional bug was found in the decorator flow. But, Mohammad logs in and submits the assignment, but then Alex views grades. That is not a decorator bug, but it is a logic/debugging issue in the test data.