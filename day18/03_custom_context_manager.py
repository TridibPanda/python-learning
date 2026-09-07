class DatabaseConnection:
    def __enter__(self):
        print("Database connected")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Database disconnected")


with DatabaseConnection() as db:
    print("Running database query")

# Output:
# Database connected
# Running database query
# Database disconnected
