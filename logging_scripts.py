import logging, time, os
logging.basicConfig(filename='debugging.log',level=logging.DEBUG)
logging.info('----- '+ 'Run of ' + os.path.basename(__file__) 
              + ' at time ' + time.strftime("%c") + ' -----')

def test_fn(x,y):
    z=x+y
    logging.debug('Added %d to %d and got %d' % (x,y,z))
    return z

print test_fn(4,6)
print os.path.basename(__file__)

logging.info('end record' + '\n')