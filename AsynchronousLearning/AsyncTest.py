def consumer():
    r=''
    while True:
        #yeild不仅可以返回一个值，还可以接受调用者发出的参数
        n=yield r
        if not n:
            return 
        print('[CONSUMER] Consuming %s' %n)
        r='200 OK'
    

def produce(c):
    n=0
    next(c)
    while n<5:
        n=n+1
        print('[PRODUCER] Producing %s...' %n)
        r=c.send(n)
        print('[PRODUCER] Consumer return %s' %r)
    c.close()


c=consumer()
produce(c)