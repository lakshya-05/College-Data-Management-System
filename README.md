# College-Data-Management-System
A small Python project using File Handling and Error Handling.

## Use Case:

### Personal Task Management:
- Organize daily, weekly, or project-related tasks.
- Keep track of to-do items and prioritize them.
- Monitor progress by marking tasks as completed.
- Easily view both pending and completed tasks.

## Key Concepts:

### Use of vector:
- The core of the application relies on the std::vector class from the C++ Standard Template Library (STL).
- vector provides a dynamic array, allowing the list of tasks to grow or shrink as needed.
- It offers efficient memory management and provides functions for adding, removing, and accessing elements, making it suitable for managing a list of tasks.

### Data Storage:
- Two std::vector objects are used, tasks (Stores the list of pending tasks) and completed (Stores the list of completed tasks).
  
### User Interface:
- A menu-driven interface allows the user to interact with the application.
- Options include adding new tasks, viewing tasks, marking tasks as complete, and deleting tasks.

### Input/Output:
- The code uses cin and cout for user input and output.
- getline(cin, task); is used to read input lines containing spaces correctly.

### Function-Based Design:
The code is organized into well-defined functions (AddTask(), ViewTasks(), MarkTaskCompleted(), DeleteTask()), improving code readability and maintainability.
