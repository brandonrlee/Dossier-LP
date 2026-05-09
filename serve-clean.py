import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

class CleanURLHandler(SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.path.split('?', 1)[0].split('#', 1)[0]
        rel = path.lstrip('/')
        if rel and not rel.endswith('/') and not os.path.exists(rel) and os.path.isfile(rel + '.html'):
            self.path = '/' + rel + '.html' + self.path[len(path):]
        return super().send_head()

if __name__ == '__main__':
    ThreadingHTTPServer(('127.0.0.1', 8000), CleanURLHandler).serve_forever()
