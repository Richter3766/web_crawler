import threading

class WorkerManager:
    def __init__(self):
        self.threads = []
        self.working = True

    def create_threads(self, worker_function, num_threads, args, name = "임시"):
        for _ in range(num_threads):
            thread = threading.Thread(target=worker_function, args=args, name=name)
            self.threads.append(thread)
            thread.start()

    def wait_threads(self):
        self.working = False
        print("===================== 스레드 종료 시작 =====================")
        for i in range(len(self.threads)):
            self.threads[i].join()
            print(f"------------- {self.threads[i].name} 스레드 {i + 1} 종료 완료 -------------")

        print("===================== 스레드 종료 완료 =====================")