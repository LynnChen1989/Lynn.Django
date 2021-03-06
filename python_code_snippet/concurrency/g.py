import gevent
import socket

from gevent import monkey


urls = ['www.google.com', 'www.example.com', 'www.python.org']
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]

gevent.joinall(jobs, timeout=2)
print [job.value for job in jobs]
