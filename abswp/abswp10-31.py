import logging
import traceback


try:
    raise Exception('This is an error message.')
except:
    errorFile = open('error_log.txt','a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The Traceback info was written error_log.txt')


def boxPrint(symbol,width,height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be of length 1')
    if (width<2) or (height<2):
        raise Exception("Width and Height must be greater than or equal to 2")
    print(symbol*width)
    for i in range(height-2):
        print(symbol + ((width-2) * ' ') + symbol)
    print(symbol*width)

    
boxPrint('*',10,10)
boxPrint('O',2,15)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of second program')

def factorial(n):
    logging.debug('Start of function')
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is %s, total is %s' % (i,total))
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(50))

logging.debug('End of second program')

