from asd1_queue import Queue

def rotate(queue : Queue, elements : int):
    for i in range(elements):
        queue.enqueue(queue.dequeue())
