import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.debug('This message should go to the log file')