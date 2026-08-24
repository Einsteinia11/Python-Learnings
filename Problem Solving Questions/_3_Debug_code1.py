# A debugger lets you pause the program while it is running and inspect what is happening line by line.
"""
Debugger: Runs the program while allowing you to inspect its execution.

Breakpoint: Pauses the program at a specific line.

Continue (F5): Continues execution until the next breakpoint or program end.

Step Over (F10): Executes the current line and moves to the next line.

Step Into (F11): Goes inside a function being called.

Step Out (Shift + F11): Exits the current function and returns to the calling line.

Variables: Shows the current values of variables while the program is paused.

Watch: Monitors specific variables or expressions during execution.

Call Stack: Shows the sequence of functions that led to the current execution point.

Restart: Starts the debugging session again.

Stop: Terminates the debugging session.

"""
numbers = [10, 20, 30, 40, 50]
total = 0

for i in range(1, len(numbers)):
    total = total + numbers[i]

average = total / len(numbers)
print("Total:", total)
print("Average:", average)