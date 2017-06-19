import aiomysql
import asyncio

"""
config = {
    'user': 'root',
    'host': '127.0.0.1',
    'port': 3306,
    'password': 'password',
    'db': 'test_pymysql',
}

async def aio_conn(loop=loop, **kw):
    conn = await aiomysql.connect(loop=loop, **kw)
    async with conn.cursor() as cur:
        await cur.execute('SELECT * FROM user')
        print(cur.description)
        r = await cur.fetchall()
        print(r)
    conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(aio_conn(loop=loop, **config))
"""


async def aio_conn(loop):
    conn = await aiomysql.connect(
        user='root',
        host='127.0.0.1',
        password='password',
        db='test',
        loop=loop,
    )
    async with conn.cursor() as cur:
        await cur.execute('SELECT * FROM user')
        print(cur.description)
        r = cur.fetchall()
        print(r)
    conn.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(aio_conn(loop))
