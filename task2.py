# example of decoration function for measures function execution time
import time                                                

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print (f'''decorate function result: method name: {method.__name__}, args: {args}, te-ts: {te-ts}''')
        return result

    return timed

@timeit
def f1():
    time.sleep(1)
    print ('f1')

@timeit
def f2(a):
    time.sleep(2)
    print ('f2',a)


f1()
f2(42)
