# Python Advanced Question & Answer

### Q1. What is Iterable ?
An iterable is an object that can return an iterator through iter() and can therefore be iterated over.

### Q2. What is Iterator ?
An iterator is an object that produces values one at a time using next() and keeps track of its current iteration state. When there are no more values, it raises StopIteration.

```text
Difference:

Iterable
→ Can be iterated
→ iter(iterable) gives an iterator
→ Examples: list, tuple, string

Iterator
→ Produces values one at a time
→ next(iterator) gives next value
→ Maintains iteration state
→ Raises StopIteration when exhausted
```
```text
Iterable
   │
   │ iter()
   ↓
Iterator
   │
   │ next()
   ↓
value
   │
   │ next()
   ↓
value
   │
   │ next()
   ↓
value
   │
   │ next()
   ↓
StopIteration
```
### Q3. what is next() in Iterator?
next() produces the next available value from the iterator and advances/updates the iterator's internal iteration state.

### Q4. __iter __()
Returns an iterator. For an iterator object, __iter__() typically returns self.

### Q5. __next __()
Returns the next value and advances the iterator's state. When no values remain, it raises StopIteration.

### Q6. for loop internally
``` text
for item in iterable:
        ↓
iter(iterable)
        ↓
iterator
        ↓
next(iterator)
        ↓
next(iterator)
        ↓
...
        ↓
StopIteration
        ↓
loop ends
```
***
```text
Iterable = can provide an iterator

Iterator = produces the values + remembers where it is
```