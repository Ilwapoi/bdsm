# Welcome to Best Desition System Making
# this is the main file which run the application
# this application will based on pyramid by background
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from lib.DB_lib import PostgreSQL



def ping_route(request):
    return Response('pong')

def ping_database(request):
    db = PostgreSQL.DB()
    return Response(str(db.test_connection()))

if __name__ == '__main__':
    with Configurator() as config:
        #ping
        config.add_route('ping', '/ping')
        config.add_view(ping_route, route_name='ping')
        #database
        config.add_route('ping_database', '/ping/database')
        config.add_view(ping_database, route_name='ping_database')
        #finally
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
