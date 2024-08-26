
# Function to query data from the database through an SSH tunnel
def query_data(ssh_host, ssh_user, ssh_port, ssh_private_key, sql_hostname, sql_username, sql_password, sql_database, sql_port, query):
    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_pkey=ssh_private_key,
            remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        conn = pymysql.connect(
            host='127.0.0.1',
            user=sql_username,
            passwd=sql_password,
            db=sql_database,
            port=tunnel.local_bind_port
        )
        data = pd.read_sql_query(query, conn)
        conn.close()
    return data


# database_utils.py

from sshtunnel import SSHTunnelForwarder
import pymysql
import pandas as pd
from contextlib import contextmanager

@contextmanager
def ssh_tunnel(ssh_host, ssh_port, ssh_user, ssh_pkey, sql_hostname, sql_port):
    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_pkey=ssh_pkey,
            remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        yield tunnel.local_bind_port

@contextmanager
def db_connection(local_port, sql_username, sql_password, sql_database):
    conn = pymysql.connect(
        host='127.0.0.1',
        user=sql_username,
        passwd=sql_password,
        db=sql_database,
        port=local_port
    )
    try:
        yield conn
    finally:
        conn.close()

def query_data(conn, query):
    return pd.read_sql_query(query, conn)
