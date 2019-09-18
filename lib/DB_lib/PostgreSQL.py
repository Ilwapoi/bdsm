import psycopg2
from lib.logs_lib.errors_responce import error_pretty_print as pretty_error

class DB:
    def __init__(self, password = 'olegoleg', username = 'postgres', host = 'localhost', port = '5432', database = 'postgres'):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def create_connection(self):
        try:
            connection = psycopg2.connect(  user = self.username
                                          , password = self.password
                                          , host = self.host
                                          , port = self.port
                                          , database = self.database)
            return {'result': connection}
        except Exception as e:
            return pretty_error(e)

    def execute(self, request, commit = False):
        try:
            conn_result = self.create_connection()
            if hasattr(conn_result,'result'):
                conn = conn_result['result']
                cursor = conn.cursor()
                cursor.execute(request)
                if commit:
                    cursor.commit()
                cursor.close()
                conn.close()
                return {'result':'Success'}
            else:
                return conn_result
        except Exception as e:
            return pretty_error(e)

    def test_connection(self):
        try:
            self.execute('select 1')
            return True
        except Exception as e:
            return False, pretty_error(e)
