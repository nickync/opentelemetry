import mq
import time
import functools

def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator

    return wrapper

class Test():

    def messenger(self):
        m = mq.MQ()
        return m
    
    @coroutine
    def sendMessage(self):
        msg = None
        while True:
            m = yield msg
            self.messenger().send(m)

    def run(self):
        co = self.sendMessage()
        for i in range(200):
            print(i)
            time.sleep(2)
            if (i % 6 == 0):
                co.send( 'Coroutine %s' % i)

te = Test()

if __name__ == '__main__':
    te.run()

    