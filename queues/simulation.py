import random

from queue import BasicQueue


class Printer(object):
    def __init__(self, ppm):
        self.pagerate = ppm
        self.current_task = None
        self.remaining_time = 0

    def tick(self):
        if self.current_task is not None:
            self.remaining_time -=1
            if self.remaining_time <= 0:
                self.current_task = None

    @property
    def busy(self):
        return self.current_task is not None

    def start_next(self, new_task):
        self.current_task = new_task
        self.remaining_time = new_task.pages * 60 / self.pagerate


class Task(object):
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.pages = random.randrange(1, 21)

    def wait_time(self, current_time):
        return current_time - self.timestamp


def new_print_task():
    if random.randrange(1, 181) == 180:
        return True
    return False


def simulation(seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = BasicQueue()
    waiting_times = []

    for current_second in range(seconds):
        if new_print_task():
            print_queue.enqueue(Task(current_second))

        if not lab_printer.busy and not print_queue.empty:
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print('Average Wait {:.2f} secs {} tasks remaining.'.format(average_wait, print_queue.size))

if __name__ == '__main__':
    for _ in range(10):
        simulation(3600, 5)
