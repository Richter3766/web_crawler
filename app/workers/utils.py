import threading

def create_threads(worker_function, num_threads, args):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=worker_function, args=args)
        threads.append(thread)
        thread.start()
    return threads