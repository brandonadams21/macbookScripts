import os
import psutil
import tkinter as tk
from tkinter import messagebox

# Define performance thresholds (adjust as needed)
CPU_THRESHOLD = 80  # CPU usage percentage
MEMORY_THRESHOLD = 80  # Memory usage percentage

# ASCII art rocket
rocket = [
    "    ^",
    "  /|_|\\",
    "  |___|",
    "  | B |",
    "  |___|",
    "  | A |",
    "  |___|",
    " /_____\\",
    "  |   |",
    "  |___|",
    "   ***",
    "   ***"
]

# Function to print the rocket animation
def print_rocket():
    os.system("clear")
    for line in rocket:
        print(line)

# Function to monitor system performance
def monitor_system_performance():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent

    # Display CPU and Memory usage in the console
    print_rocket()
    print(f"CPU Usage: {cpu_percent}%")
    print(f"Memory Usage: {memory_percent}%")

    # Check if thresholds are exceeded
    if cpu_percent > CPU_THRESHOLD or memory_percent > MEMORY_THRESHOLD:
        show_alert(cpu_percent, memory_percent)

    # Schedule the function to run again after a delay
    root.after(10000, monitor_system_performance)

# Function to display an alert
def show_alert(cpu_percent, memory_percent):
    alert_text = f"System Alert!\nCPU Usage: {cpu_percent}%\nMemory Usage: {memory_percent}%"
    messagebox.showwarning("System Alert", alert_text)

# Create the main GUI window (hidden)
root = tk.Tk()
root.withdraw()

# Start monitoring system performance
monitor_system_performance()

# Run the GUI main loop
root.mainloop()
