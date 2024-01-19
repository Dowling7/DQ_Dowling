from multiprocessing import Process
import time

def task1():
    time.sleep(5)  # Simulates a task taking 5 seconds
    print("Task 1 completed")

def task2():
    time.sleep(10)  # Simulates a task taking 10 seconds
    print("Task 2 completed")
