# threads
import threading
from contextlib import contextmanager

# threading to stored information
_local = threading.local()

@contextmanager
def acquire(*lock_state_state):

    # Object identifier to sort the lock
    lock_state_state = sorted(lock_state_state, key=lambda a: id(a))

    # checking the validity of previous locks
    acquired = getattr(_local, 'acquired', [])
    if acquired and max(id(lock_state) for lock_state in acquired) >= id(lock_state_state[0]):
        raise RuntimeError('lock_state Order Violation')

    # Collecting all the lock state.
    acquired.extend(lock_state_state)
    _local.acquired = acquired

    try:
        for lock_state in lock_state_state:
            lock_state.acquire()
        yield
    finally:
        # locks are released in reverse order.
        for lock_state in reversed(lock_state_state):
            lock_state.release()
        del acquired[-len(lock_state_state):]


# creating locks
lock_state_1 = threading.Lock()
lock_state_2 = threading.Lock()

# using acquire as there are more than one lock
def thread_1():
    while True:
        with acquire(lock_state_1, lock_state_2):
            print('Thread-1')


def thread_2():
    while True:
        with acquire(lock_state_2, lock_state_1):
            print('Thread-2')


t1 = threading.Thread(target=thread_1)

# daemon thread runs without blocking
# the main program from exiting
t1.daemon = True
t1.start()

t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()
