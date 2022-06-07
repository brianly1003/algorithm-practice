import threading
import os


def task1():
    print("Task 1 assigned to thread: {}\n".format(threading.current_thread().name))
    print("ID of process running task 1: {}\n".format(os.getpid()))


def task2():
    print("Task 2 assigned to thread: {}\n".format(threading.current_thread().name))
    print("ID of process running task 2: {}\n".format(os.getpid()))

if __name__ == "__main__": 
  
    # print ID of current process 
    print("ID of process running main program: {}\n".format(os.getpid())) 
  
    # print name of main thread 
    print("Main thread name: {}\n".format(threading.main_thread().name)) 
  
    # creating threads 
    t1 = threading.Thread(target=task1, name='t1') 
    t2 = threading.Thread(target=task2, name='t2')   
  
    # starting threads 
    t1.start() 
    t2.start() 
  
    # wait until all threads finish 
    t1.join() 
    t2.join() 