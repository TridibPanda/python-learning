# Python Advanced Question & Answer

### Q1. What is asynchronous programming in Python?
Asynchronous programming in Python is a programming paradigm that allows for concurrent execution of tasks without blocking the main thread. It enables the program to handle multiple operations at the same time, making it more efficient, especially for I/O-bound tasks. In Python, asynchronous programming is primarily achieved using the `async` and `await` keywords, along with the `asyncio` library, which provides an event loop to manage asynchronous tasks.

### Q2. How does the `asyncio` library work in Python?
The `asyncio` library in Python provides a framework for writing asynchronous code using coroutines. It allows developers to define asynchronous functions using the `async def` syntax and to pause their execution with the `await` keyword when waiting for I/O operations or other asynchronous tasks to complete. The `asyncio` event loop manages the scheduling and execution of these coroutines, enabling efficient handling of multiple tasks concurrently. The library also provides various utilities for working with asynchronous tasks, such as `asyncio.gather`, `asyncio.sleep`, and `asyncio.create_task`.

### Q3. What are the benefits of using asynchronous programming in Python?
1. **Improved Performance**: Asynchronous programming allows for better utilization of system resources by enabling concurrent execution of tasks, which can lead to improved performance, especially in I/O-bound applications.    
2. **Non-blocking Operations**: Asynchronous programming allows for non-blocking operations, meaning that the program can continue executing other tasks while waiting for I/O operations to complete, resulting in a more responsive application.
3. **Scalability**: Asynchronous programming can handle a large number of concurrent connections or tasks, making it suitable for building scalable applications, such as web servers or real-time data processing systems.

### Q4. What does async def mean in Python?
The `async def` syntax in Python is used to define an asynchronous function. When a function is defined with `async def`, it becomes a coroutine, which can be paused and resumed during execution. This allows the function to perform asynchronous operations without blocking the main thread.

```python
import asyncio


async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)
    print("Data received")
    return "Hello from server"


async def main():
    print("Start")

    result = await fetch_data()

    print("Result:", result)
    print("End")


asyncio.run(main())
```
``` text
asyncio.run(main())
        ↓
main()
        ↓
print("Start")
        ↓
await fetch_data()
        ↓
"Fetching data..."
        ↓
await asyncio.sleep(2)
        ↓
coroutine pauses
        ↓
2 seconds
        ↓
"Data received"
        ↓
return "Hello from server"
        ↓
result receives value
        ↓
"Result: Hello from server"
        ↓
"End"
```

### Q5. What does await do in result = await fetch_data()?
The `await` keyword in Python is used to pause the execution of an asynchronous function until the result of an awaited coroutine is available. In the statement `result = await fetch_data()`, the program will wait for the `fetch_data()` coroutine to complete its execution and return a result. During this waiting period, other tasks can continue to run, allowing for efficient handling of multiple asynchronous operations. Once `fetch_data()` completes, its result will be assigned to the variable `result`.

### Q6. Why is asyncio.run(main()) required here instead of simply calling main()?
The `asyncio.run(main())` function is required to run the asynchronous `main()` coroutine because it sets up and manages the event loop needed for executing asynchronous code. When you call `main()` directly, it returns a coroutine object instead of executing it, and without an event loop, the coroutine cannot be run. The `asyncio.run()` function creates a new event loop, runs the specified coroutine until it completes, and then closes the loop, ensuring proper cleanup of resources. This is essential for running asynchronous code in a synchronous context, such as the main entry point of a Python program.

### Q7. What's the difference between time.sleep(2) and await asyncio.sleep(2) in an async application?
The difference between `time.sleep(2)` and `await asyncio.sleep(2)` in an asynchronous application lies in how they handle blocking and non-blocking behavior:
- `time.sleep(2)`: This function is a blocking call that pauses the execution of the entire program for 2 seconds. During this time, no other tasks can run, which can lead to inefficiencies in an asynchronous application, especially if there are other tasks that could be executed concurrently.
- `await asyncio.sleep(2)`: This function is a non-blocking call that pauses the execution of the current coroutine for 2 seconds, allowing other tasks to run concurrently during this time. It is designed to work within the `asyncio` event loop, enabling efficient handling of multiple asynchronous operations without blocking the main thread. This makes it suitable for use in asynchronous applications where responsiveness and concurrency are important.

### Q8. Can you explain the difference between synchronous and asynchronous programming in Python?
Synchronous programming in Python follows a sequential execution model, where each operation must complete before the next one begins. This means that if a task takes a long time to complete, it can block the entire program, leading to inefficiencies, especially in I/O-bound applications. In contrast, asynchronous programming allows for concurrent execution of tasks, enabling the program to handle multiple operations at the same time without blocking the main thread. Asynchronous programming is particularly useful for I/O-bound tasks, such as network requests or file operations, where waiting for responses can be done without halting the execution of other tasks.

