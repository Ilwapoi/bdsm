# Welcome to Best Desition System Making
# this is the main file which run the application
# this application will based on pyramid by background
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def ping_route(request):
    return Response('pong')

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('ping', '/ping')
        config.add_view(ping_route, route_name='ping')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
