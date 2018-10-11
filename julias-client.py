import sys

import pyjulius

import Queue


c = pyjulius.Client('localhost',10500)
try:
    c.connect()
except pyjulius.ConnectionError:
    print('Server tho shuru karle bhai')
    sys.exit(1)

client.start()
try:
    while 1:
        try:
            result=client.results.get(False)
        except Queue.Empty:
            continue
        print(result)
except KeyboardInterrupt:
        print('Bye! Look forward to hear from you soon')
        client.stop()
        client.join()
        client.disconnect()
