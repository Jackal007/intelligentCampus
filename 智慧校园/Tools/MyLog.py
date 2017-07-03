import time
import sys

def myException(function):
    """
    A decorator that wraps the passed in function and logs 
    exceptions should one occur
    """
    def wrapper(*args, **kwargs):
#         try:
        return function(*args, **kwargs)
#         except:
#             # log the exception
#             info = sys.exc_info()  
#             with open('mylog.txt', 'a') as f:
#                 f.write(str(info[0]) + ":" + str(info[1]) + '\n')
    return wrapper
