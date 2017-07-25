'''
Created on 2017年7月22日

@author: zhenglongtian
'''

import sys, logging, logging.config

class Logger:
    '''
    日志类
    '''

    def __init__(self, filename='logger.log'):
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filename=filename,
            filemode='a'
        )

    def printLogs(self):
        '''
        输出到屏幕
        :return:
        '''

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)


def logger():
    '''
    测试用例
    :return:
    '''

    logger = Logger()
    logger.printLogs()
    logging.debug('This is debug message!')
    logging.info('This is info message!')
    logging.warning('This is warning message!')
    logging.error('This is error message!')


def loggerByConfig():
    '''
    通过读取日志配置文件记载日志
    :return:
    '''
    logging.config.fileConfig('logger.conf')
    logger = logging.getLogger('example01')
    logger.debug('This is debug message!')
    logger = logging.getLogger('example02')
    logger.error('This is error message!')

def myException(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            logger=Logger()
            info = sys.exc_info()
            logging.error(function.__doc__)
            logging.error(str(info[0]) + ":" + str(info[1]))
            print(function.__doc__)
    return wrapper
