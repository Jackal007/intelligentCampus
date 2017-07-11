import time
import sys

def myException(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            info = sys.exc_info()  
            with open('mylog.txt', 'a') as f:
                f.write("[" + str(time.time()) + "]: " + function.__doc__ + "\t")
                f.write(str(info[0]) + ":" + str(info[1]) + '\n')
                print(function.__doc__)
    return wrapper
