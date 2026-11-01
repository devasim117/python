# =================================================================== Multithreading
# 1. Thread
# 
import threading
import time

# --------- Single thread
# def task(name, age):
#     print(f"Hi {name} your age is {age}")

# t1 = threading.Thread(target=task, args=("Asim",))
# t1 = threading.Thread(target=task, args=("Asim",29))

# t1.start()
# t1.join()


# --------- Multiple thread
def task(name):
    print(f"Task {name} started")
    time.sleep(2)
    print(f"Task {name} finished")

# threads = []
# print(time.perf_counter())
# for i in range(5):
#     # task(i)
#     thread = threading.Thread(target=task, args=(i,))
#     thread.start()
#     threads.append(thread)
#     # print(thread,threads)

# for thread in threads:
#     thread.join()

# print("All threads ran")
# print(time.perf_counter())


# 2. Lock : When we want a variable has to be updated by single thread at a time. Then we locked it
# 3. Semaphore : When to hit multiple api but in limit

counter = 0
# lock = threading.Lock() # using lock
semaphore = threading.Semaphore(3) # using semaphore

def increment():
    global counter
    time.sleep(2)
    for _ in range(5000):
        # with lock:
        with semaphore:
            counter += 1

threads = []

for _ in range(5):
    thread = threading.Thread(
        target=increment
    )
    threads.append(thread)


for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


print(f"Expected: 25000")
print(f"Actual Counter: {counter}")


# 4. Queue
from queue import Queue

queue = Queue()

def producer():

    for i in range(10):

        print(f"Producing {i}")

        queue.put(i)

        time.sleep(0.5)


def consumer():

    while True:

        item = queue.get()

        print(f"Processing {item}")

        time.sleep(1)

        queue.task_done()


producer_thread = threading.Thread(
    target=producer
)

consumer_thread = threading.Thread(
    target=consumer,
    daemon=True
)

producer_thread.start()
consumer_thread.start()

producer_thread.join()

queue.join()

print("All tasks completed")




