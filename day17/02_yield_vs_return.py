def with_return():
    return [1, 2, 3]


def with_yield():
    yield 1
    yield 2
    yield 3


return_result = with_return()
yield_result = with_yield()

print(return_result)  # Output: [1, 2, 3]
print(yield_result)  # Output: <generator object with_yield at 0x104dc8f60>

print(type(return_result))  # Output: <class 'list'>
print(type(yield_result))  # Output: <class 'generator'>

print(next(yield_result))  # Output: 1
print(next(yield_result))  # Output: 2
print(next(yield_result))  # Output: 3
# return returns a final result and terminates the function, whereas yield produces a value, pauses the function, preserves its state, and allows execution to resume later.