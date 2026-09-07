class DatabaseConnection:
    def __enter__(self):
        print("Database connected")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Database disconnected")

        print("Exception type:", exc_type)
        print("Exception value:", exc_value)
        print("Traceback:", traceback)


# exc_type   → What exception?
# exc_value  → What message/details?
# traceback  → Where/how did execution reach the exception?


print("---- No Exception ----")

with DatabaseConnection() as db:
    print("Running query")

print("\n---- With Exception ----")

try:
    with DatabaseConnection() as db:
        print("Running query")
        raise ValueError("Database query failed")
except ValueError:
    print("Exception handled outside")

# Output:
# ---- No Exception ----
# Database connected
# Running query
# Database disconnected
# Exception type: None
# Exception value: None
# Traceback: None

# ---- With Exception ----
# Database connected
# Running query
# Database disconnected
# Exception type: <class 'ValueError'>
# Exception value: Database query failed
# Traceback: <traceback object at 0x107ad2cc0>
# Exception handled outside
