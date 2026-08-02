# This function demonstrates the use of the finally block in Python. It attempts to open a file and perform some operations. If an exception occurs, it catches the exception and prints an error message. Regardless of whether an exception occurs or not, the finally block is executed, ensuring that resources are properly closed.
def finally_example():
    try:
        print("Opening file")

    except ValueError:
        print("Something went wrong")
    finally:
        print("Closing resources")


finally_example()
# Output: Opening file
# Output: Closing resources
