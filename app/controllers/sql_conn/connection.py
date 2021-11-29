from urllib.parse import urlparse
import psycopg2
import os


def create_connection():
    result = urlparse(os.getenv("DATABASE_URL"))
    username = result.username
    password = result.password
    database = result.path[1:]
    hostname = result.hostname
    port = result.port

    ps = psycopg2.connect(
        user=username,
        password=password,
        host=hostname,
        port=port,
        database=database
    )

    return ps, ps.cursor()