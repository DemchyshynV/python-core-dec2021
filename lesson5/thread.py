import threading

# def show(n):
#     for i in range(n):
#         print(i, threading.current_thread().name)
#
#
# thread1 = threading.Thread(target=show, args=(5,), name='thr1', daemon=True)
# thread2 = threading.Thread(target=show, args=(8,), name='thr2', daemon=True)
#
# thread1.start()
# thread1.join()
# thread2.start()
# thread2.join()
#
# print('Main Thread')


count = 0
lock = threading.Lock()


def inc():
    with lock:
        # lock.acquire()
        global count
        count += 1
        print(count)
        # lock.release()


threads = []
for _ in range(1000):
    thread = threading.Thread(target=inc)
    threads.append(thread)
    thread.start()

for item in threads:
    item.join()
