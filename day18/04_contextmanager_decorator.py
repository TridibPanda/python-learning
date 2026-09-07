from contextlib import contextmanager


@contextmanager
def database_connection():
    print("Database connected")

    try:
        yield
        # Why is yield used instead of return here?
        # return terminates; yield pauses and resumes.
    finally:
        print("Database disconnected")


with database_connection():
    print("Running database query")

# Output:
# Database connected
# Running database query
# Database disconnected
