from cgi import parse_qs
from template_cal import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]  
    S=0 
    P=0
    if '' not in [a, b]:
	if a.isdigit() and b.digit():
            a, b = int(a), int(b)

            S=a+b
            P = a*b
            response_body = html+'sum: '+str(S)+', product:'+str(P)
	else:
	    response_body = html+'This supports only int value
    else:
	response_body = html+'There is(are) not inputted value(s)'
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
