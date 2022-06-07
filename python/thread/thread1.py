import threading

def print_cude(num):
    print("Cube: {}".format(num * num * num)) 

def print_square(num):
    print("Square: {}".format(num * num)) 

if __name__ == "__main__":
    # Creating threads
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cude, args=(10,))

    # Starting thread 1
    t1.start()
    # Starting thread 2
    t2.start()

    # Wait until thread 1 is completely executed
    t1.join()
    # Wait until thread 2 is completely executed
    t2.join()

    print("Done!")
    


