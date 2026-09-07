# Python Advanced Question & Answer

### Q1. What is a context manager in Python, and what problem does the with statement solve?
A context manager manages the setup and cleanup of a resource around a block of code. The with statement uses that context manager so cleanup happens automatically when the block exits, even if an exception occurs.

### Q2. Compare these two ways of creating a context manager: Class-based and Decorator-based
Class-based
```python
class DatabaseConnection:
    def __enter__(self): ...

    def __exit__(self, exc_type, exc_value, traceback): ...
```
```text
with DatabaseConnection() as context
        ↓
DatabaseConnection object created
        ↓
__enter__()
        ↓
return self
        ↓
context = returned self
        ↓
Inside context
        ↓
__exit__()
```
Decorator-based
``` python
@contextmanager
def database_connection():
    ...
    yield
    ...
```
``` text
@contextmanager
      ↓
generator function becomes context manager
      ↓
code before yield = enter/setup
      ↓
yield = give control to with block
      ↓
code after yield = exit/cleanup
      ↓
finally = cleanup guaranteed even on exception
```
Use it when the context manager has simple setup → use → cleanup logic.

### when would the @contextmanager approach be convenient?
It's especially convenient when you don't need a full class with state and multiple methods.
If the context manager has complex state/behavior, a class-based implementation can be clearer.

```text
Context Manager
      │
      ├── Setup
      │     ↓
      │  __enter__()
      │
      ├── Use resource
      │     ↓
      │  with block
      │
      └── Cleanup
            ↓
         __exit__()
            │
            ├── exc_type
            ├── exc_value
            └── traceback
```
And the two ways to create one:
```text
Class-based
→ __enter__()
→ __exit__()

Decorator-based
→ @contextmanager
→ yield
```