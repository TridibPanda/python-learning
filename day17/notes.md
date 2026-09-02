# Python Advanced Question & Answer

### Q1. what a generator is in Python?
A generator is a special type of function that uses yield to produce values one at a time. Each yield pauses the function and preserves its state, and the function resumes from where it paused when next() is called again.
```text
Generator function
    ↓ call function
Generator object
    ↓
Iterator + Iterable
    ↓ next()
Value
    ↓
PAUSE
    ↓ next()
Value
```

### Q2. What is the biggest practical difference between return and yield?
return returns a final result and terminates the function, whereas yield produces a value, pauses the function, preserves its state, and allows execution to resume later.
```text
return
→ value
→ function ends

yield
→ value
→ pause
→ preserve state
→ next()
→ resume
```

### Q3. Why use a generator instead of returning a list?
Generators produce values lazily, one at a time, instead of creating and storing the entire collection in memory at once. They are useful when working with large or potentially unbounded sequences.

### Q4. What does "generator state" mean?
Generator state is the execution state preserved by a generator between next() calls, including its local variables and the point where execution was paused.

### Q5. Explain why a generator is called lazy.
A generator is called lazy because it doesn't produce all values immediately. It produces each value only when requested, such as through next() or a for loop, and therefore avoids unnecessary computation and memory usage.

### Q6. Why is this (x * 2 for x in range(5)) one called a generator expression?
It is called a generator expression because it uses comprehension-like syntax to create a generator object instead of a list.

### Q7. Difference Between List comprehension and Generator expression
| Feature | List comprehension | Generator expression |
| --- | --- | --- |
| Syntax | `[expression for item in iterable]` | `(expression for item in iterable)` |
| Result | A `list` object | A `generator` object |
| Evaluation | Immediate | Lazy, when values are requested |
| Memory usage | Stores all values in memory | Produces one value at a time |
| Reusable | Yes, the list can be iterated multiple times | Usually exhausted after one complete iteration |
| Best for | Small or reusable collections | Large data or memory-efficient iteration |

``` python
# List comprehension
[x * 2 for x in range(5)]
# Generator expression
(x * 2 for x in range(5))
```

### Q8. What is the difference between a generator function and a generator expression?
A generator function is a function defined using yield that produces a generator object when called. A generator expression is a concise expression using parentheses that directly creates a generator object. Both produce values lazily and maintain iteration state.

### Q9. Can a generator be iterated over again from the beginning after it is exhausted?
No, once a generator is exhausted, it cannot be restarted or iterated over again from the beginning. To iterate again, you need to create a new generator object by calling the generator function or expression again.

### Q10. Can we use a generator to create an infinite sequence?
Yes, we can use a generator to create an infinite sequence by using a loop that never terminates, yielding values indefinitely. However, care must be taken to avoid infinite loops in the consuming code.

### Q11. Explain the relationship between iterators and generators.
Generators are a type of iterator. They implement the iterator protocol, which includes the __iter__() and __next__() methods. Generators produce values lazily, one at a time, and maintain their state between calls to next(). All generators are iterators, but not all iterators are generators.