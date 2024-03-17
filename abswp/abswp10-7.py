
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol needs to be 1 character')
    if (width < 2) or (height < 2):
        raise Exception('width and height must be greater than or equal to 2')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)
boxPrint('*',15,10)

import traceback
try:
    raise Exception('this is the error message')
except:
    errorFile = open('error_log.txt','a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('the traceback info was written error_log.txt')
