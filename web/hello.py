#hello.py

def application(environ,start_respose):
    start_respose('200 OK',[('Content-Type','text/html')])
    body='<h1>Hello,%s!</h1>' %(environ['PATH_INFO'][1:] or 'web')
    return [b'<h1>hello,web!</h1>']