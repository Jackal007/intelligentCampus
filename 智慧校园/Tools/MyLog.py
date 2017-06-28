import time

def myException(function):
    """
    A decorator that wraps the passed in function and logs 
    exceptions should one occur
    """
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            # log the exception
            err = "There was an exception in  "
            err += function.__name__
            with open('mylog.txt','a') as f:
                f.write(err+'\n')
    return wrapper
