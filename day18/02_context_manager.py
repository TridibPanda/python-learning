class DemoContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")


with DemoContext() as context:
    print("Inside context")

# Output:
# Entering context
# Inside context
# Exiting context
