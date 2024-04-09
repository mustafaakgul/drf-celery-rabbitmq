import time
from threading import Timer

def func(par1, par2):
    print("Called func")
    return par1 + par2


if __name__ == '__main__':
    t = Timer(5, func, [5, 6])

    #start_time = time.time()

    t.start()

    #end_time = time.time()
    """
    if end_time - start_time < 5:
        print("Timer will wait for sometime before calling the function")
    else:
        print("5 seconds already passed. Timer finished calling func()")
    """


"""
Here, the main program came to the last line before 5 seconds were up, so Timer makes the program wait until it calls func().

After calling func(a, b), it terminates the program, since there is nothing else to run.

Also notice that the return value of the function cannot be used by the main program.

Hopefully, this gave you some more ideas about scheduling and waiting for intervals.
"""