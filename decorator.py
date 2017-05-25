import functools
'''
def log (func):
    def wrapper(*args,**kw):
        print 'call %s:' % func.__name__
        return func(*args,**kw)
    return wrapper
'''
 
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s %s():' % (text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print '2017-05-25'
now()   