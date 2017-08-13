import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logfile.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("This is an info message in logfile")



def add(x, y):
    '''Add Function'''
    return x + y

num1 = 10
num2 = 5

add_result = add(num1, num2)
logger.info('Add: {} + {} = {}' .format(num1, num2, add_result))