### Q9. what is event loop in Python ?
An event loop in Python is a core component of asynchronous programming that manages the execution of asynchronous tasks and coroutines. It continuously checks for tasks that are ready to run, schedules them for execution, and handles their completion. The event loop allows for non-blocking operations by enabling the program to switch between tasks while waiting for I/O operations or other asynchronous events to complete. In Python, the `asyncio` library provides an event loop implementation that can be used to run asynchronous code, manage coroutines, and handle events efficiently. The event loop is responsible for coordinating the execution of multiple asynchronous tasks, ensuring that they are executed in a timely manner without blocking the main thread.

### Q10. What's the difference between simply using await task_one(); await task_two() and creating separate asyncio tasks?
The difference between using `await task_one(); await task_two()` and creating separate asyncio tasks lies in how the tasks are executed and managed:
- `await task_one(); await task_two()`: In this approach, the program will wait for `task_one()` to complete before starting `task_two()`. This means that the tasks are executed sequentially, and the second task cannot begin until the first one has finished. This can lead to inefficiencies if the tasks are independent and could be executed concurrently.
- Creating separate asyncio tasks:
```python
task1 = asyncio.create_task(task_one())
task2 = asyncio.create_task(task_two())
await task1
await task2
```
In this approach, both `task_one()` and `task_two()` are scheduled to run concurrently as separate tasks. The program does not wait for one task to complete before starting the other, allowing them to run in parallel. This can lead to improved performance and responsiveness, especially if the tasks are I/O-bound or independent of each other. By creating separate tasks, the event loop can manage their execution more efficiently, allowing for better utilization of system resources and faster completion of tasks. 

```text
Task 1
  ↓
Start
  ↓
await sleep(2)
  ↓
PAUSE
       ↘
        Event Loop
             ↓
          Task 2
             ↓
          Start
             ↓
        await sleep(1)
             ↓
           PAUSE
             ↓
        1 second
             ↓
        Task 2 End
             ↓
        Event Loop
             ↓
        Task 1 resumes
             ↓
        Task 1 End
```

In short: await waits for a coroutine's result, while asyncio.create_task() schedules the coroutine to run concurrently with other asyncio tasks.

async def makes a coroutine possible; await suspends the current coroutine; create_task() schedules independent coroutine work so the event loop can interleave it with other tasks.

### Q11. Explain the difference between concurrency and parallelism.
Concurrency is managing multiple tasks during overlapping periods; parallelism is executing multiple tasks literally at the same time.
```text
Concurrency
→ Multiple tasks make progress over overlapping time
→ asyncio is primarily designed for this
→ especially useful for I/O

Parallelism
→ Multiple tasks execute literally at the same time
→ typically requires multiple execution resources/cores
```

### Q12. what is the different between gather and wait in asyncio?
In `asyncio`, both `gather` and `wait` are used to manage multiple asynchronous tasks, but they serve different purposes and have distinct behaviors:
- `asyncio.gather(*tasks)`: This function is used to run multiple coroutines concurrently and collect their results. It takes a variable number of coroutine objects as arguments and returns a single coroutine that completes when all the input coroutines have finished. The results of the coroutines are returned in the order they were passed to `gather`, and if any of the coroutines raise an exception, `gather` will propagate that exception. It is useful when you want to run multiple tasks concurrently and need to collect their results.
```python
import asyncio


async def task_one():
    await asyncio.sleep(1)
    return "Task One Completed"


async def task_two():
    await asyncio.sleep(2)
    return "Task Two Completed"


async def main():
    results = await asyncio.gather(task_one(), task_two())
    print(results)  # Output: ['Task One Completed', 'Task Two Completed']


asyncio.run(main())
```
- `asyncio.wait(tasks, *, return_when=ALL_COMPLETED)`: This function is used to wait for a set of tasks to complete, but it does not return their results directly. It takes an iterable of tasks (coroutines or futures) and returns two sets: one containing the completed tasks and another containing the pending tasks. The `return_when` parameter allows you to specify when the function should return, such as when all tasks are completed, when the first task is completed, or when the first exception is raised. It is useful when you want to wait for tasks to finish but do not need to collect their results immediately.
```python
import asyncio


async def task_one():
    await asyncio.sleep(1)
    return "Task One Completed"


async def task_two():
    await asyncio.sleep(2)
    return "Task Two Completed"


async def main():
    tasks = [asyncio.create_task(task_one()), asyncio.create_task(task_two())]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    for task in done:
        print(task.result())  # Output: Task One Completed, Task Two Completed


asyncio.run(main())
```
```text
create_task()
    ↓
creates/schedules a Task
    ↓
await task
    ↓
get that task's result


gather()
    ↓
runs multiple awaitables concurrently
    ↓
waits for all
    ↓
returns all results together
```
In summary, `gather` is used when you want to run multiple coroutines concurrently and collect their results, while `wait` is used when you want to wait for a set of tasks to complete without necessarily collecting their results immediately.

***
```text
await
→ suspend current coroutine and wait for an awaitable

create_task()
→ schedule a coroutine as an independent asyncio Task

gather()
→ run multiple awaitables concurrently and collect their results
```
```text
async def
   ↓
creates coroutine function

await
   ↓
pause current coroutine
   ↓
give event loop opportunity to run other work

create_task()
   ↓
schedule independent coroutine

gather()
   ↓
run multiple awaitables concurrently
   ↓
collect their results
```