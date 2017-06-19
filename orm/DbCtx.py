import mysql.connector
# from datetime import date


class DbCtx(object):
    '''
    A database context which use lazy connection
    '''

    def __init__(self, db_name):
        '''
        common args are user, password, database, host, port
        '''
        if not db_name:
            db_name = 'default'
        self.config = DATABASES[db_name]
        # print(self.config)
        self.config.update(autocommit=True)
        self._conn = None
        self.transactions = None

    def __del__(self):
        self._conn.close()
        print('Connection closed!')

    @property
    def connection(self):
        if self._conn is None:
            self._conn = mysql.connector.connect(**self.config)
        return self._conn

    def cursor(self, buf=False):
        return self.connection.cursor(buffered=buf)

    def select(self, sql, *args, **kw):
        '''
        The raw select method which return cursor directly
        if you specific the buffered to be False then the cursor must be closed after use
        '''
        buffered = kw.get('buffered', True)
        curs = self.cursor(buffered)
        curs.execute(sql, args)
        # print(curs.fetchall())
        return curs

    def select_dict(self, sql, *args, **kw):
        '''
        Return list of dict
        '''
        try:
            cursor = self.select(sql, *args)
            names = [x[0] for x in cursor.description]
            first = kw.get('first', False)
            if first:
                values = cursor.fetchone()
                if not values:
                    return None
                return dict(zip(names, values))
            return [dict(zip(names, x)) for x in cursor.fetchall()]
        finally:
            if cursor:
                cursor.close()

    def update(self, sql, *args):
        try:
            cur = self.cursor()
            cur.execute(sql, args)
            return cur.rowcount
        finally:
            cur.close()


if __name__ == '__main__':
    DATABASES = {
        'default': {
            'user': 'root',
            'password': 'password',
            'database': 'test'
        }
    }
    db = DbCtx('default')
    # print(db)
    """
    db.update(
        'insert into user (name,birthday) values (%s, %s)',
        'Lucy',
        date(1990, 8, 10))
    """
    # sel = db.select('select * from user')
    # print(sel)
    sd = db.select_dict('select * from user')
    print(sd)
